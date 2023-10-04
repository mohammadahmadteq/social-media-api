from ...database.mysql.connector import initalizeDb
from mysql import connector
from ....domain.ports.userRepositoryPort import UserRepositoryPort
from ....domain.entities.user import UserEntity


class UserRepository(UserRepositoryPort):
    def getUserByEmail(self, email: str):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM social_media.users WHERE email = '{email}'"
                )
                fetchedData = cursor.fetchone()
                return fetchedData

        except connector.Error as e:
            print(e)
        finally:
            myDb.close()

    def createUser(self, user: UserEntity, password: str):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO social_media.users (userId, email, firstName, lastName, password) VALUES('{user.userId}','{user.email}','{user.firstName}','{user.lastName}', '{password}');"
                )
                fetchedData = cursor.fetchone()

                myDb.commit()

                return fetchedData

        except connector.Error as e:
            print(e)
        finally:
            myDb.close()
