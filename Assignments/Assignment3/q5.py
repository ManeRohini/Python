#waht is difference between below, expplain with example
#print is a built in function, default provieded by the python language. It is useed to dispaly value or message on the output device

print("Marvellous: Python with AIML and data science")

#return is  a keyword in a python , used to tell that if any functions gives output in the form of any value.
def demo():
    a=10
    b=20
    sum=a+b
    return sum

def main():
    
    Value = demo()
    print("value of sum is: ",Value)

if __name__ =="__main__":
    main()