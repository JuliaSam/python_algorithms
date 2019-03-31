# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

number = int(input('Введите n-количество последовательных чисел: '))


def check_hypothesis_for(n):
    honest_sum_n = 0
    for i in range(1, n + 1):
        honest_sum_n += i

    formula_result = n * (n + 1) / 2
    return formula_result == honest_sum_n

is_equation_correct = True
for n in range(1, number + 1):
    if check_hypothesis_for(n):
        print("Равенство выполняется для", n)
    else:
        print("Равенство НЕ выполняется для", n)
        is_equation_correct = False

print()
if is_equation_correct:
    print("Равенство истинно!")
else:
    print("Равенство не истинно!")
