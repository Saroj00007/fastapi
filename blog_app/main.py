from fastapi import FastAPI , Depends

from contextlib import asynccontextmanager

from sqlmodel import SQLModel , Session  , Field , select

from database import create_db_and_tables , get_session

class Product(SQLModel  ,table = True ): 
    id : int | None = Field(default=None , primary_key=True)
    name : str 
    price : float
    
    
class product_entry(SQLModel):
    name : str
    price : float
    
@asynccontextmanager
async def lifespan(app : FastAPI):
    create_db_and_tables()
    yield
    
app = FastAPI(lifespan=lifespan)

@app.post("/product")
def create_product(
    product_data : product_entry  , 
    session : Session = Depends(get_session)
): 
    
    product = Product(
        name  = product_data.name , 
        price= product_data.price
    )
    
    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product


@app.get("/products")
def get_product(
    session : Session = Depends(get_session)
): 
    
    products  = session.exec(select(Product)).all()
    
    return products
    