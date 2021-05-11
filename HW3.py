l = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]
a = {}
lis = []

for i in set(l):
    a[i] = i*2
    lis.append(i) 
print(a)
print('source:', lis)
print('total', sum(set(l)))
