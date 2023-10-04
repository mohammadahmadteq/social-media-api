from mysql import connector


def initalizeDb():
    try:
        database = connector.connect(
            host="localhost", user="user", password="password", database="social_media"
        )
        return database
    except connector.Error as e:
        print(e)
