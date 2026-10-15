from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(title="Airabook Enterprise Demo API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EnterpriseSigninRequest(BaseModel):
    proposed_account_name: str = Field(min_length=1)
    workspace_slug: str = Field(min_length=1)
    website: str = Field(min_length=1)
    country: str = Field(min_length=1)
    contact_person_name: str = Field(min_length=1)
    contact_email: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    business_description: str = Field(min_length=20)
    terms_accepted: bool


class EnterpriseLoginRequest(BaseModel):
    flow: str = "enterprise_login"
    workspace_slug: str = Field(min_length=1)
    contact_email: str = Field(min_length=1)
    password: str = Field(min_length=1)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/signin", status_code=status.HTTP_201_CREATED)
def enterprise_signup(payload: EnterpriseSigninRequest):
    
    return  {
    "status": "pending_approval",
    "message": "Enterprise onboarding request submitted for System Admin approval.",
    "request_id": f"demo-{uuid4()}",
    "workspace_url": f"{payload.workspace_slug}.airabook.com",
    "created_at": datetime.now(timezone.utc).isoformat(),
}


@app.post("/login", status_code=status.HTTP_201_CREATED)
def enterprise_login(payload: EnterpriseLoginRequest):
    print({
        "status": "demo_signed_in",
        "message": "Enterprise login successful.",
        "request_id": f"demo-{uuid4()}",
        "workspace_url": f"{payload.workspace_slug}.airabook.com",
        "email": payload.contact_email,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })
    return {
        "status": "demo_signed_in",
        "message": "Enterprise login successful.",
        "request_id": f"demo-{uuid4()}",
        "workspace_url": f"{payload.workspace_slug}.airabook.com",
        "email": payload.contact_email,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )

