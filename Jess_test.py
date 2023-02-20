# Блок try-except заставляет Python выполнить код внутри него
try:
   # Ввод имени пользователя
   name = input('Введите имя:\n')
   # Ввод информации пользователем
   date_of_birth = int(input('Введите день рождения:'))
   month_of_birth = int(input('Введите месяц рождения:'))
   year_of_birth = int(input('Введите год рождения:'))
   mail = input('Введите адрес своей эл.почты:')
   # Вывод информации пользователю
   my_visit_card = (f'Приятно познакомиться {name.capitalize()}. Меня зовут Jess, мне 28 лет.Учусь в TeachMySkills.')
   print(my_visit_card)
   # Смаил
   print('\U0001f600')
   print("\N{grinning face}")
   print("\N{winking face}")
   print(date_of_birth/month_of_birth/year_of_birth/mail)
# Завершение блока try-except
except:
      print('Ошибка ввода даных')
# Дополнительный но не обезательный оператор
finally:
       print('Програма завершена')