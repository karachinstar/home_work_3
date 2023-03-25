# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

def my_func_no_sort(num_1, num_2, num_3):
    if num_1 >= num_2 and num_2 >= num_3 or num_2 >= num_1 and num_1 >= num_3:
        sum_num = num_1 + num_2
        print(f'Сумма двух минимальных значений равна {sum_num}')
    elif num_2 >= num_3 and num_3 >= num_1 or num_3 >= num_2 and num_2 >= num_1:
        sum_num = num_2 + num_3
        print(f'Сумма двух минимальных значений равна {sum_num}')
    elif num_1 >= num_3 and num_3 >= num_2 or num_3 >= num_1 and num_1 >= num_2:
        sum_num = num_1 + num_3
        print(f'Сумма двух минимальных значений равна {sum_num}')


def my_func_sort(num_1, num_2, num_3):
    a = [num_1, num_2, num_3]
    a.sort()
    sum_num = a[1] + a[2]
    print(f'Сумма двух минимальных значений равна {sum_num}')


my_func_no_sort(int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)

my_func_sort(int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)