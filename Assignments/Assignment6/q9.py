#What is a return value in a function?


# If functions gives output in the form of any variable after performing logic return inside function body is called as return value of a function.
#In python we can return multiple variables
#multiple return variable can be assigned by other mutliple variables, or it can return value in terms of tuple.
#Return is used to end a function and send a value back to the caller. 

def fun():
    print("Welcome to Marvellous")
    a=5+2
    print("Value of a is: ", a )
    return a
    
fun()