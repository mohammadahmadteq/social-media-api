from fastapi import APIRouter, HTTPException
from src.application.dto.common.paginationDTO import PaginationInfoDTO
from src.application.postsService import PostService
from src.infrastructure.repository.mysql.posts import PostRepository

postService = PostService(PostRepository())

router = APIRouter(
    prefix="/posts", tags=["posts"], responses={404: {"message": "No data found"}}
)


@router.get("/")
async def getAllPosts(pageNumber: int, totalItems: int):
    paginatationInfoDto = PaginationInfoDTO(
        pageNumber=pageNumber, totalItems=totalItems
    )
    posts = postService.getAllPosts(paginationInfo=paginatationInfoDto)
    return {"posts": posts}
