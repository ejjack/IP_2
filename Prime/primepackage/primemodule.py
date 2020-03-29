#primemodule.py

"""Python program that contains functions to determine whether a number is prime

"""

def isPrime(num):
    """Reads number and tells whether it is prime or not

    Args:
        num (int): input integer.

    Returns:
        boolean: returns true or false if the number is prime or not

    Example:
        >>>1 = isprime(num);
        
    """
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True
    else:
        return False

def getNPrime(num):
    """Lists prime numbers up to a given point

    Args:
        num (int): input integer.

    Returns:
        list: a list of prime numbers up to num

    Example:
        >>>1 = getNprime(num);

    """
    prime_list = []
    for i in range(0, num):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    prime_list.append(i)
    return prime_list
