import re

num_regex = r"^\+7\d{3}-\d{3}-\d{2}-\d{2}$"

number = input("Введите номер\n")
is_correct = re.match(num_regex, number)
if is_correct is None:
  print("Неверный номер телефона!")
else:
  print("Отлично!")