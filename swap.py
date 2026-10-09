a = int(input())
b = int(input())
print(a, b)
c = a
a = b
b = c
print(a, b)
#2 способ
a = int(input())
b = int(input())
print(a, b)
a, b = b, a
print(a, b)
