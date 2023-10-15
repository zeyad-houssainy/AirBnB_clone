#!/usr/bin/python3
"""Basemodel for the whole project"""
import unittest
import uuid
from datetime import datetime


class BaseModel():
    """Represents a BaseModel for airBNB clone project"""
    def __init__(self, *agrs, **kwargs):
        """Define for BaseModel
            *args: not used
            **kwargs: key:value of attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
    
    def __str__(self):
        """return a specific format for the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        




