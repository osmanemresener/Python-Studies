vize1= int(input("1. vize notunuz:"))
vize2= int(input("2. vize notunuz:"))
final= int(input("Final notunuz:"))

ortalama= vize1*0.3+ vize2*0.3+final*0.4

if ortalama >90:
    print("AA")
elif ortalama >85:
    print("BA")
elif ortalama >80:
    print("BB")
else:
    print("DD kaldın.")

