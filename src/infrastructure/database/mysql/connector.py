from mysql import connector


def initalizeDb():
    try:
        with connector.connect(
            host="localhost", user="user", password="password", database="social_media"
        ) as database:
            return database
    except connector.Error as e:
        print(e)
