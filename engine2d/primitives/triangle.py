from pyglet import shapes


class Triangle(shapes.Triangle):

    def __init__(self, x, y, x2, y2, x3, y3, color):
        super().__init__(x=x, y=y, x2=x2, y2=y2, x3=x3, y3=y3, color=color.value)
        self.color_name = color.name

    def draw(self):
        super().draw()
        print(f"Drawing Triangle: first vertex {(self.x, self.y)}, "
              f"second vertex {(self.x2, self.y2)}, third vertex {(self.x3, self.y3)} with color {self.color_name}")
