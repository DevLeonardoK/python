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
from typing import Optional, List
print("#nested models ---- Optional and List\n")

class Food(BaseModel):
    name:str
    price:float
    ingredients: Optional[List[str]] = None

class Restaurant_1(BaseModel):
    name:str
    location:str
    foods: List[Food]

restaurant_1 = Restaurant_1(name="Bistro 99",location="Brazil, Porto Alegre", foods=[{"name":"Steak","price":10.5,"ingredients":["steak","salt"]},
        {"name":"potato","price":7.0,"ingredients":["potato","cheese"]}])


print(f"{restaurant_1.model_dump_json()}\n")

#Pydantic Types
#Field, conlist, EmailStr, HttpUrl,PositiveInt
#uv add pydantic[email]

print("#Field, conlist, EmailStr, HttpUrl,PositiveInt \n")

from pydantic import Field, conlist, EmailStr, HttpUrl,PositiveInt

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: int

class Employee(BaseModel):
    name: str
    position: str
    email: EmailStr

class Owner(BaseModel):
    name: str
    email: EmailStr

class Restaurant_2(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z0-9-' ]+$") 
    #pattern with raw string 'r'
    #... - not null field
    owner: Owner
    address: Address
    employees: conlist(Employee, min_length=2)
    number_of_seats: PositiveInt
    website: HttpUrl
    
    
address = Address(street="Rua Aurelios Rom",city="Porto Alegre",state="Rio Grande do Oeste", zip_code=12654258)

employee_1 = Employee(name="John",position="Supervisor",email="john@food.com")

employee_2 = Employee(name="Marta",position="Assistant", email="martafood@web.com")

owner = Owner(name="Andrew", email="andrewtok@hogm.com")

restaurant_2 = Restaurant_2(name="Garden 67", owner=owner, address=address, employees=[employee_1,employee_2],number_of_seats=40, website="https://www.garden67food.com")

print(f"{restaurant_2.model_dump_json()}\n")

print("#field_validator - single field\n")
from pydantic import field_validator

class Human(BaseModel):
    name: str
    age: int
    
    @field_validator('name')
    def validate_name(v): #v = field_validator(v)
        if ' ' not in v:
            raise ValueError("The name must contain a space")
        return v.upper()

try:
    human = Human(name="Leonardo ",age=19)
except Exception as e:
    print(e) 
else:
    print(f"{human}\n")


print("#model_validator - multiple fields")
from pydantic import model_validator, ValidationError
from typing import Any
class Signup(BaseModel):
    name: str
    age: int

    @model_validator(mode="before") #before validation/transform
    @classmethod
    def validate_data(cls, values: Any) -> Any:
        if 'password' in values:
            raise ValueError("Password should not be in the data")
        if 'user' in values:
            raise ValueError("User login should not be in the data")
        return values
    
    @model_validator(mode="after")
    def validate_object(self):
        if ' ' not in self.name:
            raise ValueError("The name must contain a space")
        return self
    
try:
    #case 1 signup = Signup(name="Leonardo",age=19, password="bluered123*")
    #case 2
        signup = Signup(name="Leonardo",age=19)
except ValidationError as e:
    print(e)
else:
    print(f"{signup}\n")
    
    
#Field
from uuid import uuid4
print("#Exploring 'Field'\n")

class Human(BaseModel):
    id:int = Field(...,default_factory=lambda: uuid4().hex)

try:
    human = Human()
except Exception as e:
    print(e)
else:
    print(f"id: {human.id}\n")
    
class Object(BaseModel):
    name: str = Field(..., max_length=5, alias="username")  # when using alias, the object must be initialized with the alias parameter
    age: int = Field(default=19, alias="years_old", ge=19, le=20) #greater or equal / less or equal ---> list[gt,ge,lt,le]
try:
    object = Object(username="leo", years_old=20)
except ValidationError as e:
    print(e)
else:
    print(f"{object.model_dump_json(by_alias=True)}\n")  # using model_dump_json(by_alias=True), the result will use the alias names
    
    # alias allows receiving API data using the alias name while using the internal variable name in the code
    

print("#Exploring 'Computed Fields ---> @property'\n")
from pydantic import computed_field

class Product(BaseModel):
    name:str = Field(..., max_length=15)
    price:float = Field(..., gt=0)
    quantity:int = Field(..., ge=0)
    
    @computed_field
    @property #mode after can use 'self'
    def total(self) -> float:
        sum_total = self.price * self.quantity
        return sum_total

try:    
    product = Product(name="keyboard",price=20.0, quantity=5)
except ValidationError as e:
    print(e)
else:
    print(f"{product.model_dump_json()} \n")

    
#dataclass
print("#using dataclass \n")

from dataclasses import dataclass, field

@dataclass
class Keyboard():
    name:str = field(default="keyboard")
    brand:str = field(default="default")
    length: int = field(default=0)

try:
    keyboard_1 = Keyboard(name="Fuji",brand="Razer", length="10")
    keyboard_2 = Keyboard()
except Exception as e:
    print(e)
else:
    print(f"{keyboard_1}\n{keyboard_2}\n")    

