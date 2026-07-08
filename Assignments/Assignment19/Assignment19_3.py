"""
3. Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user.
Filter should filter out all such numbers which greater than or equal to 70
and less than or equal to 90. Map function will increase each number by 10. 
Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
from functools import reduce

greated_than70_less90= lambda y: (y>=70 and y<=90)
increase_by10 = lambda z: z+10
product = lambda a,b: a*b

def main():
    #num = int(input("Enter the number elements: "))
    values = [int(x) for x in input("Enter the numbers separated by space: ").split()]

    filtered_value = list(filter(greated_than70_less90,values))

    print("filtered value: ",filtered_value)

    maped_value = list(map(increase_by10,filtered_value))

    print("mapped value: ",maped_value)

    reduce_value = reduce(product,maped_value)

    print("reduce value product is: ",reduce_value)
    
if __name__ =="__main__":
    main()