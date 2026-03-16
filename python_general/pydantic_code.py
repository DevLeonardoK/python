#most important library for data validation & parsing
#allows 'strict typing' by using type annotations (str,int,list...)

#allows developer to define clear and secure data models

#written in Rust

from pydantic import BaseModel
import pydantic
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
    print(f"Name: {user.name} -- Age: {user.age}")
except Exception as exception:
    print(exception)


print("\n")
    
    
#validation with pydantic
class Car(BaseModel):
    model:str
    year:int
    
try:
    car = Car(model="Fiat Uno", year='1996')
    print(f"Model type: {type(car.model).__name__} \n Year type: {type(car.year).__name__}")
except Exception as exception:
    print(exception)