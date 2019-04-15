# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import timeit

# T = трудоёмкость заключается в выполнении итераций цикла
# T_итерации = сложение (O(1)) + деление (O(1)) + сложение (O(1)) = O(1)
# T = n * O(1) = O(n)
def first_method(n):
    new_number = 1
    i = 0
    value = 0
    while i < n:
        value += new_number
        new_number = new_number / (-2)
        i += 1
    return value


# T = трудоёмкость возведения в степень + вычитание + деление
# T = O(ln n) + O(1) + O(1) = O(ln n)
def second_method(n):
    return (1 - ((-0.5) ** n)) / 1.5


n = input('Введите количество элементов: ')
tests_number = 1000
first_time = timeit.timeit('first_method(' + n + ')', setup="from __main__ import first_method", number=tests_number)
second_time = timeit.timeit('second_method(' + n + ')', setup="from __main__ import second_method", number=tests_number)

print("Среднее время работы первого алгоритма: " + str(first_time / tests_number))
print("Среднее время работы второго алгоритма: " + str(second_time / tests_number))

if first_time < second_time:
    print("Первый алгоритм эффективнее в " + str(second_time / first_time) + " раз")
else:
    print("Второй алгоритм эффективнее в " + str(first_time / second_time) + " раз")
