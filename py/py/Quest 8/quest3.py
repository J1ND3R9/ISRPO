import re

digits_only = r"^\d+$"

x = input()
digits_ismatch = re.match(digits_only, x)
if digits_ismatch is None:
  print("В строке не только числа!")
else:
  print("В строке только числа!")