#predict o/p #why is this allowed?

ba=bytearray([65,66,67])
ba[0] = 97
print(ba)
#here the int data passed to bytearray gets convereted to binary interbally
#and for disply it gives the ASCII value of that binary value accordingly

