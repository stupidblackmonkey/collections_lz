a = 0
b = 1
i = 2
u = 0
n = int(input("Введите длинну ряда"))
c = [a,b]

while i < n:
    a, b = b, a + b
    c.append(b)
    i += 1
print (c)
    
for i in range(n):
    if c[i] % 2 == 0:
        c[i] = c[i] * 2
    else:
        c[i] = c[i] ** 2
print (c)

qwe = sum(c) / n
for i in range(n):
    if i > qwe:
        u += 1
    else:
        u +=0
print (u)
    

c_max = max(c)
c_min = min(c)
print ('min = ', c_min)
print ('max = ', c_max)
c_length = len(c)
print ('dlinna = ', c_length)