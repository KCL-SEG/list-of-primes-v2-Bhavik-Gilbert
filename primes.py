"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2

    if number_of_primes <= 0:
        raise ValueError

    while(len(list) < number_of_primes):
        is_prime = True

        for prime in list:
            if(number % prime == 0):
                is_prime = False
                break

        if(is_prime):
            list.append(number)
        
        number += 1

    return list