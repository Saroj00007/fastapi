from fastapi import FastAPI  , Path  , Depends , Request  , BackgroundTasks
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from typing import Annotated

from pydantic import BaseModel , Field
from jose import jwt
from datetime import datetime , timezone , timedelta

from passlib.context import CryptContext 

from fastapi.middleware.cors import CORSMiddleware

#  creating the hasing of password




app = FastAPI()

app.add_middleware(
    CORSMiddleware , 
    allow_origins=["http://localhost:3000"]  , 
    allow_credentials=True , 
    allow_headers=["*"] , 
    allow_methods=["*"]
)

@app.middleware("http")
async def middle(request :Request , call_next ):
    print("before the request")
    
    response = call_next(request)
    
    print("after request")
    
    return response


auth_schema = OAuth2PasswordBearer(tokenUrl= "login")


class User(BaseModel):
    name : str 
    email : str  
    password  :str



# first of all creating the context
pwd_conext = CryptContext(
    schemes=["bcrypt"] 
)

def hash_password(password : str):
    
    return pwd_conext.hash(password)
    
def verify_password(plain_password , hashed_password):
    
    isvalid = pwd_conext.verify(plain_password , hash_password)   
    return isvalid
    

def create_ascess_token(sub : dict , expiry_mins : int = 30):
    to_encoe = sub.copy 
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    
    to_encoe["exp"] = expire
    
    jwt_token = jwt.encode(
        to_encoe , 
        "saroj123" , 
        algorithm="HS256"
    )

def verify_jwttoken(token):
    jwt_decoded = jwt.decode(token , "saroj123" , algorithms=["HS256"])
    # this jwt_decoded name contain the encoded information inside jwt token
    return jwt_decoded  

create_ascess_token({"id" : "12"})


# password hashing 


def get_current_user(token : Annotated[str , Depends(auth_schema)]):

    #    token aayuxa eta basa teslai decode gara ani user data nikala
    user = decode_token(token)
    return user
    
def decode_token(token : str) : 
    return {
        "token" : "decoded: "+ token , 
        "name" : "saroj kandel" , 
        "email" : "saroj@gmail.com" , 
        "password" : "saroj1212"
    }


@app.get("/current-user")
def get_currentuser(user  :Annotated[User , Depends(get_current_user)] , background_task : BackgroundTasks):
    
    background_task.add_task("sending the email to the user or may be other tasks that is helpful ")
    return user
    



@app.get("/status/{name}" )
def status(name : str ): 
    return {"message" : f"{name} , hi"}




@app.post("/login" )
def login(form_data : Annotated[OAuth2PasswordRequestForm , Depends()]):
    
    #  verifies the username and password 
    
    ascess_token = "some-granted-token"
    
    return {
        "ascess_token" : ascess_token  , 
        "token_type"  :"bearer" , 
        "form_data" : form_data
    }

    
@app.get('/user/me')
def user_info(token : Annotated[str  , Depends(auth_schema)] ):
    
    # fetch the info from the token and get the user from the db
    
    return {
        "token : " : token
    }
    
    
#  middlewares : one of the important concepts in backend engineering 
