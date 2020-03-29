#primeio.py
"""Python program that contains functions that deal with csv files

"""

import csv
from csv import writer
def write_primes(prime_list, file_name):
    """Read list of prime numbers and adds list to csv file

    Args:
        prime_list (list): list of prime numbers.
        file_name (str): input file name.

    Returns:
        file: A csv file that contains a list of prime numbers

    Example:
        >>>1 = write_primes('prime_list, output.csv);

    """
    with open(file_name, 'w') as write_prime:
        csv_write = writer(write_prime)
        for i in range(len(prime_list)):
            csv_write.writerow([prime_list[i]])

def read_primes(file_name):
    """Read csv file and takes prime numbers and puts them in a list

     Args:
        file_name (str): input file name.

    Returns:
        list: a list of primes in a csv file

    Example:
        >>>1 = read_primes('output.csv');

    """
    prime_list = []
    with open(file_name) as csv_prime:
        csv_reader = csv.reader(csv_prime)
        for row in csv_reader:
            for i in range(len(row)):
                num = row[i]
                if int(num) > 1:
                    for j in range(2, int(num)):
                        if int(num) % j == 0:
                            break
                        else:
                            prime_list.append(int(num))
        return prime_list
