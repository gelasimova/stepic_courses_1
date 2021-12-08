#Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит
# все позиции, на которых встречается число xx в переданном списке lstlst.
a = [int(i) for i in input().split()]
b = int(input())
t = []
if b in a:
    for i in range(len(a)):
        if a[i] == b:
            t.append(i)
    for j in range(len(t)):
        print(t[j], end=' ')
else:
    print('Отсутствует')