class Figure:
    pass


class Serializer:
    @staticmethod
    def serialize(self, x, y):
        d = {"type": self.figure, "color": self.color, "width": self.brush_size, "coords": self.coords}

        with open(r'example.json', 'w') as file:
            file.write(str(d))
