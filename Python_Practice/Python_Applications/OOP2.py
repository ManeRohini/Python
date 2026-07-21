
class Demo:
    #class variables
    value1 = 10
    value2 = 20

    def __init__(self):
        self.no1 = 11
        self.no2 = 21

    #Instance method
    def fun(self):
        print("Inside instance method named as fun")
        print(self.no1)
        print(self.no2)

        print(Demo.value1)
        print(Demo.value2)


#object creation
dobj = Demo()
dobj.fun()


