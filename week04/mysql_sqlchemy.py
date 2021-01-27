#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
#from . import dbdy_gain

Base = declarative_base()

dburl = "mysql+pymysql://root:xxxxxxx@127.0.0.1:3306/douban_dy?charset=utf8mb4"
engine = create_engine(dburl, echo=False, encoding="utf-8")

# 使用sqlalchemy orm创建表

class dbdy_table(Base):
    __tablename__ = 'dbdy'
    dbdy_id = Column(Integer(), primary_key=True, index=True, nullable=False)
    dbdy_name = Column(String(50), nullable=False)
    dbdy_time = Column(String(20), nullable=False)
    dbdy_star = Column(String(50))
    dbdy_content = Column(String(2000), nullable=False)
    
    def __repr__(self):
        return "dbdy_table(dbdy_name='{self.dbdy_name}', dbdy_time='{self.dbdy_time}', dbdy_star='{self.dbdy_star}', dbdy_content='{self.dbdy_content}')".format(self=self)
Base.metadata.create_all(engine)

    
    
#使用sqlalchemy orm插入数据
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
with open('res.text', 'r') as f:
    ss = f.read()
    dy_info = eval(ss)
    d_len = len(dy_info['names'])
    #print(dy_info['contents'][0])
    for i in range(d_len):
        dbdy_demo = dbdy_table(dbdy_name=dy_info['names'][i], dbdy_time=dy_info['times'][i],dbdy_star=dy_info['stars'][i],dbdy_content=dy_info['contents'][i])
        session.add(dbdy_demo)
        
session.commit()
    


    
