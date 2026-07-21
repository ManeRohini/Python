CheckEven=lambda No:(No %2 ==0)

Increment= lambda No: No+1

def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

    MData=list(map(Increment,Data))
    
    print("Data after filter ",MData)

if __name__ =="__main__":
    main()