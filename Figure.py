from abc import ABC, abstractmethod
import ast


class Figure(ABC):
    @staticmethod
    @abstractmethod
    def draw(self, x, y):
        pass


class Serializer:

    def __init__(self):
        self.l = []

    def serialize_figure(self, figure):
        d = {"type": figure.figure, "color": figure.color, "width": figure.brush_size, "coords": figure.coords}
        self.l.append(d)

    def serialize(self):
        result = {"figures": self.l}

        with open(r'example.json', 'w') as file:
            file.write(str(result))

    @staticmethod
    def deserialize() -> list:
        with open(r'example.json') as file:
            l = list(ast.literal_eval(file.read())["figures"])
        return l
