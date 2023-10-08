from pydantic import BaseModel


class CreateNewUserDTO(BaseModel):
    email: str
    password: str
    firstName: str
    lastName: str
