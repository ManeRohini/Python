import sys

print(sys.getsizeof(10))        # int → ~28 bytes
print(sys.getsizeof("hello"))   # str → ~46 bytes
print(sys.getsizeof([1]))   # list → ~64 bytes
print(sys.getsizeof([1,2,3]))   # list → ~88 bytes

#getsizeof() is a function from Python’s sys module.
#It returns the memory size (in bytes) that a Python object occupies.