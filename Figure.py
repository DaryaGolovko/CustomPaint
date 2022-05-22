from abc import ABC, abstractmethod


class Figure(ABC):
    @staticmethod
    @abstractmethod
    def draw(self, x, y):
        pass
