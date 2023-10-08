from pydantic import BaseModel


class CreateNewPostDTO(BaseModel):
    title: str
    content: str
    userId: str
