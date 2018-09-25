a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if a > b and (a > c):
    print("En büyük sayı {}'dır.".format(a))
elif b > a and b > c:
    print("En büyük sayı {}'dır".format(b))
else:
    print("En büyük sayı {}'dır.".format(c))
