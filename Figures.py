from Figure import Figure


class Line(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_line(self.x, self.y, x, y,
                              fill=self.color, width=self.brush_size)
        self.x, self.y = x, y

    @staticmethod
    def serialization(self, x, y):
        self.canv.create_line(self.x, self.y, x, y,
                              fill=self.color, width=self.brush_size)


class Ellipse(Figure):

    @staticmethod
    def draw(self, x, y):
        self.flag = False
        self.canv.create_oval(self.x, self.y, x, y,
                              fill=self.color, outline=self.color)


class Rectangle(Figure):

    @staticmethod
    def draw(self, x, y):
        self.flag = False
        self.canv.create_rectangle(self.x, self.y, x, y,
                                   fill=self.color, outline=self.color)


class Polygon(Figure):

    @staticmethod
    def draw(self, x, y):
        if self.polyflag == 2:
            self.canv.create_polygon(self.coords,
                                     fill=self.color, outline=self.color)
            self.polyflag = False
            self.flag = False
            self.coords = []
        elif self.polyflag == 1:
            self.coords.append(x)
            self.coords.append(y)


class LineSegment(Figure):

    @staticmethod
    def draw(self, x, y):
        self.flag = False
        self.canv.create_polygon(self.x, self.y, x, y,
                                 fill=self.color, outline=self.color)
