#-*- coding: utf-8 -*-
import numpy as np

#-*- coding: utf-8 -*-
import pandas as pd # biblioteka do obsługi tabel, ramek danych
import numpy as np
import os
#############Zadanie 1
# Utwórz klasę o nazwie Samochod, która ma pola: kolor, marka
# które można ustawiać dowolnie dla obiektu
# i 1 metodę o nazwie "drukuj" , która pozwala wyświetlić
# kolor i markę samochodu
#1
# class Samochod()
# def__init__(self,kolor, marka):
#   self.kolor = kolor
#   self.marka = marka


# ###########
# s = Samochod(kolor = 'czerwony' , marka = 'BMW')
# print(s.kolor)
# print(s.marka)


#2
# class Samochod():
#   def__init__(self,kolor = 'różowy', marka = 'audi'):
#   self.kolor = kolor
#   self.marka = marka


# ###########
# s = Samochod(kolor = 'czerwony' , marka = 'BMW')
# print(s.kolor) #domyslne parametry
# print(s.marka)

# class Samochod()
# def__init__(self,kolor, marka):
#   self.kolor = kolor
#   self.marka = marka

#   def print(self):
#     print('Kolor:{}, \n Marka:{}'.format (kolor,marka))

# ######
# s1= Samochod(kolor = 'bialy', marka = 'Fiat')
# s1.print()

#############Zadanie 2
# Utwórz etykietę: Jaki pojazd wybierasz?
# Utwórz 2 pola do wyboru:
# samochód i rower, użytkownik zaznacza odpowiedź, wciska przycisk OK i
# wyświetlany jest tekst z odpowiedzią wybraną przez użytkownika w oknie interfejsu

# from tkinter import *
# def run():
#   if var1.get() == 10: #tto włączony 1 radiobutton
#     t = 'Samochod'
#   elif var1.get() == 20: #tto włączony 2 radiobutton
#     t = 'Rower'
#   else
#    t='Nic nie zaznaczyłeś'
#   wynik.cofing(text = t)
# okno = Tk()
# okno.title('Pytanie')
# okno.geometry('200x200')
# Label(okno, text = 'Jaki pojazd wybierasz?').grid(row = 1, colums = 1)
# var1 = InVar()
# Radiobutton(okno,text = 'Samochod',variable = var1, value = 10).grid(row = 2, colums = 1)
# Radiobutton(okno,text = 'Rower',variable = var1, value = 20).grid(row = 3, colums = 1)
# Button(okno, text = 'OK', command = run).grid(row = 4, colums = 1)
# wynik = Label(okno, text = 'Jaki pojazd wybierasz')
# wynik.grid(row = 5, colums = 1)

# okno.mainloop()
#######################################################################
# print('Przykład 1 Utwórz klasę Ankieta, która będzie posiadała 5 pól: nazwisko, wiek, studia, lubi1, lubi2')
# print('oraz 5 metod: pytanieDane, pytanieWiek, pytanieStudia, pytanieLubi, wyswietlAnkiete')
# print('Zbierz informacje od conajmniej 2 użytkownikow, zadajac im pytania: o dane osobowe, wiek, kierunek studiow')
# print('o to co lubią robić w wolnym czasie, a następnie wyniki zapisz do listy/słownika ')
#
# class Ankieta(object):
#     nazwisko=[]
#     wiek = []
#     studia = []
#     lubi1 = []
#     lubi2 = []

#     def __init__(self):
#         return(print('Nazwisko: - ', 'Wiek: -', 'Studia: -', 'Lubi: -'))

#     def pytanieDane(self,noweNazwisko):
#         self.nazwisko = noweNazwisko
#         return(self.nazwisko)

#     def pytanieDane(self, wiek1):
#         self.wiek = wiek1
#         return(self.wiek)

#     def pytanieStudia(self, studia1):
#         self.studia = studia1
#         return (self.studia)

#     def pytanieLubi(self, lubi11,lubi22):
#         self.lubi1 = lubi11
#         self.lubi2 = lubi22
#         return([self.lubi1, self.lubi2])

#     def wyswietl(self):
#         mojSlownik = {'Imie_Nazwisko': self.nazwisko, 'Wiek': self.wiek, 'Studia_kierunek': self.studia,'Lubi': [self.lubi1, self.lubi2]}
#         print(mojSlownik)
#
# mojaAnkieta = Ankieta()
# mojaAnkieta.wyswietl()
# #mojaAnkieta.nazwisko = 'Kowalska'
# mojaAnkieta.nazwisko = input('Podaj nazwisko: ')
# mojaAnkieta.wiek = 18
# mojaAnkieta.studia = 'Informatyka'
# mojaAnkieta.lubi1 = 'Spacery z psem'
# mojaAnkieta.wyswietl()
# mojaAnkieta.lubi2 = 'Muzyka'
# mojaAnkieta.wyswietl()

