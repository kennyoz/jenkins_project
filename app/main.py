from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My FastAPI Project")


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate) -> UserResponse:
    return UserResponse(
        id=1,
        name=user.name,
        email=user.email,
    )