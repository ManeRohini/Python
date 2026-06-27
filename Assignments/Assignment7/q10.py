#Explain the difference between:  
#• return x  
#• return x, y  
#• return

#return statements controls what value a function sends back to the caller 

#return x : returns the single value

def add(a,b):
    c=a+b
    print("vale of c is: ",c)
    return c

add(1,2)

#return x,y: returns multiple values form a function call
#it returns the tuple
def calc(a,b):
    c=a+b
    d=a-b
    print("vale of c is: ",c)
    print("vale of c is: ",d)
    return c,d

result=calc(20,5)
print("result is:", result)

#return: this is empty return, it returns nothing
#return value is None

def only_print(name):
    print("name is: ", name)
    return

output=only_print("rohini")
print("output value is: ", output)