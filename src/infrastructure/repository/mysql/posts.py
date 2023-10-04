from ...database.mysql.connector import initalizeDb
from mysql import connector
from ....domain.ports.postsRepositoryPort import PostRepositoryPort
from ....domain.entities.post import PostEntity


class PostRepository(PostRepositoryPort):
    def getAllPosts(self, paginationInfo: dict):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM social_media.posts OFFSET {paginationInfo['pageNumber'] * paginationInfo['totalItems']} ROWS FETCH NEXT {paginationInfo['totalItems']} ONLY"
                )
                fetchedData = cursor.fetchall()
                return fetchedData

        except connector.Error as e:
            print(e)
        finally:
            myDb.close()

    def getAllPosts(self, userId: str, paginationInfo: dict):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM social_media.posts WHERE userId = '{userId}' OFFSET {paginationInfo['pageNumber'] * paginationInfo['totalItems']} ROWS FETCH NEXT {paginationInfo['totalItems']} ONLY"
                )
                fetchedData = cursor.fetchall()
                return fetchedData
        except connector.Error as e:
            print(e)
        finally:
            myDb.close()

    def createPost(self, post: PostEntity):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO social_media.posts (postId, title, content, userId) VALUES ('{post.postId}', '{post.title}', '{post.content}', '{post.userId}')"
                )
                fetchedData = cursor.fetchone()

                myDb.commit()

                return fetchedData
        except connector.Error as e:
            print(e)
        finally:
            myDb.close()

    def createPost(self, post: PostEntity):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute(
                    f"UPDATE social_media.posts SET title = '{post.title}', content = '{post.content}' WHERE postId = '{post.postId}'"
                )
                fetchedData = cursor.fetchone()

                myDb.commit()

                return fetchedData
        except connector.Error as e:
            print(e)
        finally:
            myDb.close()
