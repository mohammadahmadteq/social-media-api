class PostEntity:
    def __init__(self, title: str, content: str, userId: str, postId: str) -> None:
        self.title = title
        self.content = content
        self.userId = userId
        self.postId = postId

    @staticmethod
    def createPostEntity(title: str, content: str, userId: str, postId: str):
        return PostEntity(title, content, userId, postId)
