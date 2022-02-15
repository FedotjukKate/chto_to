from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .db_session_holiday import SqlAlchemyBase


class ClientOrder(SqlAlchemyBase):
    __tablename__ = 'Client_Order'

    client_order_id = Column(Integer, primary_key=True, autoincrement=True)
    id_client = Column(ForeignKey('Client.client_id'), nullable=False)
    id_order = Column(ForeignKey('Order.order_id'), nullable=False)

    Client = relationship('Client')
    Order = relationship('Order')