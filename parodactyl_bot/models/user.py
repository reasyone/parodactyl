from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    role_id: int
    username: Optional[str]
    phone_number: Optional[str]
    full_name: Optional[str]
    city: Optional[str]