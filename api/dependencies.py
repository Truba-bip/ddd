from repositories.user_repository import UserRepository
from repositories.order_repository import OrderRepository
from services.user_services import UserService
from services.order_services import OrderService


def users_service():
    return UserService(UserRepository)

def orders_service():
    return OrderService(OrderRepository)