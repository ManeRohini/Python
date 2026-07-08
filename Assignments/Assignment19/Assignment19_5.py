"""
5. Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all prime numbers. Map function will multiply each number by 2. 
Reduce will return Maximum number from that numbers. 
(You can also use normal functions instead of lambda functions).

Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

"""

from functools import reduce

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

multiply2 = lambda z: z*2
max = lambda a,b: a>b

def main():
    #num = int(input("Enter the number elements: "))
    values = [int(x) for x in input("Enter the numbers separated by space: ").split()]

    filtered_value = list(filter(is_prime,values))

    print("filtered value: ",filtered_value)

    maped_value = list(map(multiply2,filtered_value))

    print("mapped value: ",maped_value)

    reduce_value = reduce(max,maped_value)

    print("reduce value product is: ",reduce_value)
    
if __name__ =="__main__":
    main()