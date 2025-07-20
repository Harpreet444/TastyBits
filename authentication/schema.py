from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user_name: str
    email: EmailStr
    user_id: str

class SignUpRequest(BaseModel):
    email: EmailStr
    password: str
    confirm: str

class SignUpResponse(BaseModel):
    email: str
    access: str
    refresh: str

class LogInRequest(BaseModel):
    email: EmailStr
    password: str
    
class LogInResponse(BaseModel):
    email: str
    access: str
    refresh: str