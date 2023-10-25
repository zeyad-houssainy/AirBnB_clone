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
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """return a specific format for the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """changes the date time to be the current moment when click [save]"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """create a dictionary out of the data entered"""
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        # for k,v in copy_dict.items():
        #     if k == "created_at" or k == "updated_at":
        #         v = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
        # print(copy_dict)
        return (copy_dict)



my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
# print(my_model)
my_model.save()
# print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
#           type(my_model_json[key]), my_model_json[key]))
