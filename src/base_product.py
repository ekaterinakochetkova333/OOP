from abc import ABC, abstractmethod


class BaseProduct(ABC):
    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass