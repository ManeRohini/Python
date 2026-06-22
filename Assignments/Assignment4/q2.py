#tuple is immutable and fast
#list is mutable and slow

import sys, timeit

print(sys.getsizeof([1,2,3]))   # 88 bytes
print(sys.getsizeof((1,2,3)))   # 72 bytes

print(timeit.timeit("x=(1,2,3)", number=1000000))  # Faster #this is refered from internet
print(timeit.timeit("x=[1,2,3]", number=1000000))  # Slower
