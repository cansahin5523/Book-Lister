import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from tkinter import *

pencere = Tk()
pencere.geometry("850x500")
pencere.title("Book Comporison")

etiket = Label(pencere)
etiket.config(text="Kitap Adını Giriniz",font=("Times",13))
etiket.place(x=30,y=30)

e1 = Entry(pencere)
e1.place(x=30,y=60)

browser = webdriver.Chrome(ChromeDriverManager().install())

def bkm():
    #bkm kitap
    e1String = e1.get()
    url = "https://www.bkmkitap.com/"
    browser.get(url)
    searchbar1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/header/div/div[3]/div/div[2]/div/div/div[4]/form/div[1]/div/input")
    searchbar1.send_keys(e1String)
    search = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/header/div/div[3]/div/div[2]/div/div/div[4]/form/div[2]/input").click()
    time.sleep(3)
    sorce = browser.page_source
    soup = BeautifulSoup(sorce,'html.parser')

    bkmAdListe = []
    #kitabın yazarı
    kaynak1 = soup.findAll("div",{"class":"col col-12 productDetails loaderWrapper"})
    kaynak2 = soup.findAll("div",{"class":"box col-12 text-center"})
    kaynak3 = soup.findAll("a",{"class":"fl col-12 text-description detailLink"})
    for kitabadi in kaynak3:
        kitap_adi = kitabadi.text
        bkmAdListe.append(kitap_adi)

    bkmFiyatListe = []
    #kitabın fiyatı
    kaynak = soup.findAll("div", {"class": "col col-2 col-md-4 col-sm-6 col-xs-6 p-right mb productItem zoom ease"})
    for fiyat in kaynak:
        yazi = fiyat.find_all("div",{"class": "col col-12 currentPrice"})
        for res in yazi:
            kitap_fiyat = res.text
            bkmFiyatListe.append(kitap_fiyat)

    #kitabın yayınevi
    yayinEviListe = []
    kaynak5 = soup.findAll("div",{"class":"col col-12 productDetails loaderWrapper"})
    kaynak4 = soup.findAll("div",{"class":"box col-12 text-center"})
    for yayınevi in kaynak4:
        yayin = yayınevi.find_all("a",{"class":"col col-12 text-title mt"})
        for yayın in yayin:
            yayinEvi = yayın.text
            yayinEviListe.append(yayinEvi)

    sayac = 0
    listbox = Listbox(pencere,width=30, height=27)
    listbox.place(x=200,y=30) 

    for i in bkmAdListe:
        listbox.insert(sayac,i)
        sayac += 1
    for z in bkmFiyatListe:
        listbox2.insert(sayac,z)
        sayac += 1
    for x in yayinEviListe:
        listbox3.insert(sayac,x)
        sayac += 1        

buton = Button(pencere)
buton.config(text="Kitap Bul",command=bkm)
buton.place(x=50,y=90)

listbox = Listbox(pencere,width=30, height=27)
listbox.place(x=200,y=30) 

listbox2 = Listbox(pencere,width=30,height=27)
listbox2.place(x=400,y=30)

listbox3 = Listbox(pencere,width=30,height=27)
listbox3.place(x=600,y=30)

etiket2 = Label(pencere)
etiket2.config(text="Kitap Adı",font=("Times",13))
etiket2.place(x=200,y=6)

etiket3 = Label(pencere)
etiket3.config(text="Kitap Fiyatı",font=("Times",13))
etiket3.place(x=400,y=6)

etiket4 = Label(pencere)
etiket4.config(text="Yayınevi",font=("Times",13))
etiket4.place(x=600,y=6)

pencere.mainloop()
