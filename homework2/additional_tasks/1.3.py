# Требуется вычислить факториал целого числа N.

N = int(input("Введите число: "))


def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)


print(factorial(N))
