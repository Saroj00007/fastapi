from sqlmodel import SQLModel , create_engine , Session




Database_url = (
    "postgresql+psycopg://"
    "fastapi_user:fastapi_user@localhost:5432/fastapi_db"
)


#  engine is the connection manager with the database 

engine  = create_engine(
    Database_url , 
    echo= True
    
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session
    