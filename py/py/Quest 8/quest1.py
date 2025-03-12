import re

email_regex = r"^[A-z\d]+@[A-z]+\.[A-z]{2,3}$"

email = input("Введите почту\n")
email_correct = re.match(email_regex, email)
if email_correct is None:
  print("Неверная почта")
else:
  print("Отлично!")
  