print("""
****************************************
Boy ve Kilo Endeksi Hesaplama Programı
****************************************
""")
boy= float(input("Boyunuzu Giriniz(metre):"))
kilo= float (input("Kilonuzu giriniz(kg):"))
endeks= kilo/(boy*boy)
if endeks <= 18.5:
    print("Zayıf")
elif endeks <= 25:
    print("Normal")
elif endeks <= 30:
    print("Fazla kilolu")
else:
    print("Obez")
print("Vücut kitle endeksiniz {}'dir.".format(endeks))
