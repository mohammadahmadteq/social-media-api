from pydantic import BaseModel

class BanUserDTO(BaseModel):
    userId: str
    reason: str
    timeHours: int
