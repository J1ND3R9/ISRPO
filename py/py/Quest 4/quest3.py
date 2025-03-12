queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

words = {}

for query in queries:
  space = len(query.split())
  if space in words:
    words[space] += 1
  else:
    words[space] = 1

precentages = {}
for key, quantity in words.items():
  precentage = round(quantity * 100 / len(queries), 2)
  precentages[key] = str(precentage) + "%"

print(precentages)