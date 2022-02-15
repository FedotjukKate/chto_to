from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .db_session_holiday import SqlAlchemyBase


class EmployeeOrder(SqlAlchemyBase):
    __tablename__ = 'Employee_Order'

    employee_order_id = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(ForeignKey('Employee.employee_id'), nullable=False)
    id_order = Column(ForeignKey('Order.order_id'), nullable=False)

    Employee = relationship('Employee')
    Order = relationship('Order')