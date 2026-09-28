from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    tenant_id: int
    role: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str