from server.apiServer import app
from src.infrastructure.repository.mysql.user import UserRepository

repo = UserRepository()

repo.getUserByEmail()
