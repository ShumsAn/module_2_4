numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for n in numbers:
    if n != 1:
        is_primes = True
        for i in range(2, n):
            if n % i == 0:
                is_primes = False
                break
        if is_primes == False:
            not_primes.append(n)
        if is_primes == True:
            primes.append(n)

print('primes:', primes)
print('not_primes:', not_primes)
