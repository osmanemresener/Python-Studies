a=1
b=1
fibonacci= [a,b]
fibonacci.append(a)
for i in range(20):
    a,b =b,a+b
    fibonacci.append(b)
print(fibonacci)