#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_modl_json = my_model.to_dict()
print(my_modl_json)
print("JSON of my_model:")
for k in my_modl_json.keys():
    print("\t{}: ({}) - {}".format(k, type(my_modl_json[k]), my_modl_json[k]))
