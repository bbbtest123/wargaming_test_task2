import pyglet

from engine2d.colors import Colors
from engine2d.primitives.circle import Circle
from engine2d.primitives.rectangle import Rectangle
from engine2d.primitives.triangle import Triangle


class Engine2D:

    def __init__(self, width, height, color=Colors.red):
        display = pyglet.canvas.get_display()
        screen = display.get_default_screen()

        template = pyglet.gl.Config(alpha_size=8)
        config = screen.get_best_config(template)
        context = config.create_context(None)
        self.window = pyglet.window.Window(width, height, context=context)
        self.shapes = []
        self.color = color

    def change_color(self, color):
        self.color = color

    def add_circle(self, x, y, radius):
        self.shapes.append(Circle(x, y, radius, self.color))

    def add_rectangle(self, x, y, width, height):
        self.shapes.append(Rectangle(x, y, width, height, self.color))

    def add_triangle(self, x, y, x2, y2, x3, y3):
        self.shapes.append(Triangle(x, y, x2, y2, x3, y3, self.color))

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        for shape in self.shapes:
            shape.draw()
        self.window.clear()
