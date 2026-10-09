import sys
if len(sys.argv) < 2:
    print("Использование: ./bases.py <число>")
    sys.exit(1)
num = int(sys.argv[1])
a = bin(num)
b = oct(num)
c = hex(num)
print(num, "->", a, b, c)
