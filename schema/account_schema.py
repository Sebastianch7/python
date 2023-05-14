from pydantic import BaseModel
from typing import Optional

class AccountSchema(BaseModel):
    name: str
    numberid: int
    accountid: int
    current: int
    