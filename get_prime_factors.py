def is_prime(n):
    prime_stat = True
    for i in range(2, n):
        if i**2 <= n:
            if n%i == 0:
                prime_stat=False
    return prime_stat

def get_prime_factors(n):
    if is_prime(n):
        prime_factors = [n]
    else:
        for i in range(2, n):
            if is_prime(i) and n%i == 0:
                prime_factors = [i] + get_prime_factors(n//i)          
    return sorted(prime_factors)

print(get_prime_factors(630))