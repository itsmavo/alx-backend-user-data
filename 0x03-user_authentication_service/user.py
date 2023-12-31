#!/usr/bin/env python3
"""
SQLAlchemy model 'User' for DB table 'users'
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ( Column, Integer, String)

Base = declarative_base()


class User(Base):
    """ Definition of User class """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)
