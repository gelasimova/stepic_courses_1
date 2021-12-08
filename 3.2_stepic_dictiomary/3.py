d={}
k=[]
n=int(input())
for i in range(n):
    x = int(input())
    k.append(x)
for j in range(len(k)):
    if k[j] in d:
        print(d[k[j]])
    elif k[j] not in d:
        p = k[j]
        d[k[j]] = 5 * p
        print(d[k[j]])
print(d)