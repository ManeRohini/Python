from abc import ABC, abstractmethod #ABC is abstarct base class

class Base(ABC): #it is mandatory to inherite ABC class to write abstract menthod in any class
    @abstractmethod
    def addition(self,no1,no2):
        pass


class Derived(Base):
    def addition(self,no1,no2):
        return no1+no2

dobj = Derived()  
ret = dobj.addition(10,11)
                  
print("Addition is: ",ret)