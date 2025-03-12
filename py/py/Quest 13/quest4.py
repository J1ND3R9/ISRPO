class Thermometer:
  def __init__(self, temperature):
    self.__temperature = temperature
    
  @property
  def temperature(self):
    return self.__temperature
  
  @temperature.setter
  def temperature(self, temperature):
    if -273.15 < temperature:
      self.__temperature = temperature
    else:
      print("Температура ниже абсолютного нуля невозможна.")
  def __str__(self):
    return f"Температура: {self.__temperature}"
  
therm = Thermometer(float(36.6))
print(therm)
therm.temperature = float(input("Введите температуру: "))
print(therm)
therm.temperature = float(input("Введите температуру: "))
print(therm)