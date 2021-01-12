#!/usr/bin/env python3

'''
张三给李四通过网银转账 100 极客币，现有数据库中三张表：
一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
'''



from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.sql.sqltypes import DECIMAL, Float


Base = declarative_base()
dburl = "mysql+pymysql://testuser:Test!123pass@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=False, encoding="utf-8")

# 使用sqlalchemy orm创建表

class User_table(Base):
    __tablename__ = 'user'
    user_id = Column(Integer(), primary_key=True, nullable=False)
    user_name = Column(String(50), nullable=False)
    
    def __repr__(self):
        return "User_table(user_id='{self.user_id}', user_name='{self.user_name}')".format(self=self)

class Money_table(Base):
    __tablename__ = 'money'
    id = Column(Integer(), primary_key=True, nullable=False)
    money_id = Column(Integer(), ForeignKey("user.user_id"), nullable=False)
    money_sum = Column(DECIMAL(10,3), nullable=False)
    
    def __repr__(self):
        return "Money_table(money_id='{self.money_id}', money_sum='{self.money_sum}')".format(self=self)


class Audit_table(Base):
    __tablename__ = 'audit'
    audit_id = Column(Integer(), primary_key=True, nullable=False)
    audit_transfer_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)
    autid_transfer_id = Column(Integer(), nullable=False)
    autid_totransfer_id = Column(Integer(), nullable=False)
    autid_transfer_money = Column(DECIMAL(10,3), nullable=False)
 
    def __repr__(self):
        return "Audit_table(audit_id='{self.audit_id}',audit_transfer_time='{self.audit_transfer_time}', autid_transfer_id='{self.autid_transfer_id}',\
        autid_totransfer_id='{self.autid_totransfer_id}', autid_transfer_money='{self.autid_transfer_money}')".format(self=self)

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f'{e}')

# 添加用户
# user1_demo = User_table(user_id=1, user_name="张三")
# user2_demo = User_table(user_id=2, user_name="李四")

# session.add(user1_demo)
# session.add(user2_demo)

# money1_demo = Money_table(money_id=1, money_sum=120)
# money2_demo = Money_table(money_id=2, money_sum=30)

# session.add(money1_demo)
# session.add(money2_demo)
# session.commit()

# 转账分为三步走：
# 1、验证转账的用户是否存在，用户的资产总额是否满足需求；
# 2、被转账的用户是否存在，存在则进行转账；不在进行报错；
# 3、记录转账的记录；

from_transfer_user = input("请输入转账人姓名：" )
to_transfer_user = input("请输入转给人姓名：" )
trans_money = input("请输入转账金额： ")
transfer_money = int(trans_money)

def transfer_process(fromuser, touser, transmoney):
    user1 = session.query(User_table).filter(User_table.user_name == fromuser).first()
    if user1.user_name:
        user1_money = session.query(Money_table).filter(Money_table.money_id == user1.user_id).first()
        if user1_money.money_sum < transfer_money:
            print(f'{fromuser}账户余额不足,还剩下{user1_money}.')
        else:
            session.query(Money_table).filter(Money_table.money_id == user1.user_id).update({Money_table.money_sum: user1_money.money_sum - transfer_money})
            try:
                user2 = session.query(User_table).filter(User_table.user_name == touser).first()
            #if user2.user_name:
                user2_money = session.query(Money_table).filter(Money_table.money_id == user2.user_id).first()
                session.query(Money_table).filter(Money_table.money_id == user2.user_id).update({Money_table.money_sum: user2_money.money_sum + transfer_money})
                audit_demo = Audit_table(audit_transfer_time=datetime.now(), autid_transfer_id=user1.user_id, autid_totransfer_id=user2.user_id, autid_transfer_money=transfer_money)
                session.add(audit_demo)
            #else:
            except Exception as e:
                print(f'{touser} info error,please check; error info {e}')
                session.rollback()     
    else:
        print(f'{fromuser} account info is error , {e}')
        
    session.commit()


if __name__ == '__main__':
    transfer_process(from_transfer_user, to_transfer_user, transfer_money)