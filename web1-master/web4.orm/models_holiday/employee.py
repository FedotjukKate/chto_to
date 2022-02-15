from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .db_session_holiday import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'Employee'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    login = Column(Text, nullable=False)
    password = Column(Text, nullable=False)