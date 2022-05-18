from tkinter import *  # biblioteka do tworzenia interfejsu graficznego użytkownika
#import numpy as np
#import matplotlib.pyplot as plt

######Przykład 1 - Tworzenie suwaka
# okno = Tk()
# okno.geometry("400x200")
#
# suwak1 = Scale(okno, from_=0, to=40,tickinterval=10)  #suwak pionowy
# suwak1.grid(row = 1,column = 1)
#
# suwak2 = Scale(okno, from_=0, to=400, orient=HORIZONTAL) #suwak poziomy
# suwak2.grid(row = 2,column = 1)
#
# okno.mainloop()

##########Zadanie 1
# Utwórz 2 suwaki o etykietach: parametr A i parametr B o wartościach od 1 do 100,
# użytkownik ustawia wartości parametrów na suwakach
# po wciśnieciu kontrolki ok dodaje 2 ustawione na suwakach liczby, wynik wypisuje w oknie
###########################################################################################
# def wyswietlWynik():
#    suma = var1.get() + var2.get()
#    wyswietlany_tekst = "A + B = " + str(suma)
#    text3.config(text = wyswietlany_tekst)
# 
# okno = Tk()
# var1 = IntVar()
# var2 = IntVar()
# okno.geometry("400x200")
# text1 = Label(okno, text="Ustaw parametr A", bg="green", fg="white")
# text1.grid(row = 1,column = 1)
# suwak1 = Scale(okno, from_=0, to=100, orient=HORIZONTAL, variable = var1 )
# suwak1.grid(row = 2,column = 1)
# text2 = Label(okno, text="Ustaw parametr B", bg="red", fg="white")
# text2.grid(row = 3,column = 1)
# suwak2 = Scale(okno, from_=0, to=100, orient=HORIZONTAL, variable = var2)
# suwak2.grid(row = 4,column = 1)
# przycisk = Button(okno , text = "Suma", command = wyswietlWynik, fg="red")
# przycisk.grid(row = 5,column = 1)
# text3 = Label(okno, text=" ")
# text3.grid(row = 6,column = 1)
# okno.mainloop()

#####Przykład 2 - Tworzenie pól wielokrotnego wyboru, uwaga zwróć uwagę że możesz skrócić kod oraz wyrównać
# okno2 = Tk()
# var1 = IntVar()   # możliwe typy np:StringVar(), IntVar(), BooleanVar()
# Checkbutton(okno2 , text="lubie dawać prezenty", variable=var1).grid(row=0, sticky=W, pady=4) # sticky = W - wyrównaj do lewej
# var2 = IntVar()
# Checkbutton(okno2 , text="lubie dostawać prezenty", variable=var2).grid(row=1, sticky=W,pady=4) # pady=4 - odstęp równy 4 row nad/pod kontrolką
# okno2.mainloop()

##########Zadanie 2
#Pewna firma zleciła Ci wykonie badania ankietowego dotyczącego kupowanych przez konsumentów produktów na święta:
# Do każdego pytania utwórz 2-3 kontrolki wielokrotnego wyboru z następującymi opcjami do wyboru.
# np. Co najczęściej kupujesz dla rodziny w prezencie?
# opcja 1: agd
# opcja 2: kosmetyki
# opcja 3: odzież
#Podsumowanie wypełnionej ankiety przez konsumenta wyświetl w Consoli po wciśnieciu kontrolki "Koniec ankiety"
# def Podsumuj():
#   if var.get()==1:
#     print("mamie")
#   elif var.get()==2:
#     print("tacie")
#   elif var.get()==3:
#    print("siostrze")



# okno2 = Tk()
# okno2.title("Ankieta")
# okno2.geometry("400x200")
# var = IntVar()   
# # print("Komu najczęściej Pani/Pan daje prezenty")
# Label(okno2, text ="Komu najczesciej dajesz prezenty?").grid(row = 1, column = 1)
# Radiobutton(okno2, text = "mamie", variable=var, value=1).grid(row = 2,column = 1)
# Radiobutton(okno2, text = "tacie", variable=var, value=2).grid(row = 3,column = 1)
# Radiobutton(okno2, text = "siostrze", variable=var, value=3).grid(row = 4,column = 1)
# Button(okno2, text = "Koniec ankiety", command = Podsumuj).grid(row = 5,column = 1)
# okno2.mainloop()

######Przykład 3 - Kolorowanie pól
# okno3 = Tk()
# w = Label(okno3, text="Czerwony", bg="red", fg="white")
# w.pack(fill=X)
# w = Label(okno3, text="Zielony", bg="green", fg="black")
# w.pack(fill=X)
# mainloop()

# okno = Tk()
# okno.geometry("400x200")
# text1 = Label(okno, text ="Komu najczesciej dajesz prezenty?")
# przycisk1 = Button(okno2, text = "mamie".grid(row = 1, column = 1)
# przycisk1.grid(row = 1,column = 1)

##########Zadanie 3
# Niestety okres świąt to również zwiększony czas brania kredytów przez konsumentów
# Zaprojektuj prosty interfejs który obliczy ratę kredytu zgodnie ze wzorem:
# rata =(K*q^n*(1-q))/(1-q^n) gdzie: q = 1+p/100
# K - kwota udzielonego kredytu
# n - liczba okresów  (n=1,2,3)
# p - stopa procentowa (p=const, jako ułamek)
#############################################################
##########Zadanie 3
# Niestety okres świąt to również zwiększony czas brania kredytów przez konsumentów
# Zaprojektuj prosty interfejs który obliczy ratę kredytu 1000-10000zł zgodnie ze wzorem:
# rata =(K*q^n*(1-q))/(1-q^n) gdzie: q = 1+p/100
# K - kwota udzielonego kredytu
# n - liczba okresów  (n=1,2,3) np. mc
# p - stopa procentowa (p=const, wpisz jako ułamek)
# Uwaga jak wiadomo emocje można wyrazić za pomocą kolorów
# A zatem postaraj się uzależnić kolor wyświetlanej kwoty raty do spłaty od potencjalnych emocji klienta banku na
# widok ile musi oddać bankowi.
#############################################################
##########Zadanie 4
# Dziś utworzysz program który zostanie wykorzystany przez nauczyciela na zajęciach
# Nauczyciel ma problem aby nauczyć ucznia pojęć: smak, węch, emocje itp
# pomóż mu obejrzyj mapę myśli którą stworzył nauczyciel
# : https://jaksieuczyc.pl/wp-content/uploads/2014/01/wizualizacja_mapa_mysli.jpg
# Zaprojetuj interfejs dla ucznia gdzie uczeń będzie mógł z przyjemnością nauczyć się lub sprawdzić swoją wiedzę.
# Np1. Uczeń chce się dowiedzić jakie są typy skojarzeń, program je wyświetla
# Np2. Uczeń wybiera sobie pojęcie/pojęcia z listy których chce się nauczyć
# Np3. Uczeń wybiera pojęcie i sam wpisuje odpowiedz a program sprawdza wynik
# Np4. Uczeń wybiera pojęcia jakich chce się nauczyć a program losowo n- krotnie wyświetla odpowiedź
# aż uczeń wciśnie stop    






