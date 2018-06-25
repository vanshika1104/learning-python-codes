a=10
b=4
a=bin(a)
b=bin(b)
print(type(a))
c=bin(int(a,base=2)+int(b,base=2))
print(c)
print(int(c,base=2))

