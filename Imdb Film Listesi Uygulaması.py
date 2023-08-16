#Imdb Film Listesi Uygulaması 
import requests
import json
import time
import re
import textwrap

class Film:
    def __init__(self):
        self.dongü=True

    def program(self):
        secim=self.menü()

        if secim=="1":
            self.eniyi259()
        if secim=="2":
            self.enpopuler()
        if secim=="3":
            self.sinemalarda()
        if secim=="4":
            self.yakinda()
        if secim=="5":
            self.filmara()
        if secim=="6":
            self.cikis()
        
    def menü(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim):
                raise Exception("Lğtfen 1 ve 6 arasında bir seçim yapınız...")
        while True:
            try:
                secim=input("Hoşgeldiniz.. Lütfen yapmak istediğiniz işlemi seçiniz..... \n\n1-En İyi 250 Film \n2-En popüler Filmler\n3-Sinemalarda\n4-Yakında Olan Filmler\n5-Film Ara\n6-Çıkış\n")                   
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break
        return secim

    def eniyi259(self):
        print("En iyi 250 film listesine Ulaşılıyor... \n")
        time.sleep(1)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_m648d9nv")
        sonuc=url.json()
        for i in sonuc["items"]:  # for döngüsü ile itemler arasından seçmek istediğimiz bilgiyi seçiyoruz.Ve yazdırıyoruz.
            print(i["fullTitle"])
        self.menudon()

        
       
    def enpopuler(self):
        print("En popüler filmler listesine ulaşılıyor...")
        time.sleep(1)
        url=requests.get("https://imdb-api.com/en/API/MostPopularMovies/k_m648d9nv")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
    def sinemalarda(self):
        print("Sinemalardaki filmlere ulaşılıyor..")
        time.sleep(1)
        url=requests.get("https://imdb-api.com/en/API/InTheaters/k_m648d9nv")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
    def yakinda(self):
        print("Yakında gelecek filmlere ulaşıluyor...")
        time.sleep(1)
        url=requests.get("https://imdb-api.com/en/API/ComingSoon/k_m648d9nv")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def filmara(self):
        print("Film ara menüsüne  ulaşıluyor...")
        time.sleep(1)
        film=input("Lüften film adını giriniz..")
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_m648d9nv")
        sonuc=url.json()
        ID=list()
        for i in sonuc["items"]:  #  İtems kısmından id yi bulup listeye ekler.
            ID.append(i["id"])
        AD=list()
        for i in sonuc["items"]:  #items kısmından title kısmını bulup listeye ekler.
            AD.append(i["title"])  

        cevir=zip(AD,ID) #ad ve ıd çevirme işlemi yapar.
        veri=dict(cevir) #sözlük yapısında oluşturur.   {ad,ıd}
        key=veri.get(film) 

        url2=requests.get("https://imdb-api.com/tr/API/Wikipedia/k_m648d9nv/{}".format(key)) 
        sonuc2=url2.json()

        print(textwrap.fill(sonuc2["plotShort"]["plainText"]),130)

        self.menudon()     
        

    def cikis(self):
        time.sleep(2)
        Sistem.döngü=False
        exit()

    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için 7'ye basınız. Çıkmak için Lütfen 6'ya basınız..")
            if x=="7":
                print("Ana mmenüye dönülüyor...")
                time.sleep(1)
                self.program()
                break
            elif x=="6":
                self.cikis()
            else:
                print("Lütfen geçerli bir seçim yapınız...")


Sistem=Film()
while Sistem.dongü:
    Sistem.program()
