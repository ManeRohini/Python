#what si the difference between list and tuple in python? Mutability, memory,performance,use cases

                #List         #Tuple
#------------------------------------------
#ordered        yes         yes
#Indexed        yes         yes
#mutable        yes         no
#Heterogenous   yes         yes
#memory         high due    low due to fixed size and no over allocation allowed
#               to dynamic 
#               allocation       
#performance    slow        fast

#use cases    
# list: Dynamic data structures, frequent modifications, collections that grow/shrink
#tuple: Fixed collections, constants, data integrity, dictionary keys
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

   
    