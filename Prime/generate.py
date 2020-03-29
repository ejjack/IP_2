#generate.py
#!/usr/bin/python

"""A Python program generating a list of prime numbers and output them into a csv file

"""

from primepackage import *

def main():
    """Generate 100 prime numbers and output it into output.csv file

    """
    primes = getNPrime(100)

    write_primes(primes, 'output.csv')

    prime_list = read_primes('output.csv')

    print(prime_list)

if __name__ == '__main__':
    try:
       main()
    except IOError as argument:
        print("Error: no file found", argument)
