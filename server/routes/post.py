from fastapi import APIRouter, HTTPException
from src.application.dto.common.paginationDTO import PaginationInfoDTO
from src.application.postsService import PostService
from src.application.dto.post.createNewPostDto import CreateNewPostDTO
from src.infrastructure.repository.mysql.posts import PostRepository
from src.application.dto.post.updatePostDto import UpdatePostDTO

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


@router.get("/myPosts")
async def getMyPosts(pageNumber: int, totalItems: int, userId: str):
    paginatationInfoDto = PaginationInfoDTO(
        pageNumber=pageNumber, totalItems=totalItems
    )
    posts = postService.getMyPost(paginationInfo=paginatationInfoDto, userId=userId)
    return {"posts": posts}


@router.post("/create")
async def createNewPost(createNewPostDto: CreateNewPostDTO):
    posts = postService.createPost(PostDTO=createNewPostDto)
    return {"posts": posts}


@router.put("/update")
async def updatePost(createNewPostDto: UpdatePostDTO):
    posts = postService.updatePost(PostDTO=createNewPostDto)
    return {"posts": posts}
