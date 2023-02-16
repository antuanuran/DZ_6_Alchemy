import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_db, Publisher, Book, Shop, Stock, Sale

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
book2 = Book(title='Мастер и маргарита', bind_publisher=pub2)
book3 = Book(title='Анна Каренина', bind_publisher=pub1)
book4 = Book(title='Бородино', bind_publisher=pub3)
book5 = Book(title='У Лукоморья', bind_publisher=pub4)
book6 = Book(title='Узник', bind_publisher=pub4)

# 3/Создаем экземпляры магазинов
shop1 = Shop(name='Цум')
shop2 = Shop(name='Литератор')
shop3 = Shop(name='Магазин книг')

# 4/Создаем экземпляры Стоков
stock1 = Stock(count=20, bind_book=book1, bind_shop=shop1)
stock2 = Stock(count=12, bind_book=book2, bind_shop=shop2)
stock3 = Stock(count=6, bind_book=book3, bind_shop=shop3)
stock4 = Stock(count=70, bind_book=book4, bind_shop=shop2)
stock5 = Stock(count=28, bind_book=book5, bind_shop=shop1)
stock6 = Stock(count=100, bind_book=book6, bind_shop=shop3)

# 5/Создаем экземпляры Распродаж
sale1 = Sale(price='15 000 р.', date_sale='12.10.2022', count=25, bind_stock=stock1)
sale2 = Sale(price='25 000 р.', date_sale='12.11.2022', count=10, bind_stock=stock2)
sale3 = Sale(price='35 000 р.', date_sale='12.05.2022', count=12, bind_stock=stock3)
sale4 = Sale(price='17 000 р.', date_sale='15.03.2022', count=16, bind_stock=stock4)
sale5 = Sale(price='19 000 р.', date_sale='12.02.2023', count=18, bind_stock=stock5)
sale6 = Sale(price='12 000 р.', date_sale='12.01.2023', count=31, bind_stock=stock6)
sale7 = Sale(price='21 000 р.', date_sale='12.10.2022', count=33, bind_stock=stock5)
sale8 = Sale(price='23 000 р.', date_sale='02.12.2022', count=41, bind_stock=stock4)


# Добавляем и закрываем сессию
sess.add_all([pub1, pub2, pub3, pub4])
sess.add_all([book1, book2, book3, book4, book5, book6])
sess.add_all([shop1, shop2, shop3])
sess.add_all([stock1, stock2, stock3, stock4, stock5, stock6])
sess.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8])

sess.commit()



# Запросы:

# 1/ Запрос. Вывести все книги писателя по его Фамилии
question1 = input('1.Введите фамилию писателя:')
print(f'\nВсе книги писателя по фамилии: {question1}:')
for x in sess.query(Book).join(Publisher).filter(Publisher.name == question1):
    print(f'| {x.title:15} |')


# 2/ Запрос. Ввести название магазина и вывести все книги, которые есть в этом магазине
question2 = input('\n2. Введите название магазина:')
print(f'\nВсе книги, которые есть в магазине: {question2}:')
for x in sess.query(Book).join(Stock).join(Shop).filter(Shop.name == question2):
    print(f'| {x.title:15} |')


# 3/ Запрос. Ввести фамилию писателя и вывести все магазины, где продаются книги данного писателя
question4 = input('\n3. Введите фамилию писателя:')
print(f'\nВсе магазины, где продаются книги писателя по фамилии: {question4}:')
for x in sess.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == question4):
    print(f'| {x.name:15} |')


# 4/ Запрос. Ввести фамилию писателя и вывести: название книги, магазин, кол-во проданных книг, стоимость и дату продажи
question4 = input('\n4. Введите фамилию писателя:')
print(f'\nВся информация по продажам писателя по фамилии: {question4}:')
for x in sess.query(Sale).join(Stock).join(Book).join(Publisher).filter(Publisher.name == question4):
    print(f'| {x.bind_stock.bind_book.title:15} | {x.bind_stock.bind_shop.name:18} | {x.count:3} | {x.price:10} | {x.date_sale:10} |')



































