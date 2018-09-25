geo= input("Dörtgen mi? Yoksa Üçgen mi?")
if geo == "Dörtgen" or "Üçgen":
    print("Demek {} seçtin!!!".format(geo))
    if geo == "Dörtgen":
        kenar1=int(input("Dörtgen'in 1.kenarını giriniz:"))
        kenar2 = int(input("Dörtgen'in 2.kenarını giriniz:"))
        kenar3 = int(input("Dörtgen'in 3.kenarını giriniz:"))
        kenar4 = int(input("Dörtgen'in 4.kenarını giriniz:"))
        if kenar1==kenar2 and kenar1==kenar3 and kenar1==kenar4:
            print("Bu bir karedir.")
        elif (kenar1==kenar2 and kenar3==kenar4) or (kenar1==kenar3 and kenar2==kenar4) or (kenar1==kenar4 and kenar2==kenar3):
            print("Bu bir dikdörtgendir.")
        else:
            print("Bu sıradan bir dörtgendir")
    elif geo== "Üçgen":
        kenar1= int(input("Üçgen'in 1. kenarını giriniz:"))
        kenar2 = int(input("Üçgen'in 2. kenarını giriniz:"))
        kenar3 = int(input("Üçgen'in 3. kenarını giriniz:"))
        if kenar1==kenar2 and kenar1==kenar3:
            print("Eş kenar üçgendir.")
        elif kenar1==kenar2 or kenar2==kenar3 or kenar1==kenar3:
            print("İkiz kenar üçgendir.")
        else:
            print("Sıradan bir üçgendir.")
else:
    print("Sadece Dörtgen ve Üçgen girebilirsin!!!")