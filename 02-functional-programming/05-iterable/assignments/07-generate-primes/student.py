def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes():
    current = 2
    while True:
        if is_prime(current):
            yield current
        current += 1