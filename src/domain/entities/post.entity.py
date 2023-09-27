from pydantic import BaseModel


class PostEntity:
    def __init__(
        self, title: str, content: str, userId: str, votes: int, postId: str
    ) -> None:
        self.title = title
        self.content = content
        self.userId = userId
        self.votes = votes
        self.postId = postId

    @staticmethod
    def createPostEntity(
        title: str, content: str, userId: str, votes: int, postId: str
    ):
        return PostEntity(title, content, userId, votes, postId)
