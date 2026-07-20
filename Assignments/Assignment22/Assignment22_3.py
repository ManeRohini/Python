""""
3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.

Example  
10000
20000
30000
40000

Display total prime count for each number.

"""

import multiprocessing 
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Function to count primes up to N
def count_primes_up_to_n(N):
    count = 0
    for num in range(2, N + 1):
        if is_prime(num):
            count += 1
    return count

if __name__ == "__main__":
    numbers = [10000, 20000, 30000, 40000]

   
    pobj =multiprocessing.Pool()
    results = pobj.map(count_primes_up_to_n, numbers)

    print("Input:", numbers)
    print("Output:", results)

    for n, count in zip(numbers, results):
        print(f"Primes up to {n}: {count}")