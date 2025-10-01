# from pydantic import BaseModel


class User:
    id: str
    email:  str
    password_hash: str
    created_at: datetime
    is_active: bool

class Token:
    access_token: str
    token_type: str
    expires_in: int
