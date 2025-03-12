import re

digits_only = r"\d+"

x = input()
digits = re.findall(digits_only, x)
digits_str = ""
for digit in digits:
    digits_str += str(digit)
print(digits_str)