from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .db_session_holiday import SqlAlchemyBase


class EmployeePosition(SqlAlchemyBase):
    __tablename__ = 'Employee_Position'

    employee_position_id = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(ForeignKey('Employee.employee_id'), nullable=False)
    id_position = Column(ForeignKey('Position.position_id'), nullable=False)

    Employee = relationship('Employee')
    Position = relationship('Position')
