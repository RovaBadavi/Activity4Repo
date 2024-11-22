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
    
    