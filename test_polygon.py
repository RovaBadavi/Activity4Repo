from polygon import Polygon


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

