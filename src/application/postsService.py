from ..domain.ports.postsRepositoryPort import PostRepositoryPort
from ..domain.entities.post import PostEntity
from ..application.dto.post.createNewPostDto import CreateNewPostDTO
from ..application.dto.post.updatePostDto import UpdatePostDTO
from ..application.dto.common.paginationDTO import PaginationInfoDTO

from uuid import uuid4


class PostService:
    postRepository: PostRepositoryPort

    def __init__(self, postRepository: PostRepositoryPort) -> None:
        self.postRepository = postRepository

    def getAllPosts(self, paginationInfo: PaginationInfoDTO):
        try:
            posts: list = self.postRepository.getAllPosts(paginationInfo)
            return posts
        except:
            print("Database Error Occured")

    def getMyPost(self, userId: str, paginationInfo: PaginationInfoDTO):
        try:
            posts: list = self.postRepository.getMyPosts(userId, paginationInfo)
            return posts
        except:
            print("Database Error Occured")

    def createPost(self, PostDTO: CreateNewPostDTO):
        try:
            postId = str(uuid4())
            postEntity = PostEntity.createPostEntity(
                title=PostDTO.title,
                content=PostDTO.content,
                userId=PostDTO.userId,
                postId= str(postId),
            )
            posts = self.postRepository.createPost(postEntity)
            return postEntity
        except Exception as e:
            print("Database Error Occured", e)

    def updatePost(self, PostDTO: UpdatePostDTO):
        try:
            postEntity = PostEntity.createPostEntity(
                title=PostDTO.title,
                content=PostDTO.content,
                userId="dsg",
                postId=PostDTO.postId,
            )
            posts = self.postRepository.updatePost(postEntity)
            return postEntity
        except:
            print("Database Error Occured")
