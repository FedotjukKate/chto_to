from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .db_session_holiday import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'Order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text)