from pydantic import BaseModel

from fastapi import FastAPI

class items(BaseModel):
    name : str
    price : int | None

# app = FastAPI()

# @app.get("/status/{id}")
# def status(limit: int , id : int ):
#     return {"status" : "healthy! running successfully!!"  , 
#             "limit " : limit , 
#             "id " : id 
            
#             }

# path is simply used for path parameter and query is used for query paramater 


#  simply type hints ko barema janna paro

users:list[str] = ["saroj" , "roshan" , "hari" , 1]
# print(users)


obj : dict[int ,  str] = {1 : "saroj" , "saroj" : 2}

def test(item : items): 
    print(item)

# test({"name": "saroj kandel" })


def test(**numbers):
    print(numbers)


# test(name = "saroj kandel")


# oops concepts: 

class Vehicle:
   def __init__(self , name , price ):
          self.name = name
          self.price  = price
          
   def init(self):
        print(f"{self.name} is running")
        

lambo = Vehicle("lamborgini" , 10000000)
lambo.init()


from dataclasses import dataclass , field

@dataclass
class bike : 
    name : str 
    price : int
    category : str = "default normal"
    
    
kawasaki = bike("kawasaki" , 1000 , "sports")
# print(f"{kawasaki.name} || {kawasaki.price}")





