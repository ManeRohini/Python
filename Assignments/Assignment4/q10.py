

r1 = range(1,10)
print(r1)
print(list(r1))

r2 = range(1,10,2)
print(r2)
print(list(r2))

#range(1,10) indicates the scope of values starting from 1 to 9 (that is end-1), 
# when we rint this we get o/p as list of numbers from 1 to 9 [1, 2, 3, 4, 5, 6, 7, 8, 9]
#range(1,10,2) has 3 parameters start,end and last is jump(also as iterator or skip) it indicates the number starts from
#1 to 10 but by akiping the jump count
# ex : range(1,10,2) prints [1, 3, 5, 7, 9]
