import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from Models import create_db, Publisher, Book, Shop, Sale, Stock

DSN = 'postgresql://postgres:postgres@localhost:5432/Home_6'
engine = sq.create_engine(DSN)

# Создаем Модели
create_db(engine)

# Создаем сессию и экземпляр сессии
Session = sessionmaker(engine)
sess = Session()

# 1/Создаем экземпляры Писателей
pub1 = Publisher(name='Толстой')
pub2 = Publisher(name='Булгаков')
pub3 = Publisher(name='Лермонтов')
pub4 = Publisher(name='Пушкин')


# 2/Создаем экземпляры книг
book1 = Book(title='Война и мир', bind_publisher=pub1)
book2 = Book(title='Мастер и Маргарита', bind_publisher=pub2)
book3 = Book(title='Анна Каренина', bind_publisher=pub1)
book4 = Book(title='Бородино', bind_publisher=pub3)
book5 = Book(title='У лукоморья', bind_publisher=pub4)
book6 = Book(title='Узник', bind_publisher=pub4)



# 3/Создаем экземпляры магазинов
shop1 = Shop(name='Цум')
shop2 = Shop(name='Литератор')
shop3 = Shop(name='Магазин книг')


# 4/Создаем экземпляры Стоков
stock1 = Stock(count=20, bind_book=book1, bind_shop=shop1)
stock2 = Stock(count=5, bind_book=book2, bind_shop=shop2)
stock3 = Stock(count=70, bind_book=book3, bind_shop=shop3)
stock4 = Stock(count=15, bind_book=book4, bind_shop=shop2)
stock5 = Stock(count=25, bind_book=book5, bind_shop=shop1)
stock6 = Stock(count=100, bind_book=book6, bind_shop=shop3)



# 5/Создаем экземпляры продаж
sale1 = Sale(price='15 000', date_sale='12.10.2022', count=25, bind_stock=stock1)
sale2 = Sale(price='20 000', date_sale='15.10.2021', count=10, bind_stock=stock2)
sale3 = Sale(price='15 000', date_sale='12.11.2022', count=20, bind_stock=stock3)
sale4 = Sale(price='18 000', date_sale='16.10.2021', count=18, bind_stock=stock4)
sale5 = Sale(price='21 000', date_sale='18.09.2022', count=12, bind_stock=stock5)
sale6 = Sale(price='22 000', date_sale='10.11.2021', count=16, bind_stock=stock6)
sale7 = Sale(price='26 000', date_sale='12.10.2022', count=24, bind_stock=stock5)
sale8 = Sale(price='13 000', date_sale='30.10.2021', count=10, bind_stock=stock4)


# Добавляем и закрываем сессию
sess.add_all([pub1, pub2, pub2, pub4])
sess.add_all([book1, book2, book3, book4, book5, book6])
sess.add_all([shop1, shop2, shop3])
sess.add_all([stock1, stock2, stock3, stock4, stock5, stock6])
sess.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8])

sess.commit()



# Запросы

# 1/Запрос
question1 = input("Введите название Писателя:")
print(f'\nВсе книги писателя по фамилии {question1}:')
for a in sess.query(Book).join(Publisher).filter(Publisher.name == question1):
    print(a)

# 2/Запрос
question2 = input("\nВведите название Магазина:")
print(f'\nВсе книги, проданные в магазине: {question2}:')
for b in sess.query(Book).join(Publisher).join(Stock).join(Shop).filter(Shop.name == question2):
    print(b)

# 3/Запрос
question3 = input("\nВведите название Писателя:")
print(f'\nВсе покупки книг, написанные писателем: {question3}:')
for c in sess.query(Sale).join(Stock).join(Book).join(Publisher).filter(Publisher.name == question3):
    print(f'{c.count} | {c.price}')










# print('\nКнига конкретная:')
# for b in sess.query(Book).filter(Book.title == 'Узник'):
#     print(b)
#
# print('\nКниги по Автору:')
# for b in sess.query(Book).join(Publisher).filter(Publisher.name == 'Толстой'):
#     print(b)


































