
from pydantic import BaseModel , Field
from fastapi import FastAPI
from typing import Annotated , Union

from fastapi.encoders import jsonable_encoder

from typing import Annotated

from fastapi import Cookie ,Depends ,  Path , Header , Query , status , File , UploadFile , Form , HTTPException

task_list = []

def depends_params(q : str = "default"  , limit : int | None = None , skip : int = 10 ):
    return {"q" : q , "limit" : limit , "skip" : skip}
    



class form_model(BaseModel):
    name : str = Field(description="this is the name of the user" , ge=50)
    age : int
    hobby : list[str] | None = None  # this is the optional field
    

class depends_demo:
    def __init__(self , q : str = "default" , limit : int = 10):
        self.q = q 
        self.limit = limit


class query_params(BaseModel):
     
    model_config = {"extra" : "forbid"}
    
    limit : str = Field(title="this is the limit query" , default="hello")


class tasks(BaseModel):
    id : Annotated[int , "this id must be unique for all the task"]
    description : str
    priority : str = Field(description="this is the priority set that helps to rank the priority of the task" , max_length=100 )
    
    
class response(BaseModel):
    status : str | int
    message : str = "this is the default value" , 
    task_id : int

app = FastAPI(dependencies=[Depends(depends_demo)])


@app.post("/task" , response_model=response , status_code=status.HTTP_201_CREATED)
def create_task(task : tasks ,
                # registration_form : form_model = Form(),
                query_params : Annotated[dict  , Depends(depends_params)]
                
                ):
    
    json_format = jsonable_encoder(task)
    print(json_format) # now this is the json format data you can store it in db
    
    task_list.append(task)
    
    return {"status" : "ok" , 
            "message" : "the task is created successfully" ,
            "name" : registration_form.name
            }



@app.get("/task/{task_id}")
def get_task(task_id : int ,  depends_query : Annotated[depends_demo , Depends()] ):
    for task in task_list : 
        if(task.id == task_id):
            return task
        
@app.delete("/task/{task_id}")
def delete_task(task_id : int , session_id : str = Cookie() , x_token : str | None = Header(default=None)):
        for task in task_list : 
             if(task.id == task_id):
                task_list.remove(task)
                return{"message" : "deleted successfully" , "tasks" : task_list}



@app.post("/files/upload" , tags=["delete task"] , status_code= status.HTTP_204_NO_CONTENT , summary="this is the delete api" , deprecated=True)
def file_upload(file : bytes = File() ):
    
    if len(file) == 1212: 
        raise HTTPException(status_code=400 , detail="the file not found!!")
    
    return {"filelen" : len(file)}

