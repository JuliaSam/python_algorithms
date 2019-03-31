#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
new_number = 1
i = 0
sum = 0

while i < n:
    sum += new_number
    new_number = new_number/(-2)
    i += 1
print(sum)
