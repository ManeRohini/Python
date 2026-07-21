import threading

def Display(no):  #def Display(*no)
    print(f"Inside display {no}:",threading.get_ident())


def main():
    print("Inside main:",threading.get_ident())

   # tobj=threading.Thread(target=Display) #error
    tobj=threading.Thread(target=Display,args=11) #error

    tobj.start()

if __name__=="__main__":
    main()
    
 #TypeError: __main__.Display() argument after * must be an iterable, not int