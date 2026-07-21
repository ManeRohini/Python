from abc import ABC, abstractmethod #ABC is abstarct base class

class Base(ABC): #it is mandatory to inherite ABC class to write abstract menthod in any class
    @abstractmethod
    def addition(self,no1,no2):
        pass


class Derived(Base):
    pass

dobj = Derived()  #error