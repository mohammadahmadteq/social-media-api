from pydantic import BaseModel, constr


class CreateNewPostDTO(BaseModel):
    title: str
    content: str
    userId: constr(max_length=7)
