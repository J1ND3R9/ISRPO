import time

def timer_decorator(input_func):
  def output_func():
    now = time.time()
    input_func()
    delta_time = time.time() - now
    print(f'Время выполнения функции "{input_func.__name__}": {round(delta_time, 3)}с.')
  return output_func

@timer_decorator
def small_func():
  print("Hello World!")

@timer_decorator
def big_func():
  x = 99999999
  while x > 0:
    x -= 1
  print(x)
    
small_func()
print()
big_func()