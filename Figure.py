from abc import ABC, abstractmethod


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
        print(self.l)
        

    def serialize(self):
        result = {"figures": self.l}

        with open(r'example.json', 'w') as file:
            file.write(str(result))

    @staticmethod
    def deserialize(figure):
        with open(r'example.json') as file:
            restored = dict(file.read())
            figure.figure = restored["type"]
            figure.color = restored["color"]
            figure.brush_size = restored["width"]
            figure.coords = restored["coords"]
