from Figure import Figure


class Line(Figure):

    @staticmethod
    def draw(self, x, y):
        self.canv.create_line(self.x, self.y, x, y,
                              fill=self.color, width=self.brush_size)
        self.x, self.y = x, y
        self.coords.append(self.x)
        self.coords.append(self.y)
        self.coords.append(x)
        self.coords.append(y)


class Ellipse(Figure):

    @staticmethod
    def draw(self, x, y):
        self.flag = False
        self.canv.create_oval(self.x, self.y, x, y,
                              fill=self.color, outline=self.color)
        self.coords.append(self.x)
        self.coords.append(self.y)
        self.coords.append(x)
        self.coords.append(y)


class Rectangle(Figure):

    @staticmethod
    def draw(self, x, y):
        self.flag = False
        self.canv.create_rectangle(self.x, self.y, x, y,
                                   fill=self.color, outline=self.color)
        self.coords.append(self.x)
        self.coords.append(self.y)
        self.coords.append(x)
        self.coords.append(y)


class Polygon(Figure):

    @staticmethod
    def draw(self, x, y):
        if self.polyflag == 2:
            self.canv.create_polygon(self.coords,
                                     fill=self.color, outline=self.color)
            self.polyflag = False
            self.flag = False
        elif self.polyflag == 1:
            self.coords.append(x)
            self.coords.append(y)


class LineSegment(Figure):

    @staticmethod
    def draw(self, x, y):
        self.flag = False
        self.canv.create_polygon(self.x, self.y, x, y,
                                 fill=self.color, outline=self.color, width=self.brush_size)
        self.coords.append(self.x)
        self.coords.append(self.y)
        self.coords.append(x)
        self.coords.append(y)
