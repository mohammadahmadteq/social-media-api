from abc import ABC, abstractmethod

from ..entities.post import PostEntity


class PostRepositoryPort(ABC):
    @abstractmethod
    def getAllPosts(self, pagination: dict):
        pass

    @abstractmethod
    def getMyPosts(self, userId: str, pagination: dict):
        pass

    @abstractmethod
    def createPost(self, post: PostEntity):
        pass

    @abstractmethod
    def updatePost(self, post: PostEntity):
        pass
