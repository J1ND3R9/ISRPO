class Dog:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def bark(self):
       print(f"{self.name} сказал(а): Гав!" )
    def output_info(self):
       print(f"Кличка: {self.name}, возраст: {self.age}")
       self.bark()
     
name = input('Имя песеля\n')
dog = Dog(name, 4)
dog.output_info()