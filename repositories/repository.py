from abc import ABC,abstractmethod
class AbstractRepository(ABC):
    @abstractmethod
    async def get_all():
        raise NotImplementedError
    @abstractmethod
    async def get():
        raise NotImplementedError
    @abstractmethod
    async def add():
        raise NotImplementedError
    @abstractmethod
    async def delete():
        raise NotImplementedError
    @abstractmethod
    async def update():
        raise NotImplementedError