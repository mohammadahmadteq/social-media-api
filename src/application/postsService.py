from ..domain.ports.postsRepositoryPort import PostRepositoryPort
from ..domain.entities.post import PostEntity
from uuid import uuid4


class PostService:
    postRepository: PostRepositoryPort

    def __init__(self, postRepository: PostRepositoryPort) -> None:
        self.postRepository = postRepository

    def getAllPosts(self, paginationInfo: dict):
        try:
            posts = self.postRepository.getAllPosts(paginationInfo)
            return posts
        except:
            print("Database Error Occured")

    def getMyPost(self, userId: str, paginationInfo: dict):
        try:
            posts = self.postRepository.getMyPosts(userId, paginationInfo)
            print(posts)
        except:
            print("Database Error Occured")

    def createPost(self, PostDTO: dict):
        try:
            postId = uuid4()
            postEntity = PostEntity.createPostEntity(
                title=PostDTO.title,
                content=PostDTO.content,
                userId=PostDTO.userId,
                postId=postId[0:7],
            )
            posts = self.postRepository.createPost(postEntity)
            print(posts)
        except:
            print("Database Error Occured")

    def updatePost(self, PostDTO: dict):
        try:
            postEntity = PostEntity.createPostEntity(
                title=PostDTO.title,
                content=PostDTO.content,
                userId=PostDTO.userId,
                postId=PostDTO.postId,
            )
            posts = self.postRepository.updatePost(postEntity)
            print(posts)
        except:
            print("Database Error Occured")
