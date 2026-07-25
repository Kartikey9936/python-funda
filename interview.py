#swapping of two numbers 
a = 10 #using tuple unpacking
b =20
a, b = b, a
print(a,b)

temp = a
a = b 
b = temp
print(a,b)

a = a +b 
b = a -b
a = a -b

a = a*b
b= a/b
a = a/b

a = a ^ b
b = a ^ b
a = a ^ b


