class UserEntity:
    userId: str
    email: str
    firstName: str
    lastName: str

    def __init__(self, userId, email, firstName, lastName) -> None:
        self.userId = userId
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    @staticmethod
    def createUserEntity(userId, email, firstName, lastName):
        return UserEntity(userId, email, firstName, lastName)
