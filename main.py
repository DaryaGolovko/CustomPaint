from tkinter import *
import Figures
from Figure import Figure
import Plugin
from JsonSerializer import Serializer


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.color = "black"
        self.brush_size = 2
        self.canv = Canvas(self, bg="white")
        self.figure = "Line"
        self.figures = Figure.__subclasses__()

        self.canv.grid(row=3, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)
        self.set_canvas()

        self.flag = False
        self.polyflag = 0
        self.x = 0
        self.y = 0
        self.coords = []

        self.obj = Serializer()
        self.serialization = False

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def serialize(self):
        self.serialization = True
        self.obj.serialize()
        l = self.obj.deserialize()

        for i in range(len(l)):
            restored = dict(l[i])
            if self.figures.count(restored["type"]) != 0:
                continue
            self.figure = restored["type"]
            self.color = restored["color"]
            self.brush_size = restored["width"]
            self.coords = restored["coords"]
            self.flag = True
            if self.figure == "Polygon":
                self.polyflag = 2
            self.draw_figure(self)

        self.serialization = False

    def draw_figure(self, event):
        if not self.flag:
            self.flag = True
            self.x, self.y = event.x, event.y
        else:
            for i in self.figures:
                if self.figure == i.__name__:
                    if not self.serialization:
                        if self.polyflag == 2:
                            self.polyflag = False
                            self.flag = False
                        elif self.polyflag == 1:
                            self.coords.append(event.x)
                            self.coords.append(event.y)
                            break
                        else:
                            if self.figure != "Line":
                                self.flag = False
                            self.coords.append(self.x)
                            self.coords.append(self.y)
                            self.coords.append(event.x)
                            self.coords.append(event.y)
                    i.draw(self, event.x, event.y)

            if self.polyflag != 1:
                self.obj.serialize_figure(self)
                self.coords = []

    def set_figure(self, figure):
        self.figure = figure
        self.flag = False

        if figure == "Polygon" and self.polyflag == 0:
            self.polyflag = 1
            self.draw_figure(self)
        elif figure == "Polygon" and self.polyflag == 1:
            self.polyflag = 2
            self.draw_figure(self)

    def set_canvas(self):

        self.parent.title("Paint")
        self.pack(fill=BOTH, expand=2)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(3, weight=1)

        self.canv.bind("<Button - 1>", self.draw_figure)
        self.canv.bind("<B1-Motion>", self.draw_figure)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)

        green_btn = Button(self, text="Green", width=10,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="Yellow", width=10,
                           command=lambda: self.set_color("yellow"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10,
                         command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        clear_btn = Button(self, text="Serialize", width=10,
                           command=lambda: self.serialize())
        clear_btn.grid(row=1, column=6, sticky=W)

        figure_lab = Label(self, text="Figure: ")
        figure_lab.grid(row=2, column=0, padx=2)

        counter = -1
        for i in self.figures:
            counter = counter + 1
            temp = Button(self, text=i.__name__, width=10,
                          command=lambda i=i: self.set_figure(i.__name__))
            temp.grid(row=2, column=1 + counter)


def main():
    root = Tk()
    root.geometry("850x500+300+300")
    Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()
