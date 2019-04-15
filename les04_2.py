# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

#Не используя алгоритм "Решето Эратосфена"
#В связи с использованием цикла, сложность алгоритма очень сильно увеличивается. Скорее всего, сложность экспоненциальная
import timeit

def simple_primes_numbers_searching_algorithm(n):
    prime_numbers = []
    candidate_to_be_prime = 1
    while len(prime_numbers) < n:
        candidate_to_be_prime += 1
        is_prime = True
        for possible_divider in range(2, int(candidate_to_be_prime ** 0.5) + 1):
            if candidate_to_be_prime % possible_divider == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(candidate_to_be_prime)
    return prime_numbers


for n in range(5, 50, 2):
    print(n, timeit.timeit('simple_primes_numbers_searching_algorithm(' + str(n) + ')', setup="from __main__ import simple_primes_numbers_searching_algorithm", number=50))