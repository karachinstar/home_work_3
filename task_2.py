# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
#
# Process finished with exit code 0
#
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
#
# Process finished with exit code 0
def input_val():
    try:
        a = int(input())
        return a
    except ValueError:
        print("Требуется ввести числовые значения")
        input_val()
def zero_div():
    try:
        division_numbers = number_1 / number_2
        return division_numbers
    except ZeroDivisionError:
        print("Нельзя делить на 0")

print("Введите первое число - ")
number_1 = input_val()
print("Введите второе число - ")
number_2 = input_val()
div_num = zero_div()
print(f'{number_1} / {number_2} = {div_num}')