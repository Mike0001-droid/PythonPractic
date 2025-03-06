import requests
import pandas as pd
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime
from config_db.database import init_engine
import xlrd


class Base(DeclarativeBase):
    pass

class SpimexTradingResults(Base):
    __tablename__ = 'spimex_trading_results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    exchange_product_id = Column(String)
    exchange_product_name = Column(String)
    oil_id = Column(String)
    delivery_basis_id = Column(String)
    delivery_basis_name = Column(String)
    delivery_type_id = Column(String)
    volume = Column(String)
    total = Column(String)
    count = Column(String)
    date = Column(String)


engine = init_engine()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

url1 = 'https://spimex.com/upload/reports/oil_xls/oil_xls_20250305162000.xls?r=5165'
response = requests.get(url1)
with open('bulletin23.xlsx', 'wb') as file:
    file.write(response.content)

columns = [
    'Код Инструмента', 'Наименование Инструмента', 'Базис поставки', 
    'Объем Договоров в единицах измерения', 'Объем Договоров, руб.', 
    'Количество Договоров, шт.'
]

workbook = xlrd.open_workbook('bulletin23.xlsx')
worksheet = workbook.sheet_by_index(0)
for i in range(6, 18):
    for j in range(1, 15):
        cell = worksheet.cell_value(i, j)
        if j == 14 and i == 6:
            stroka =  'Количество Договоров, шт.'
            print(cell == stroka)
    print('')