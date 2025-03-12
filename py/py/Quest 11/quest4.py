def logs(input_func):
  def output_func(*args, **kwargs):
    print(f"Вызов функции: {input_func.__name__}")
    print(f"Аргументы функции: args={args}, kwargs={kwargs}")
    return_result = input_func(*args, **kwargs)
    print(f"Функция {input_func.__name__} вернула результат {return_result}")
  return output_func

@logs
def very_difficult_func(x, y, total_thread):
  return "Hello World!"

very_difficult_func(10, 5, total_thread=1835.311)
  