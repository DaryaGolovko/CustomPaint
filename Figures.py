from Figure import Figure


class Line(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_line(self.coords,
                              fill=self.color, width=self.brush_size)
        self.x, self.y = x, y


class Ellipse(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_oval(self.coords,
                              fill=self.color, outline=self.color)


class Rectangle(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_rectangle(self.coords,
                                   fill=self.color, outline=self.color)


class Polygon(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_polygon(self.coords,
                                 fill=self.color, outline=self.color)


class LineSegment(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_polygon(self.coords, fill=self.color,
                                 outline=self.color, width=self.brush_size)
