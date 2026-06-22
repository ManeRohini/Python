
def fun():
    x=10
    print(x)

fun()
print(x)  # error


#PS C:\Users\Admin\Desktop\PYAssignments\Assignment3> python q3.py
#10
#Traceback (most recent call last):
#  File "C:\Users\Admin\Desktop\PYAssignments\Assignment3\q3.py", line 7, in <module>
 #   print(x)
 #         ^
#NameError: name 'x' is not defined


#the scope of variable x is inside function fun() only as x is a local varable declared inside fun()
# if we try to print it externally(outside the function call/scope) ,it gives name error