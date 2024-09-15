# Исходные данные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Решение
primes = []
not_primes = []
is_prime = True

for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
        if j > i:
            break
        elif numbers[i] % numbers[j] == 0 and i > j:
            is_prime = False
            # print(f'{numbers[i]} / {numbers[j]} = {numbers[i] / numbers[j]}', is_prime)
            not_primes.append(numbers[i])
            break
        else:
            is_prime = True
            # print(f'{numbers[i]} / {numbers[j]} = {numbers[i] / numbers[j]}', is_prime)
            primes.append(numbers[i])


# Вывод результата
print('Primes: ', list(set(primes)))
print('Not Primes: ', not_primes)
print()


# ПОПЫТКА №2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Решение
primes = []
not_primes = []
is_prime = True

for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
        if j > i:
            break
        elif numbers[i] % numbers[j] == 0 and i > j:
            is_prime = False
            not_primes.append(numbers[i])
            break

primes = (numbers)
for i in range(len(not_primes)):
    primes.remove(not_primes[i])
primes.remove(1)

# Вывод результата
print('Primes: ', primes)
print('Not Primes: ', not_primes)