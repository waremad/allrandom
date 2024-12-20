import random

n = str(random.random())
m = 1
print(m,n)
while not(n[:6] == "0.0000"):
    n = str(random.random())
    m += 1
    #print(m,n)
print(m-1,n)