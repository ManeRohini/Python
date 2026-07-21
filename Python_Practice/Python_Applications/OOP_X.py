
class Arithmatic:
    def add(self,no1,no2):
        Ans = no1+no2
        return Ans

    def substract(self,no1,no2):
        Ans = no1-no2
        return Ans
    
Aobj = Arithmatic()

print("Enter 1st no: ")
val1 =int(input())

print("Enter 2nd no: ")
val2 =int(input())

Ret =Aobj.add(val1, val2)       
print("Addition is: ",Ret)  

Ret2 =Aobj.substract(val1,val2)         #
print("Substraction is: ",Ret2)






