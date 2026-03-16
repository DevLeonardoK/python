#most important library for data validation & parsing
#allows 'strict typing' by using type annotations (str,int,list...)

#allows developer to define clear and secure data models

#written in Rust

from pydantic import BaseModel
import pydantic
from typing import Optional, List

print(pydantic.__version__) #2.12.5

#validation without pydantic
class User:
    def __init__(self, age:int, name:str):
        
        if not isinstance(age, int):
            raise TypeError(f"Expected int, got {type(age).__name__}")
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name).__name__}")
        
        self.age = age
        self.name = name        
try:
    user = User(age=19,name="Leonardo")
    print("#validation without pydantic")
    print(f"Name: {user.name} -- Age: {user.age}\n")
except Exception as exception:
    print(exception)    
    
#validation with pydantic
class Car(BaseModel):
    model:str
    year:int
    
try:
    car = Car(model="Fiat Uno", year='1996')
    print("#validation with pydantic")
    print(f"Model type: {type(car.model).__name__} \n Year type: {type(car.year).__name__}\n")
except Exception as exception:
    print(exception)

#model fields – explicitly passed parameters
print(f"#model fields – explicitly passed parameters \n {car.model_fields_set}\n")

#helper methods - json
print("#helper methods - json \n")
print(f"1 - model_dump() dictionary-----> {car.model_dump()}\n")
print(f"2 - model_dump_json() json -----> {car.model_dump_json()}\n")
print(f"3 - model_json_schema() json more info-----> {car.model_json_schema()}\n")


#Nested models

class Food(BaseModel):
    name:str
    price:float
    ingredients: Optional[List[str]] = None

class Restaurant(BaseModel):
    name:str
    location:str
    foods: List[Food]

restaurant = Restaurant(name="Bistro 99",location="Brazil, Porto Alegre", foods=[{"name":"Steak","price":10.5,"ingredients":["steak","salt"]},
        {"name":"potato","price":7.0,"ingredients":["potato","cheese"]}])

print(restaurant.model_dump_json())