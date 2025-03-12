def access_control_decorator(input_func):
  def wrapper(role, *args, **kwargs):
    if "админ" in role.lower():
      input_func(*args, **kwargs)
    else:
      print("Доступ запрещен. Только для администратора")
  return wrapper

@access_control_decorator
def delete_user(user_id):
  # типа подключились к SQL и нашли крутых пользователей
  user_list = list(range(0, 1000))
  if user_id not in user_list:
    print("Такого юзера нет!")
  else:
    user_list.pop(user_id)
    print(f"Пользователь {user_id} был удалён")
 
role = input("Ваша роль в системе: ")
delete_user(role, int(input()))