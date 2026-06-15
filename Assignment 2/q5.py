a=10
b=10

print(id(a)==id(b))

print(id(a))
print(id(b))
print(type(a))
print(type(b))

#Explain
#a and b have same value assigned to it so single memory gets allocated to these variables but reference count gets 
#incresed by 1 here , so the id for a and b are same that why print statement at line number 4 gives output as TRUE