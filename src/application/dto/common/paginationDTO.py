from pydantic import BaseModel


class PaginationInfoDTO(BaseModel):
    pageNumber: int
    totalItems: int
