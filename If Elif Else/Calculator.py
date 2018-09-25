print("""*****************************
Hesap Makinesi Programı

İşlemler;

1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
*****************************
""")

a= int(input("Birinci sayı:"))
b= int(input("İkinci sayı:"))

islem = input("işlemi giriniz:")

if islem == "1":
    print("{} ile {} in toplamı {} dir".format(a,b,a+b))
elif islem == "2":
    print("{} dan {} ı  çıkartırsak sonuç {} dir".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} ı  çarparsak sonuç {} dir".format(a, b, a*b))
elif islem == "4":
    print("{} ile {} ı  bölersek sonuç {} dir".format(a, b, a/b))
else:5

    print("Hatalı işlem yaptınız.")

