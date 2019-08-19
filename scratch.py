from heapdict import heapdict

a = heapdict()

b = [1,3,5,2,4,9,8,6,7]
for item in b:
    a[item] = item

print(1 in a)

print(a)
print(list(a))
print(a.popitem())
print(a.popitem())
print(a.popitem())

while a:
    print(a.popitem())

print('Success')
