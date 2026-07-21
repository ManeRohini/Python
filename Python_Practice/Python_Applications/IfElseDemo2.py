print("---------------------")
print("-----Ticket pricing software------")
print("---------------------")

print("Enter your Age: ")
Age = int(input())

if (Age <= 5):
    print("Entry free")
elif(Age > 5 and Age <=18):
    print("Ticket price :900")
elif(Age > 18 and Age<=40):
    print("Ticket price:1200")
else:
    print("Ticket price: 500")


    