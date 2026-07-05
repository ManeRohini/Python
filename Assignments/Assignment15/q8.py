#8.Write a lambda function using filter() which accepts a list of numbers and 
# returns a list of numbers divisible by both 3 and 5.

filter_divisible = lambda n: n%3 ==0 and n%5==0 

def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

    print("Data before  ",Data)

    FData=list(filter(filter_divisible,Data))
    
    print("Data after  ",FData)

if __name__ =="__main__":
    main()