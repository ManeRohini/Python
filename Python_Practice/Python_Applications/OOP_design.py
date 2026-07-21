
class Arithmatic:

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B


    def add(self): #instance method
        Ans = self.no1 + self.no2
        return Ans

    def substract(self):
        Ans = self.no1 - self.no2
        return Ans
    


print("Enter 1st no: ")
val1 =int(input())

print("Enter 2nd no: ")
val2 =int(input())

Aobj = Arithmatic(val1,val2)

Ret =Aobj.add()       
print("Addition is: ",Ret)  

Ret2 =Aobj.substract()         #
print("Substraction is: ",Ret2)






