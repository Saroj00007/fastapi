from fastapi import APIRouter

router = APIRouter()

@router.get("/check")
def check():
    return {"message" : "this is the router scope "}

