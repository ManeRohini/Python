"""
3: Design a Python application that creates two threads named EvenList and OddList.

Both threads should accept a list of integers as input.

The EvenList thread should:

Extract all even elements from the list.

Calculate and display their sum.

The OddList thread should:

Extract all odd elements from the list.

Calculate and display their sum.

Threads should run concurrently.

"""
import threading

def EvenList(lst):
    even_list = []
    sum=0
    for i in lst:
        if(i%2 ==0):
            even_list.append(i)
            sum+=i
    print("even no in list is :",even_list)  
    print("even sum is: ",sum)  
    return even_list

def OddList(lst):
    odd_list = []
    sum=0
    for i in lst:
        if(i%2 !=0):
            odd_list.append(i)
            sum+=i
    print("odd no in list is:",odd_list)
    print("odd sum is: ",sum)  
    return odd_list

def main():
    values = [int(x) for x in input("Enter the numbers separated by space: ").split()]
    t1=threading.Thread(target=EvenList, args=(values,))
    t2=threading.Thread(target=OddList, args=(values,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=="__main__":
    main()