
class Marvellous:
    #class variable 
    No1 = 11  #class variable same as static variable in c/c++
    No2 = 12  
    
    def __init__(self):
        #Instance variable 
        self.value1 = 21  
        self.value2 = 51

print(Marvellous.No1)
print(Marvellous.No2)

print("Object or Instance creation")

mobj1 = Marvellous()
mobj2 = Marvellous()
mobj3 = Marvellous()

print(mobj1.value1)
print(mobj2.value1)
print(mobj3.value2)
