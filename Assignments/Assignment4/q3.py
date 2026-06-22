#predict o/p

lst = [10,20,30]
tpl=(10,20,30)

print("list:", lst)
print("tuple:", tpl)

lst[0]=100
#tpl[0]=100  #error because tuple is immutable, we can not change the value initally 
# assigened to any other value of any element

print("list:", lst[0])
print("tuple:", tpl[0])