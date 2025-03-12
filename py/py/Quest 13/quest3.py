class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    
class Car(Vehicle):
  def __init__(self, brand, model, num_doors):
    super().__init__(brand, model)
    self.num_doors = num_doors
    
  def honk(self):
    return "Бип бип!"
    
  def __str__(self):
    return f"Марка: {self.brand}\nМодель: {self.model}\nКоличество дверей: {self.num_doors}\n{self.honk()}"
  
brand = input("Марка автомобиля\n")
model = input("Модель автомобиля\n")
num = input("Кол-во дверей\n")
totoya = Car(brand, model, int(num))
print(totoya)