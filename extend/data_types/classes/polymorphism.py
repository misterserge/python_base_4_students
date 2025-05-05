class Shape:
    def __init__(self, color: str):
        self.color = color
        
    def get_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def get_area(self) -> float:
        return 3.14 * self.radius ** 2
    
    def __str__(self) -> str:
        return f"Circle(color={self.color}, radius={self.radius})"
    
class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height
    
    def __str__(self) -> str:
        return f"Rectangle(color={self.color}, width={self.width}, height={self.height})"
        
    
calc_circle_area = Circle("red", 10)

print(calc_circle_area.get_area())

shapes = [Circle("red", 10), Rectangle("blue", 10, 20)]

for shape in shapes:
    print(shape.get_area())


    
