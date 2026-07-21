                #List         #Tuple
#------------------------------------------
#ordered        yes         yes
#Indexed        yes         yes
#mutable        yes         no

def main():
    Data1=[10,20,30,40]   #List
    Data2=(10,20,30,40)       #Tuple

    print(Data1)
    print(Data2)
    print(Data1[0])
    print(Data2[0])

if __name__=="__main__":
    main()

#TypeError: 'tuple' object does not support item assignment
    
    