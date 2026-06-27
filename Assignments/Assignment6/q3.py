#What is the importance of indentation inside a function body? What happens if indentation is incorrect?

#In c/c++ {} is used to represent the block, but in python : and indentation is used to write a  block 
# : indicates the start of block
# if correctindentation is not given the it may give error
# in function, conditional statments , loop or inside class ,user need to miantain correct indentation to avoid logical errors

def indentation():
    print("I am indentation function")

print("I am outside the indentation function")


def main():
    indentation()

if __name__ =="__main__":
main()  # IndentationError

"""
PS C:\Users\Admin\Desktop\PYAssignments\Assignment6> python q3.py
  File "C:\Users\Admin\Desktop\PYAssignments\Assignment6\q3.py", line 18
    main()
    ^^^^
IndentationError: expected an indented block after 'if' statement on line 17

"""