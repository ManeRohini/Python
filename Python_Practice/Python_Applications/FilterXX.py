CheckEven = lambda No: (No%2==0)

def Increment(No) :
    pass

def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

   # FData=filter(Data, CheckEven)  #error

    FData=list(filter(CheckEven, Data))  #error solution is typecasting
    
    #iterable <-- filter(iterable,function)
    #iterable <-- filter(iterable,function)
    #single value <-- filter(iterable,function)
    #output
    print("Data after filter ",FData)

if __name__ =="__main__":
    main()