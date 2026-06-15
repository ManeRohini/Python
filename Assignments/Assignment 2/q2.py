a=10
b=10

print(id(a))
print(id(b))
print(type(a))
print(type(b))

#Explain using id()
#Here for a and b both variables on line 1 and 2 are int type. 
#when we check or print it's id then we get the same id for both a and b that is for example 140734571398552
#This is because when a =10, it gets memory in heap and value in that memory is 10
# when b=10, as value is same as a the reference count for a variable gets incremented by 1
#so that id for a and b variable are same
#int is immutable, it may share the memory
a=[10]
b=[10]

print(id(a))
print(id(b))
print(type(a))
print(type(b))

#Explain using id()
#Here for a and b both variables on line 15 and 16 are list type. 
#when we check or print it's id then we get the different id for both a and b.
#  example id for a is 2562885924672
# id for b is 2562885808064
#here as it is a list data type, a and b gets different memory allocated in heap
#list is mutable, memory gets allocated seperatly to each element
