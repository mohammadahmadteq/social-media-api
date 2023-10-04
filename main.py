from server.apiServer import app
from src.infrastructure.repository.mysql.user import UserRepository
from src.domain.ports import userRepositoryPort

repo = UserRepository()

user = {
    "userId": "3",
    "email": "c@c.com",
    "firstName": "jeph",
    "lastName": "adaxs",
    "password": "stiffBoi123123",
}

repo.createUser(user)
