#!/usr/bin/python3
"""
This Script contains the class definition of a State and an
Instance.
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column("name", String(128), nullable=False)

    
