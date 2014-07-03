from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from task1 import settings
import mysql.connector

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(32))
    description = Column('description', String(200), nullable=True)
    link = Column('link', String(100), nullable=True)
    location = Column('location', String(70), nullable=True)
    category = Column('category', String(70), nullable=True)
    original_price = Column('original_price', String(15), nullable=True)
    price = Column('price', String(15), nullable=True)