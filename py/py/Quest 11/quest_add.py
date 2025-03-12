import time

def logs(input_func):
  def output_func(*args, **kwargs):
    print(f"Вызов функции: {input_func.__name__}")
    print(f"Аргументы функции: args={args}, kwargs={kwargs}")
    return_result = input_func(*args, **kwargs)
    print(f"Функция {input_func.__name__} вернула результат {return_result}")
  return output_func

def greet_decorator(input_func):
    def output_func(*args, **kwargs):
      print(f"Привет! Идёт запуск функции \"{input_func.__name__}\"")
      input_func(*args, **kwargs)
    return output_func
 
def access_control_decorator(input_func):
  def wrapper(role, *args, **kwargs):
    if "админ" in role.lower():
      input_func(*args, **kwargs)
    else:
      print("Доступ запрещен. Только для администратора")
  return wrapper

def timer_decorator(input_func):
  def output_func(*args, **kwargs):
    now = time.time()
    input_func(*args, **kwargs)
    delta_time = time.time() - now
    print(f'Время выполнения функции "{input_func.__name__}": {round(delta_time, 3)}с.')
  return output_func

@access_control_decorator
@greet_decorator
@timer_decorator
@logs
def random_func(x):
  i = 2000000
  while i != 0:
    i -= x
  return x

random_func("админ", 1)