
import re
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

class Email:

    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9]+[A-Za-z0-9._]*[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+$")

    def __init__(self, value):
        self.value = value
        if not self._is_valid():
            raise ValueError

    def _is_valid(self):
        return self.EMAIL_REGEX.match(self.value) is not None
