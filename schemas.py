from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int
    priority: Optional[int] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_fits_bcrypt(cls, value: str) -> str:
        # bcrypt учитывает не больше 72 байт пароля, а bcrypt 5 на более длинном падает.
        if len(value.encode()) > 72:
            raise ValueError("Password is longer than 72 bytes")
        return value


class UserOut(BaseModel):
    id: int
    email: EmailStr

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
