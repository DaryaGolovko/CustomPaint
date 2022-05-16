from Figure import Figure


class Trapeze(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_polygon(self.x, self.y, self.x, y - 50, x, self.y - 50, x, self.y,
                                 fill=self.color, width=self.brush_size)
        self.flag = False
