#1. Write a program which accepts one character and checks whether it is vowel or consonant.  
#Input: a
#Output: Vowel

def IsVowel(ch):
    set={"a","e","i","o","u"}
    if ch.lower() in set:
        print("The character  is a vowel")
    else:
        print("The character  is consonant")

def main():
    char=input("Enter a character  to check it is vowel or consonant: ")
    if(len(char)==1) and char.isalpha():
        IsVowel(char)
    else:
        print("Enter the single character only")

if __name__ =="__main__":
    main()
