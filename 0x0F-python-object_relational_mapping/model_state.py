#!/usr/bin/python3
"""
This Script contains the class definition of a State and an
Instance.
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class for creating a table in MySQL database
    """

    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
