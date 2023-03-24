# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень
def input_val():
    try:
        a = int(input("Введите номер месяца - "))
        return a
    except ValueError:
        print("Требуется ввести числовое значение от 1 до 12")
        input_val()


season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {'зима': [12, 1, 2],
               'Весна': [3, 4, 5],
               'Лето': [6, 7, 8],
               'осень': [9, 10, 11]}
number_mouth = input_val()
if number_mouth > 12:
    print('Вы ввели неверный номер месяца')
    input_val()
else:
    if number_mouth == 12:
        print(f'Результат через список - месяц №{number_mouth} - это {season_list[0]}')
    else:
        n = ((number_mouth // 3) + (1 if number_mouth % 4 >= 0 else 0)) - 1
        print(n)
        print(f'Результат через список - месяц №{number_mouth} - это {season_list[n]}')
print(list(season_dict.keys())
      [list(season_dict.values()).index(number_mouth)])
