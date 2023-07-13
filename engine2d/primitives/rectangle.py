from pyglet import shapes


class Rectangle(shapes.Rectangle):

    def __init__(self, x, y, width, height, color):
        super().__init__(x=x, y=y, width=width, height=height, color=color.value)
        self.color_name = color.name

    def draw(self):
        super().draw()
        print(f"Drawing Rectangle: {(self.x, self.y)} with width = {self.width}, "
              f"height = {self.height} and color {self.color_name}")
