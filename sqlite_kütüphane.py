from kütüphane import *

print("""
--------------------------------
Kütüphaneye Hoşgeldiniz         

işlemler:

1.Kitap ekle

2.Kitap sil

3.Kitapları göster

4.Kitap sorgula

Çıkmak için 'q' ya basın.
--------------------------------
""")

kütüphane = Kütüphane()

while True:
    işlem = input("yapacağınız işlemi seçiniz:")

    if işlem == "q":
        print("kütüphane kapatılıyor")
        break

    elif işlem == "1":
        isim = input("Kitap ismi:")
        yazar = input("yazar:")
        yayınevi = input("yayınevi:")
        sayfa_sayısı = int(input("sayfa sayısı:"))


        yeni_kitap = Kitap(isim,yazar,yayınevi,sayfa_sayısı)
        print("--Kitap ekleniyor--")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("--Kitap eklendi--")



    elif işlem == "2":
        print("--Silmek istediğiniz kitabın adını yazınız--")
        isim = input("Kitap ismi:")

        cevap = input("Silmek istediğine emin misin!! (E/H):")

        if cevap == "E" or cevap == "e" or cevap == "evet":
            kütüphane.kitap_sil(isim)
            print("--Kitap silindi--")

    elif işlem == "3":
        kütüphane.kitapları_goster()


    elif işlem == "4":
        print("--Kitap Sorgula--")
        isim = input("Kitap ismi:")

        kütüphane.kitap_sorgula(isim)

    else:
        print("--Geçersiz işlem--")


























