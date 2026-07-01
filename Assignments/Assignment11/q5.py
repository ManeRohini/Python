#5. Write a program which accepts one number and checks whether it is palindrome or not.
#Input: 121
#Output: Palindrome

def IsPalindrome(No):
    rev=0
    while No>0:
        digit=No%10
        rev= rev*10+digit
        No=No//10
    return rev
    
def main():
    num=int(input("Enter the number: "))
    Result=IsPalindrome(num)

    if(num==Result):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")

if __name__=="__main__":
    main()