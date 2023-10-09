from pydantic import BaseModel, constr


class UpdatePostDTO(BaseModel):
    title: str
    content: str
    postId: constr(max_length=7)
