from Figure import Figure


class Rectangle(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_rectangle(self.coords,
                                   fill=self.color, outline=self.color)
