class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height
  
  def perimeter(self):
    return 2 * (self.width + self.height)
  
  def __str__(self):
    return f"Прямоугольник с шириной {self.width} и высотой {self.height}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}"
  
x = input("Ширина\n")  
y = input("Высота\n")  
rect = Rectangle(int(x), int(y))
print(rect)