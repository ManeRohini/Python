                #List         #Tuple
#------------------------------------------
#ordered        yes         yes
#Indexed        yes         yes
#mutable        yes         no
#Heterogenous   yes         yes
#------------------------------------------

def main():
    Data1=[10,3.14,True, "pune"]   #List #heterogenous
    Data2=(10,3.14,True, "pune")       #Tuple

    print(Data1)
    print(Data2)
    print(Data1[0])
    print(Data2[0])

if __name__=="__main__":
    main()

#TypeError: 'tuple' object does not support item assignment
    
    