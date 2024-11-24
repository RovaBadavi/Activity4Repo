from polygon import Polygon
import pytest

def test_polygon_initialization():
    p1 = Polygon("Triangle", [3.0, 3.0, 3.0])

    assert p1.name == "Triangle"
    assert p1.sides == [3.0, 3.0, 3.0]

def test_get():
    p2 = Polygon("Square", [4.0, 4.0, 4.0, 4.0])

    assert p2.get_name() == "Square"
    assert p2.get_sides() == [4.0, 4.0, 4.0, 4.0]

def test_set():
    p2 = Polygon("Square", [4.0, 4.0, 4.0, 4.0])

    p2.set_name("Pentagon")
    p2.set_sides([5.0, 5.0, 5.0, 5.0, 5.0])

    assert p2.get_name() == "Pentagon"
    assert p2.get_sides() == [5.0, 5.0, 5.0, 5.0, 5.0]

def test_polygon_equality():
    triangle = Polygon("Triangle", [3.0, 3.0, 3.0])
    triangle2 = Polygon("Triangle", [3.0, 3.0, 3.0])

    assert triangle.get_name() == triangle2.get_name()
    assert triangle.get_sides() == triangle2.get_sides()

def test_polygon_inequality():
    triangle = Polygon("Triangle", [3.0, 3.0, 3.0])
    square = Polygon("Square", [4.0, 4.0, 4.0, 4.0])

    assert triangle.get_name() != square.get_name()
    assert triangle.get_sides() != square.get_sides()

def test_polygon_string():
    triangle = Polygon("Triangle", [3.0, 3.0, 3.0])
    string = f"{triangle.get_name()} with sides: {triangle.get_sides()}"
    assert string == triangle.__str__()

def test_polygon_calculate_circumference():
    triangle = Polygon("Triangle", [3, 3, 3])
    square = Polygon("Square", [4, 4, 4, 4])
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6.00001])

    assert triangle.calculate_circumference() == pytest.approx(9)
    assert square.calculate_circumference() == pytest.approx(16)
    assert hexagon.calculate_circumference() == pytest.approx(36)