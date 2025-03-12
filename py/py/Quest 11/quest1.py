def greet_decorator(input_func):
    def output_func():
      print(f"Привет! Идёт запуск функции \"{input_func.__name__}\"")
      input_func()
    return output_func

@greet_decorator
def SayGex():
  print("gex")
  
SayGex()