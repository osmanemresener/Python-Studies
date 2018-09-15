a= float(input("Aracın yakıt harcamasını lt/100km olarak olarak giriniz."))
b= float(input("Kaç km yol kat edildi?"))
c= float(input("Motorin fiyatı ne kadar?"))
print("{} km yol katederek toplamda {} TL'lik yakıt harcaması yaptınız.".format(b,a*b/100*c))
