

CheckEven = lambda No: (No % 2 ==0)

Increment =lambda No: (No+1)

Addition= lambda No1, No2:No1+No2

def filterX(Task,elemnts):
   result =[]

   for no in elemnts:
      ret = Task(no)
      if(ret==True):
            result.append(no)
            return result


def mapX(Task,elemnts):
    result =[]

    for no in elements:
        ret =Task(no)
        result.append(ret)
    return result

def reduceX(Task,elements):
    sum=0

    for no in elements:
        sum = Task(sum,no)
    return sum




def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

    FData=list(filterX(CheckEven, Data))  

    MData=list(mapX(Increment,Data))
  
    print("Data after lter ",MData)

    RData = reduceX(Addition, MData)

    print("Data after reduce:",RData)


if __name__ =="__main__":
    main()