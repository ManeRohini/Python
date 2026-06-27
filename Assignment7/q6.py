#Can a function return another function? Explain conceptually.

#Yes,function can return another function


def fun1(msg):
    def fun2():
        print("hello world",msg)
    return fun2



output=fun1("marvellous")

output()