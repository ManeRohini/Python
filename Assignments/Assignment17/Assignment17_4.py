#4. Write a program which accepts one number from the user and returns the addition of its factors.
#Input: 12  Output: 16  (1 + 2 + 3 + 4 + 6)

def FactAdd(No):
    total = 0
    for i in range(1, No):        
        if No % i == 0:          
            total += i             
    return total
    
def main():
    num=int(input("Enter the value: "))
    ret=FactAdd(num)
    print(f"FactAdd of {num} is: ",ret)
    
if __name__ =="__main__":
    main()