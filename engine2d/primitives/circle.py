from pyglet import shapes


class Circle(shapes.Circle):

    def __init__(self, x, y, radius, color):
        super().__init__(x=x, y=y, radius=radius, color=color.value)
        self.color_name = color.name

    def draw(self):
        super().draw()
        print(f"Drawing Circle: {(self.x, self.y)} with radius = {self.radius} and color {self.color_name}")
