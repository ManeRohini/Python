#5. Write a program which accepts marks and displays grade.
"""""
Condition Example:

≥ 75 → Distinction

≥ 60 → First Class

≥ 50 → Second Class

< 50 → Fail
"""
def Grade(Marks):
    if(Marks >= 75):
        print("Distinction")
    elif(Marks>=60):
        print("First Class")
    elif(Marks>=50):
        print("Second Class")
    elif(Marks<50):
        print("Fail")

def main():
    No=int(input("Enter your marks to know your grade:"))
    Grade(No)

if __name__ =="__main__":
    main()