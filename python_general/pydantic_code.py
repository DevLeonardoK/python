#most important library for data validation & parsing
#allows 'strict typing' by using type annotations (str,int,list...)

#allows developer to define clear and secure data models

#written in Rust

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
    user = User(age=19,name=12)
    print(f"Name: {user.name} -- Age: {user.age}")
except Exception as exception:
    print(exception)