def func(start, finish):
  while start < finish:
    yield start**2
    start += 1
    
a = func(1, int(input()) + 1)
for i in a:
  print(i)