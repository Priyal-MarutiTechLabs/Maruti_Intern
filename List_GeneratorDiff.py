import sys
import time
#Output a List Containing Even Numbers
list = []

for i in range(1000000):
    if i%2 == 0:
        list.append(i)

start_time=time.time()
for var in list:
    pass
#print("List:",list)
print("Size required by list:",sys.getsizeof(list))
print("Time required by list:",time.time()-start_time)

#Output a Genrator containg even numbers
def Generator(n):
    for j in range(n):
        if j%2==0:
            yield j
x = Generator(1000000)
StartingTime=time.time()
for var in x:
    pass
print("Values In Generator:",x)
print("Memory required by generator:",sys.getsizeof(x))
print("Time required by generator:",time.time()-StartingTime)