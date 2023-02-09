import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

BaseModel = declarative_base()

class Publisher (BaseModel):
    __tablename__ = 'publisher'

    id = sq.Column(sq.BigInteger(), primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'{self.name}'


class Book (BaseModel):
    __tablename__ = 'book'

    id = sq.Column(sq.BigInteger(), primary_key=True)
    title = sq.Column(sq.String(length=60))
    id_publisher = sq.Column(sq.BigInteger(), sq.ForeignKey('publisher.id'))

    bind_publisher = relationship(Publisher)

    def __str__(self):
        return f'{self.title}'


class Shop (BaseModel):
    __tablename__ = 'shop'

    id = sq.Column(sq.BigInteger(), primary_key=True)
    name = sq.Column(sq.String(length=60))

    def __str__(self):
        return f'{self.name}'


class Stock (BaseModel):
    __tablename__ = 'stock'

    id = sq.Column(sq.BigInteger(), primary_key=True)
    count = sq.Column(sq.BigInteger())
    id_book = sq.Column(sq.BigInteger(), sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.BigInteger(), sq.ForeignKey('shop.id'))

    bind_book = relationship(Book)
    bind_shop = relationship(Shop)

    def __str__(self):
        return f'{self.id_shop}'



class Sale (BaseModel):
    __tablename__ = 'sale'

    id = sq.Column(sq.BigInteger(), primary_key=True)
    price = sq.Column(sq.String(length=60))
    date_sale = sq.Column(sq.String(length=20))
    count = sq.Column(sq.BigInteger())
    id_stock = sq.Column(sq.BigInteger(), sq.ForeignKey('stock.id'))

    bind_stock = relationship(Stock)

    def __str__(self):
        return f'{self.id_stock} | {self.price} | {self.date_sale} | {self.count}'



def create_db(engine):
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)








































