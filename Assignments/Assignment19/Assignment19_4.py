"""
4. Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all such numbers which are even. 
Map function will calculate its square. Reduce will return addition of all that numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""

from functools import reduce

Even_number= lambda y: y%2==0
square = lambda z: z**2
sum = lambda a,b: a+b

def main():
    #num = int(input("Enter the number elements: "))
    values = [int(x) for x in input("Enter the numbers separated by space: ").split()]

    filtered_value = list(filter(Even_number,values))

    print("filtered value: ",filtered_value)

    maped_value = list(map(square,filtered_value))

    print("mapped value: ",maped_value)

    reduce_value = reduce(sum,maped_value)

    print("reduce value sum is: ",reduce_value)
    
if __name__ =="__main__":
    main()