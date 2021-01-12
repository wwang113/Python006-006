#!/usr/bin/env python3
'''
使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交
'''

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

dburl = "mysql+pymysql://testuser:Test!123pass@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=False, encoding="utf-8")

# 使用sqlalchemy orm创建表

class Userinfo_table(Base):
    __tablename__ = 'userinfo'
    userinfo_id = Column(Integer(), primary_key=True)
    userinfo_name = Column(String(50), index=True)
    userinfo_age = Column(Integer(), nullable=False)
    userinfo_birthday = Column(String(20), nullable=False)
    userinfo_sex = Column(String(10),nullable=False)
    userinfo_school = Column(String(20))
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)   
    
    def __repr__(self):
        return "Userinfo_table(userinfo_id='{self.userinfo_id}', userinfo_name='{self.userinfo_name}', userinfo_age='{self.userinfo_age}', userinfo_birthday='{self.userinfo_birthday}',\
        userinfo_sex='{self.userinfo_sex}', userinfo_school='{self.userinfo_school}', create_on='{self.create_on}', update_on='{self.update_on}')".format(self=self)
Base.metadata.create_all(engine)



# 使用pymysql插入数据
#def insert_table_sql():
    # db = pymysql.connect("127.0.0.1","testuser","Test!123pass","testdb")
    # try:
    #     with db.cursor() as cusor:
    #         sql = '''insert into userinfo (userinfo_id, userinfo_name, userinfo_age, userinfo_birthday, userinfo_sex, userinfo_school, create_on, update_on) values (%s, %s, %s, %s, %s, %s, %s, %s)'''
    #         values = (
    #             (1, "张三", 31, "1990.09.12", "男", "专科", datetime.now(), datetime.now()),
    #             (2, "李四", 30, "1991.10.10", "男", "本科", datetime.now(), datetime.now()),
    #             (3, "王五", 24, "1997.09.12", "女", "高中", datetime.now(), datetime.now()),
    #         )
    #         #cusor.execute(sql, value)
    #         cusor.executemany(sql, values)
    #     db.commit()
    # except Exception as e:
    #     print(f"insert error {e}")
    # finally:
    #     db.close()
    #    print(cusor.rowcount)
    
    
#使用sqlalchemy orm插入数据
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
userinfo_demo = Userinfo_table(userinfo_id=5, userinfo_name="周六", userinfo_age=32, userinfo_birthday="1990.09.12", userinfo_sex='男', userinfo_school="本科", create_on=datetime.now(), update_on=datetime.now())
userinfo_demo = Userinfo_table(userinfo_id=6, userinfo_name="张七", userinfo_age=22, userinfo_birthday="1999.08.22", userinfo_sex='女', userinfo_school="硕士", create_on=datetime.now(), update_on=datetime.now())
userinfo_demo = Userinfo_table(userinfo_id=7, userinfo_name="吴八", userinfo_age=27, userinfo_birthday="1994.06.02", userinfo_sex='男', userinfo_school="博士", create_on=datetime.now(), update_on=datetime.now())
  
session.add(userinfo_demo)
session.commit()
    
    
#使用sqlalchemy orm查询
result = session.query(Userinfo_table).all()
for result in session.query(Userinfo_table):
    print(result)
    
session.commit()

    
