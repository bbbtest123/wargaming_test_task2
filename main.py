import pyglet

from engine2d.colors import Colors
from engine2d.engine2d import Engine2D


if __name__ == '__main__':
    engine2d = Engine2D(800, 600)
    engine2d.add_circle(100, 150, 100)
    engine2d.add_rectangle(200, 200, 200, 200)
    engine2d.change_color(Colors.blue)
    engine2d.add_triangle(50, 60, 70, 80, 90, 100)

    engine2d.draw()
