#predict o/p # expalin change / no change in id

s="python"
print(id(s))
print(s)
s=s+"3"
print(id(s))
print(s)

#here s=s+3 is the performs the uppend operation which added s=python+3 that becomes python3
#here number of charactors in the string changes that means the size of string changes 
# that why memory allocation fr the newly updated string changes and that's why 
# we get different id's before and after s=s+3 operation

