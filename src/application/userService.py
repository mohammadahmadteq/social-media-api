from ..domain.ports.userRepositoryPort import UserRepositoryPort
from .dto.user.createUserDto import CreateNewUserDTO
from .dto.user.banUserDto import BanUserDTO

class UserService:
    userRepository: UserRepositoryPort

    def __init__(self, userRepository: UserRepositoryPort) -> None:
        self.userRepository = userRepository
    
    def createUser(self, createUserDto: CreateNewUserDTO):
        pass
    
    def banUser(self, blockUserDto: BanUserDTO):
        pass

    def deleteUser(self, userId: str):
        pass