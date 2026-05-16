import random
kurban_listesi=[]
kurtulanlar=[]
infaz_edilen=''
for i in range(6):
    sec=input('secilecek mahkumun ismini oku:')
    print("{} sahneye çıkarıldı".format(sec))
    kurban_listesi.append(sec) #İsimleri tutan sec, kurban listesine sec'i ekliyoruz. çağırınca girdiğimiz isimler gelir

silah_patladı=0
sayac=1 #çünkü sayac indisi tutmuyor
r=random.randint(1,6)
print("ss subayı silahını çıkardı ve rus ruleti için hazırladı.")
while silah_patladı==False:
    if sayac==r:
        print("boom {}.kişi öldü".format(sayac))
        silah_patladı=True
        infaz_edilen=kurban_listesi[sayac-1]
    else:
        print("Tıkkkk  {}.kişi kurtuldu sıra {}.kişide".format(sayac , sayac+1))
        kurtulanlar.append(kurban_listesi[sayac-1])
        sayac = sayac + 1
