class Polygon:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def get_name(self):
        return self.name
    def get_sides(self):
        return self.sides
    
    def set_name(self, name):
        self.name = name
        
    def set_sides(self, sides):
        self.sides = sides

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name and self.sides == other.sides 

    def __ne__(self, other):
        return not self.__eq__(other) 
    
    def __str__(self):
        return f"{self.get_name()} with sides: {self.get_sides()}"
    
def main():
    triangle = Polygon("Triangle", [3, 3, 3])
    square = Polygon("Square", [4, 4, 4, 4])
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])

    print(triangle)
    print(square)
    print(hexagon)

if __name__ == "__main__":
    main()