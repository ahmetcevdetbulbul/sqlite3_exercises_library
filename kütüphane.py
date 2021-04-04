import sqlite3
import time




class Kitap():
    def __init__(self,isim,yazar,yayınevi,sayfa_sayısı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.sayfa_sayısı = sayfa_sayısı

    def __str__(self):
       return """
        isim: {}
        yazar: {}
        yayınevi: {}
        sayfa sayısı: {}
        """.format(self.isim,self.yazar,self.yayınevi,self.sayfa_sayısı)

class Kütüphane():
    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("kütüphane.db")

        self.cursor = self.con.cursor()

        self.cursor.execute("Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,sayfa_sayısı INT)")
        self.con.commit()


    def kapat(self):
        self.con.close()


    def kitapları_goster(self):

        sorgu =  "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3])
                print(kitap)
                print("-------------------------")




    def kitap_ekle(self,kitap):
        self.cursor.execute("Insert Into kitaplar VALUES (?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.sayfa_sayısı))
        self.con.commit()

    def kitap_sil(self,isim):
        self.cursor.execute("Delete From kitaplar where isim = ?",(isim,))

        self.con.commit()

    def kitap_sorgula(self,isim):
        self.cursor.execute("Select * From kitaplar where isim = ?",(isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("böyle bir kitap bulunmuyor!!")
        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], )
            print(kitap)
            print("-------------------------")











