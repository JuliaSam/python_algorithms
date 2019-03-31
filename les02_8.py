# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def func_count(digit, number):
    return_value = 0
    while number > 0:
        if number % 10 == digit:
            return_value += 1
        number = number // 10
    return return_value


numbers_quantity = int(input('Введите количество вводимых чисел: '))
digit = int(input('Введите символ, который хотите найти: '))
total_count = 0
for i in range(0, numbers_quantity):
    number = int(input('Введите число: '))
    total_count += func_count(digit, number)

print('Цифра встретилась в последователньности', total_count, 'раз')