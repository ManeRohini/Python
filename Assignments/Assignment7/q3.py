#Explain the use of the global keyword. When should it be used?


#global variable
#The variable which is defined outside of scope or block  of any function is called as global variable 
#Delcared outside functions
#can be acceesed inside and outside
#same names may leads to logical error
#shared values accross multiple parts

Global_var =10


def add(a1,b1):
    sum1=a1+b1
    print("value of addition is:", sum1)
    Global_var =sum1
    print("updated value of global variable is:", sum1)
    return sum1

add(Global_var,5)

if(Global_var>5):
    print("The global varibale is greater than 5: that is", Global_var)

