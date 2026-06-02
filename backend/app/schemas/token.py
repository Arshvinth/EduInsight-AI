from pydantic import BaseModel


# Schema for login token response
class Token(BaseModel):
    access_token: str
    token_type: str


# Schema for token payload data
class TokenData(BaseModel):
    username: str | None = None


# Schema for user login payload
class UserLogin(BaseModel):
    username: str
    password: str


# defines what the login response looks like