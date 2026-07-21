
class Arithmatic:
    def add(no1,no2):
        Ans = no1+no2
        return Ans

    def substract(no1,no2):
        Ans = no1-no2
        return Ans
    
Aobj = Arithmatic()

print("Enter 1st no: ")
val1 =int(input())

print("Enter 2nd no: ")
val2 =int(input())

Ret =Aobj.add(val1, val2)       #Issue /error
print("Addition is: ",Ret)  

Ret2 =Aobj.substract(val1,val2)         #Issue /error
print("Substraction is: ",Ret2)






