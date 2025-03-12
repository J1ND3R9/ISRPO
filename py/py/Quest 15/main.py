def calculate_sum(n: int):
  s = 0
  for i in range(1, n + 1):
    s += i
  return s

def only_three(li: list):
  only_three = []
  for word in li:
    if len(word) == 3:
      only_three.append(word)
  return only_three

def sort_by_len(li: list):
  li.sort(key=len)
  li.reverse()
  return li

def count_letters(li: list):
  di = {}
  for word in li:
    for letter in word.lower():
      if letter in di:
        di[letter] += 1
      else:
        di[letter] = 1
  return di

def factorial(n: int):
  mult = 1
  if n > 0:
    for i in range(1, n + 1):
      mult *= i
  elif n < 0:
    for i in range(-1, n - 1, -1):
      mult *= i
  return mult

if __name__ == '__main__':
  x = factorial(0)
  print(x)
  