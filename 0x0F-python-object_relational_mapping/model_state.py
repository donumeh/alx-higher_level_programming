#!/usr/bin/python3

"""
Python script that contains the class definition of a State
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import declarative_base
# from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()


class State(Base):
    """
    A state object model
    """

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
