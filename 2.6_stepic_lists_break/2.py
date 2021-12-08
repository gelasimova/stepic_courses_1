a = []
n = int(input('Введите n = '))
for i in range(1, n + 1):
    a += [str(i)] * i
print(' '.join(a[0:n]))
