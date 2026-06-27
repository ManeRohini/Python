#Can a Python function return multiple values? If yes, how does Python handle it internally?

def StudentDetails():
    return "rohini", 25, "python"

def main():
    name, age, course = StudentDetails()
    print(name, age, course)  

if __name__ =="__main__":
    main()

#yes python function can return mulyipe values
#internally python automatically packs the multiple return values in tuple form
#multiple return values can be store in different seperate variavles
