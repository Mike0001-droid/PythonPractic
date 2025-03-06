from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import  Column, Integer, String, ForeignKey
from config_db.database import init_engine


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)


class Genre(Base):
    __tablename__ = "genre"
 
    name = Column(String, nullable=False)


class Author(Base):
    __tablename__ = "author"
 
    name = Column(String, nullable=False)


class Book(Base):
    __tablename__ = "book"
 
    title = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    genre = relationship("Genre", back_populates="books")
    author = relationship("Author", back_populates="books")


class City(Base):
    __tablename__ = "city"
 
    name = Column(String, nullable=False)
    days_delivery = Column(Integer, nullable=False)


class Client(Base):
    __tablename__ = "client"
 
    name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    email = Column(String, nullable=False)
    city = relationship("City", back_populates="clients")


class Buy(Base):
    __tablename__ = "buy"
 
    buy_description = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    client = relationship("Client", back_populates="buys")


class BuyBook(Base):
    __tablename__ = "buybook"
 
    buy_id = Column(Integer, ForeignKey('buy.id'), nullable=False)
    book = Column(Integer, ForeignKey('book.id'), nullable=False)

    buy = relationship("Buy", back_populates="buybooks")
    book = relationship("Book", back_populates="buybooks")


class Step(Base):
    __tablename__ = "step"
 
    name = Column(String, nullable=False)


class BuyStep(Base):
    __tablename__ = "buystep"
 
    buy_id = Column(Integer, ForeignKey('buy.id'), nullable=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False)

    buy = relationship("Buy", back_populates="buysteps")
    step = relationship("Step", back_populates="buysteps")


Base.metadata.create_all(init_engine())