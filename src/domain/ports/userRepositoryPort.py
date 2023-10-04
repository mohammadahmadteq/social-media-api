from abc import ABC, abstractmethod
from ..entities.user import UserEntity


class UserRepositoryPort(ABC):
    @abstractmethod
    def getUserByEmail(self, email: str):
        pass

    @abstractmethod
    def createUser(self, user: UserEntity):
        pass
