def primes(n):
    """returns prime numbers"""
    prime_nums = []
    for i in range(n-1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums


def is_prime(m):
    """returns if a number is a prime"""
    if (m <= 1):
        return False
    if (m <= 3):
        return True
    if (m % 2 == 0 or m % 3 == 0):
        return False
    i = 5
    while(i * i <= m):
        if (m % i == 0 or m % (i + 2) == 0):
            return False
        i = i + 6
    return True
