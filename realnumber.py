import random

def real():
    num = 2
    n = 1
    out = 0
    while random.randint(1,num) == 1:
        n += 1

    m = 1
    for i in range(n):
        out += random.randint(0,num-1)*m
        m = num*m
    return out

ls = []
times = 0
for i in range(100000):
    ls.append(real())
    times += 1
    print((sum(ls)/times)//0.1/10,sorted(ls)[-1])
#print(sorted(ls))
