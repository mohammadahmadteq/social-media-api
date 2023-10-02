from ...database.mysql.connector import initalizeDb


class UserRepository:
    def getUserByEmail(email: str):
        myDb = initalizeDb()

        try:
            with myDb.cursor() as cursor:
                cursor.execute("SELECT * FROM social_media.users WHERE email = a@a.com")
                returned_data = cursor.fetchall()
                for result in returned_data:
                    print(result)
        except:
            print("errro")
