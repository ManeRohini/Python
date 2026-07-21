no=11  #Global variable

def Display():
    a=21 #Local variable
    print("From Display: ",no)
    print("From dispaly value of a :", a) 
    
def Demo():
    print("From Demo: ",no)
    print("From demo value of a :", a) #error


Display()
Demo()


