print("""
************************
Kullanıcı Girişi
************************
""")

sys_kullanici_adi = "emre"
sys_parola = "1,2,3"

kullanici_adi = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Parola Hatalı....")
elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Kullanıcı Adı Hatalı....")
elif (kullanici_adi !=sys_kullanici_adi and parola != sys_parola):
    print("Kullanıcı Adı ve Parola Hatalı....")
else:
    print("Sisteme başarıyla giriş yapıldı....")




