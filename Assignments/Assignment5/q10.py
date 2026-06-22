#what is dynamic typing in python?
#Dynamic typing in Python means that variables are not bound to a fixed type at declaration — 
# their type is determined at runtime based on the value assigned. This allows the same variable to 
# hold different types of data during program execution, 
#unlike statically typed languages where types are fixed at compile time.

#Runtime type inference: Python decides the type of a variable when you assign a value.

#Flexible reassignment: A variable can change type during execution.

#No explicit declarations: You don’t need to declare variable types before use.

x = 42
print(type(x))   # <class 'int'>

x = "Dynamic Typing"
print(type(x))   # <class 'str'>