# print('Zadanie 3 Twoim zadaniem będzie zebranie informacji w formie ankiety od conajmniej 3 osób planujących')
# print('swoje wakacje, zadaj odpowiednie pytania, zbierz interesujące Cię informacje')
# print('Utwórz klasę Wakacje, conajmniej 6 pól np.: wiek, płeć, kraj, miasto, transport, liczbaOsob')
# print('conajmniej 4 metod: pytanieWiek, ..., pytanieliczbaOsob, wyswietlAnkiete')
# print('Zbierz informacje od conajmniej 2 użytkownikow, zadajac im pytania: o dane osobowe, wiek, kierunek studiow')
# print('o to co lubią robić w wolnym czasie, a następnie wyniki zapisz do listy/słownika

#######################################################################
# print('Przykład 4 Utwórz klasę Tekst, która będzie posiadała metodę: )
# print(' kapitalikiTekst - która zamienia litery tekstu na duże litery i wyświetla tekstu')
# print('Następnie zaprezentuj działanie w/w metody, na dowolnym tekście, który deklaruje użytkownik')
# wariant1
# class Tekst(object):  # wpisanie Tekst(object): bardziej programistycznie poprawne niż Tekst(): czy też Tekst:
#     def __init__(self):
#         self.text = input("Podaj tekst = ")
#
#     def kapitalikiTekst(self):
#         duzyText = self.text.upper()
#         print(duzyText)
#
# malyText = Tekst()
# malyText.kapitalikiTekst()

# wariant2 - działający ale niepoprawny
# class Tekst():
#     def wczytajTekst(self):
#         self.text = input("Podaj tekst = ")
#
#     def kapitalikiTekst(self):
#         duzyText = self.text.upper()
#         print(duzyText)
#
# #############
# malyText = Tekst()
# malyText.wczytajTekst()
# malyText.kapitalikiTekst()
# ############
# malyText = Tekst()
# malyText.kapitalikiTekst() #zwróć uwagę że jeżeli użytkownik nie wpisze metod w odpowiedniej kolejności to ma błąd

# wariant3
# class Tekst(object):
#     def __init__(self):
#         self.text = 'Oto test tekst: jeżeli chcesz zamienić swój własny tekst użyj właściwej metody'
#
#     def wczytajTekst(self):
#         self.text = input("Podaj tekst = ")
#
#     def kapitalikiTekst(self):
#         duzyText = self.text.upper()
#         print(duzyText)
#
# malyText = Tekst()
# malyText.kapitalikiTekst()
# malyText.wczytajTekst()
# malyText.kapitalikiTekst()
# malyText.kapitalikiTekst()

# print('Zadanie 5 Do klasy Tekst dodaj metody o nazwach: podzielPrzecinekTekst, podzielKropkaTekst, podzielSpacjaTekst ')
# print('w/w metoda dzieli na N - części tekst w którym  odpowiednio dla metody')
# print(N -  przecinków lub kropek lub spacji, wyświetla rozwielony tekst jako elementy listy')
# print('do rozdzielania tekstu na zadania można użyć metody split(".")')

########## obsługa błędów
#liczba = int(input('podaj liczbe: '))
#print(liczba)
## jesli uzytkownik wpisze słownie liczbe np, 'cztery'
################################
# try:
#     liczba = int(input('podaj liczbe: '))
# except(ValueError):
#     liczba = 0
#     print('Nie wpisałeś liczby numerycznie, podstawiono 0')
#
# print(liczba)
#############################
################################
# lista1 = ['TV1','TV2','Polsat','TVN']
# print(lista1[5]) # IndexError, użytkownik wpisał indeks wiekszy niz dostępny
#######################################
# lista1 = ['TV1','TV2','Polsat','TVN']
# indeks = int(input('podaj indeks: '))
# try:             # klausula try
#     kanal = lista1[indeks]
# except(IndexError):
#     print('Wpisany indeks nie istnieje, ustawiono kanał 1')
#     kanal = lista1[0]  # lista1[0] to "sztucznie" przypisana wartość tzw. argument wyjątku
#
# print(kanal)
# ################# inne typy błędów: https://pl.python.org/docs/tut/node10.html

# print('Przykład 3 ')
# def poleKola1(r):
#     pole = np.pi * r ** 2
#     print(pole)
#
# poleKola1(4)
# poleKola1('cztery')


# def poleKola2(r):
#     assert r == int, 'Wpisana liczba to nie typ integer' # czy r jest typu integer?
#     pole = np.pi * r ** 2
#     print(pole)
#
# poleKola2('cztery')
###########################################################
# promienie = [10, 20, 30, 40, 50]
#
# def poleKola3(indeks):
#     try:
#         pole = np.pi * promienie[indeks] ** 2
#     except (IndexError,TypeError,ValueError) as e:
#         print(e)
#     else:
#         print(pole)
#
# poleKola3(1)
# poleKola3(7)
# poleKola3('dwa')

# print('Zadanie 6 Zaprojektuj i utwórz klasę Kwadrat, utworz metody o nazwie: obliczPole,')
# print('obliczObwod', zadanie wykonaj z obsługą błędów)