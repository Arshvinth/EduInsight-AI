from pydantic import BaseModel


# Schema for login token response
class Token(BaseModel):
    access_token: str
    token_type: str


# Schema for token payload data
class TokenData(BaseModel):
    username: str | None = None



# defines what the login response looks like