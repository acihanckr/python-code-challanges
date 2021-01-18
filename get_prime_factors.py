def get_prime_factors(n):
    prime_factors = list()
    for i in range(2, n+1):
        if  n%i == 0 and i != n:
            prime_factors = [i] + get_prime_factors(n//i)
            return sorted(prime_factors) 
        elif i == n:
            return [i]         

print(get_prime_factors(630))