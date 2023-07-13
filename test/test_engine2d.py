import pyglet
import pytest

from engine2d.colors import Colors
from engine2d.engine2d import Engine2D


@pytest.fixture(autouse=True)
def engine2d():
    engine2d = Engine2D(800, 600)

    yield engine2d


@pytest.mark.parametrize("test_input", [(100, 150, 100), (0, 0, 0), (100.0, 150.5, 100.7), (-100, -150, -100),
                                        (-100.1, -150.2, -100.3), (2000, -5000, 3000)])
def test_circle_positive(capsys, test_input, engine2d):
    engine2d.add_circle(test_input[0], test_input[1], test_input[2])
    engine2d.draw()

    out, err = capsys.readouterr()

    assert out == f"Drawing Circle: {(test_input[0], test_input[1])} with radius = {test_input[2]}" \
                  f" and color {engine2d.color.name}\n"


@pytest.mark.parametrize("test_input,expected", [(("100", 150, 100), 'must be real number, not str'),
                                                 ((0, "0", 0), 'must be real number, not str'),
                                                 ((100.0, 150.5, "100.7"),
                                                  "unsupported operand type(s) for /: 'str' and 'float'")])
def test_circle_negative(capsys, test_input, expected, engine2d):
    with pytest.raises(TypeError) as err:
        engine2d.add_circle(test_input[0], test_input[1], test_input[2])
        engine2d.draw()

    assert str(err.value) == expected


@pytest.mark.parametrize("test_input", [(100, 150, 100, 200), (0, 0, 0, 0), (100.0, 150.5, 100.7, 10.8),
                                        (-100, -150, -100, -200),
                                        (-100.1, -150.2, -100.3, -56.5), (2000, -5000, 3000, -1000)])
def test_rectangle_positive(capsys, test_input, engine2d):
    engine2d.add_rectangle(test_input[0], test_input[1], test_input[2], test_input[3])
    engine2d.draw()

    out, err = capsys.readouterr()

    assert out == f"Drawing Rectangle: {(test_input[0], test_input[1])} with width = {test_input[2]}, " \
                  f"height = {test_input[3]}" \
                  f" and color {engine2d.color.name}\n"


@pytest.mark.parametrize("test_input,expected", [(("100", 150, 100, 2), 'must be real number, not str'),
                                                 ((0, "0", 0, 0), 'must be real number, not str'),
                                                 ((100.0, 150.5, "100.7", 5),
                                                  "unsupported operand type(s) for +: 'int' and 'str'"),
                                                 ((100.0, 150.5, 100.7, "5"),
                                                  "unsupported operand type(s) for +: 'int' and 'str'")])
def test_rectangle_negative(capsys, test_input, expected, engine2d):
    with pytest.raises(TypeError) as err:
        engine2d.add_rectangle(test_input[0], test_input[1], test_input[2], test_input[3])
        engine2d.draw()

    assert str(err.value) == expected


@pytest.mark.parametrize("test_input", [(100, 150, 100, 200, 2, 3), (0, 0, 0, 0, 0, 0),
                                        (100.0, 150.5, 100.7, 10.8, 0.5, 5.5),
                                        (-100, -150, -100, -200, -6, -123),
                                        (-100.1, -150.2, -100.3, -56.5, -56.7, -555),
                                        (2000, -5000, 3000, -1000, -7777, -8888)])
def test_triangle_positive(capsys, test_input, engine2d):
    engine2d.add_triangle(test_input[0], test_input[1], test_input[2], test_input[3], test_input[4], test_input[5])
    engine2d.draw()

    out, err = capsys.readouterr()

    assert out == f"Drawing Triangle: first vertex {(test_input[0], test_input[1])}, " \
                  f"second vertex {(test_input[0] + test_input[2], test_input[1] + test_input[3])}, " \
                  f"third vertex {(test_input[0] + test_input[4], test_input[1] + test_input[5])} " \
                  f"with color {engine2d.color.name}\n"


@pytest.mark.parametrize("test_input,expected", [(("100", 150, 100, 200, 2, 3), 'must be real number, not str'),
                                                 ((0, "0", 0, 0, 0, 0), 'must be real number, not str'),
                                                 ((100.0, 150.5, "100.7", 10.8, 0.5, 5.5),
                                                  'can only concatenate str (not "int") to str'),
                                                 ((-100, -150, -100, "-200", -6, -123),
                                                  'can only concatenate str (not "int") to str'),
                                                 ((-100.1, -150.2, -100.3, -56.5, "-56.7", -555),
                                                  'can only concatenate str (not "int") to str'),
                                                 ((2000, -5000, 3000, -1000, -7777, "-8888"),
                                                  'can only concatenate str (not "int") to str')])
def test_triangle_negative(capsys, test_input, expected, engine2d):
    with pytest.raises(TypeError) as err:
        engine2d.add_triangle(test_input[0], test_input[1], test_input[2], test_input[3], test_input[4], test_input[5])
        engine2d.draw()

    assert str(err.value) == expected


def test_color(capsys, engine2d):
    engine2d.add_circle(0, 1, 2)
    engine2d.change_color(Colors.blue)
    engine2d.add_rectangle(0, 1, 2, 3)
    engine2d.change_color(Colors.green)
    engine2d.add_triangle(0, 1, 2, 3, 4, 5)
    engine2d.draw()

    out, err = capsys.readouterr()

    assert out == f"Drawing Circle: (0, 1) with radius = 2 and color red\n" \
                  f"Drawing Rectangle: (0, 1) with width = 2, height = 3 and color blue\n" \
                  f"Drawing Triangle: first vertex (0, 1), " \
                  f"second vertex (2, 4), third vertex (4, 6) with color green\n"
