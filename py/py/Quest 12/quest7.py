def fib(end):
    first = 0
    second = 1
    for i in range(end):
      result = first + second
      yield first
      first = second
      second = result
        
for i in fib(int(input())):
  print(i)  