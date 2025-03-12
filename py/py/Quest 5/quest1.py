documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def people(num):
  for i in documents:
    if i.get("number") == num:
      return i.get("name")
  return "Человек не найден!"

def shelf(num):
  for key, li in directories.items():
    if num in li:
      return key
  return "Полки с таким документом нет!"

def list():
  if len(documents) == 0:
    print("Нет документов")
  else:
    for doc in documents:
      for key, value in doc.items():
        print(value, end=" ")
      print("\n")

def add(num, type, name, shelf):
  if shelf not in directories:
    print(f"Полки с номером {shelf} не существует")
  else:
    doc_dict = {"type": type, "number": num, "name": name}
    documents.append(doc_dict)
    directories[shelf].append(num)
    print("Документ успешно добавлен!")

while True:
  fun = input("Введите команду\np - вывести человека с n номером документа\ns - вывести номер полки с n номером документа\nl - вывести список всех документов\na - добавить новый документ\n")
  if fun == "p":
    doc = input("Введите номер документа\n")
    print(people(doc))
  elif fun == "s":
    doc = input("Введите номер документа\n")
    print(shelf(doc))
  elif fun == "l":
    list()
  elif fun == "a":
    doc_num = input("Введите номер документа\n")
    doc_type = input("Введите тип документа\n")
    doc_name = input("Введите имя\n")
    shelf_num = input("Введите номер полки\n")
    add(doc_num, doc_type, doc_name, shelf_num)
  elif fun == "q":
    break
  print("\n")
  input()