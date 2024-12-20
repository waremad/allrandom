import random

def two2ten(ls):
    out = 0
    n = 1
    for i in ls:
        out += i*n
        n += n
    return out

ls = []
result = []
times = 100000
many = 13
zoro = [0,0]

for i in range(2):
    ls.append(random.randint(0,1))

for i in range(times):
    ls.append(random.randint(0,1))

for i in range(many):
    result.append([0]*(2**(i+1)))


for i in range(times):
    for j in range(many):
        result[j][two2ten(ls[i:i+j+1])] += 1
        if two2ten(ls[i:i+j+1]) == 0 and j == many-1:
            zoro[0] += 1
        if two2ten(ls[i:i+j+1]) == 2**(many-1) and j == many-1:
            zoro[1] += 1
#print(ls)
for i in range(len(result)):
    print(i+1,max(result[i]),min(result[i]))
print(zoro)