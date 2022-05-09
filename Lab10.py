from tkinter import *  #biblioteka do tworzenia interfejsu graficznego użytkownika

#######################################################################
###Przykład 1: Tworzenie kontrolki typu Przycisk") #####
#
# def wywolajFunkcje():  # funkcja wywoływana po wciśnięciu kontrolki przycisk1 z etykietą OK
#     print("Witaj użytkowniku")
# # # #
# okno = Tk() # tworzenie głównego okna
# okno.title("Moj interfejs uzytkownika 1") # tytuł okna
# okno.geometry("500x300") # rozmiar okna
# # #
# przycisk1 = Button(okno, text = "OK", fg="blue", command = wywolajFunkcje)
# przycisk1.grid(row = 1,column = 1) # grid() sposób ustawienia kontrolek, traktuje okno jako siatkę,
# # # # ###należy wskazać dokładne współrzędne pola, w którym dany element ma zostać zamieszczony.
# okno.mainloop() #tworzenie obiektów

#############Zadanie 1 ######################
# Utwórz 2 przyciski obok siebie:
# gdy wcisniesz 1-przycisk program wypisze twoje imie
# gdy wcisniesz 2-przycisk program wypisze twoje nazwisko

# def printImie():  # funkcja wywoływana po wciśnięciu kontrolki przycisk1 z etykietą imie
#     print("Aneta")
#
# def printNazwisko():  # funkcja wywoływana po wciśnięciu kontrolki przycisk1 z etykietą nazwisko
#     print("Polewko-Klim")
#
# okno2 = Tk() #tworzenie głównego okna
# okno2.geometry("300x300") # rozmiar okna
#
# przycisk1 = Button(okno2, text = "imie", fg="blue", command = printImie)
# przycisk1.grid(row = 1,column = 1)
# #
# przycisk2 = Button(okno2, text = "nazwisko", fg="red", command = printNazwisko)
# przycisk2.grid(row = 1,column = 2)
# #
# okno2.mainloop()

######Przykład 2: Tworzenie kontrolki typu Edit Text )")
# def pobierzDaneZedittext1():  # funkcja wywoływana po wciśnięciu kontrolki przycisk1 z etykietą OK
#     dodaj = int(edittext1.get())+10  # get() pobiera dane z kontrolki o nazwie text1
#     print(dodaj)
# # # #
# okno = Tk() #tworzenie głównego okna
# okno.title("Moj interfejs uzytkownika 2") # tytuł okna
# okno.geometry("500x300") # rozmiar okna
# #
# text1 = Label(okno, text ="Wpisz liczbe do ktorej dodasz liczbe 10") #Tekst Statyczny nad okienkiem edycyjnym
# text1.grid(row = 1,column = 1) #położenie tekstu nad okienkiem edycyjnym
# #
# edittext1 = Entry(okno,fg='red') # utworzenie kontrolki Edit Text
# edittext1.grid(row = 2,column = 1) # położenie kontrolki Edit Text w oknie
# # #
# przycisk1 = Button(okno , text = "OK", command = pobierzDaneZedittext1, fg="blue")
# przycisk1.grid(row = 3,column = 1) # grid() sposób ustawienia kontrolek, traktuje okno jako siatkę,
#
# okno.mainloop()


#############Zadanie 2 ######################
# # Utwórz 2 kontrolki typu edit tekst i 1 przycisk
# # po wcisnieciu przycisku program powinien dodawać wpisane przez użytkownika
# # w kontrolkach edit tekst liczby

#
# def sumFunction():  # funkcja wywoływana po wciśnięciu kontrolki przycisk1 z etykietą "x + y"
#     sumVariable = int(edittext1.get()) + int(edittext2.get())  # get() pobiera dane z kontrolki edittext1 i edittext2
#     print(sumVariable)
#
# okno = Tk()
# okno.title("Sumuj dwie liczby całkowite") # tytuł okna
# okno.geometry("500x300") # rozmiar okna
#
# text1 = Label(okno, text ="x = ") #Tekst Statyczny nad okienkiem edycyjnym
# text1.grid(row = 1,column = 1) #położenie tekstu nad okienkiem edycyjnym
#
# text2 = Label(okno, text ="y = ") #Tekst Statyczny nad okienkiem edycyjnym
# text2.grid(row = 2,column = 1) #położenie tekstu nad okienkiem edycyjnym
#
# edittext1 = Entry(okno,fg='red') # utworzenie kontrolki Edit Text
# edittext1.grid(row = 1,column = 2) # położenie kontrolki Edit Text w oknie
#
# edittext2 = Entry(okno,fg='red') # utworzenie kontrolki Edit Text
# edittext2.grid(row = 2,column = 2) # położenie kontrolki Edit Text w oknie
#
# pushbutton1 = Button(okno , text = "x + y", command = sumFunction, fg="blue")
# pushbutton1.grid(row = 3,column = 1) # grid() sposób ustawienia kontrolek, traktuje okno jako siatkę,
#
# okno.mainloop()

#############Zadanie 3 ######################
# Utwórz 2 kontrolki typu edit tekst i 1 przycisk "ok"
# po wcisnieciu przycisku program powinien łączyć dwa fragmenty zdań wpisane przez użytkownika
# w kontrolkach edit tekst. Tekst wpisywany powinien być w różnych kolorach

#
# def sumFunction():
#     sumVariable = edittext1.get() + ' ' + edittext2.get()
#     print(sumVariable)
#
# okno = Tk()
# okno.title("Łącz dwa fragmenty zdań")
# okno.geometry("500x300")
#
# text1 = Label(okno, text ="zdanie 1 = ")
# text1.grid(row = 1,column = 1)
#
# text2 = Label(okno, text ="zdanie 2 = ")
# text2.grid(row = 2,column = 1)
#
# edittext1 = Entry(okno,fg='red')
# edittext1.grid(row = 1,column = 2)
#
# edittext2 = Entry(okno,fg='blue')
# edittext2.grid(row = 2,column = 2)
#
# pushbutton1 = Button(okno , text = "Połącz zdania", command = sumFunction, fg="blue")
# pushbutton1.grid(row = 3,column = 1)
#
# okno.mainloop()
#

#############Zadanie 4 ######################
# Utwórz 1 kontrolkę typu edit tekst i 1 przycisk "ok"
# po wcisnieciu przycisku program powinien wyświetlić wpisany napis 5-krotnie

# def printText():
#     for i in range(0,5):
#         vartext = edittext.get()
#         print(vartext)
#
# okno = Tk()
# okno.title("Wyświetl tekst 5-krotnie")
# okno.geometry("500x300")
#
# text = Label(okno, text ="Tekst: ")
# text.grid(row = 1, column = 1)
#
# edittext = Entry(okno,fg='blue')
# edittext.grid(row = 1,column = 2)
#
# pushbutton = Button(okno , text = "Ok", command = printText, fg="blue")
# pushbutton.grid(row = 3,column = 1)
#
# okno.mainloop()

# # ####Przykład 3: Tworzenie kontrolki typu zaznacz opcję tj.Radiobutton )")
# def wywolajRadioButton():   # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#    mojnowytekst = "Włączony radiobutton to: " + str(var.get())
#    text1.config(text = mojnowytekst) # ustawienie tekstu w kontrolce o nazwie etykieta_text1
#
# okno = Tk()
# var = IntVar()  # ustawienie typu pobieranej zmiennej
# # ### tworzenie kontrolki radioButton
# R1 = Radiobutton(okno, text="Numer 1", variable=var, value=1, command=wywolajRadioButton)
# R1.grid(row = 1,column = 1) # położenie kontrolki radioButton o etykiecie R1
# #
# R2 = Radiobutton(okno, text="Numer 2", variable=var, value=2,command=wywolajRadioButton)
# R2.grid(row = 2,column = 1)
# #
# text1 = Label(okno, text ="Włączony radiobutton to: 0") #Tekst statyczny umieszczony pod kontrolką R2
# text1.grid(row = 4,column = 1) #położenie kontrolki z tekstem statycznym
#
# okno.mainloop()
############################################## stop
# #############Przykład 4: prosty kalkulator
# def wyswietlWynik():   # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#    if var.get() == 1: # sprawdzam ktora kontrolka radiobutton jest wcisnieta R1 czy R2
#         wynikDzialania = int(text1.get()) + int(text2.get())
#    if var.get() == 2:
#        wynikDzialania = int(text1.get()) - int(text2.get())
#    if var.get() == 3:
#        wynikDzialania = int(text1.get()) * int(text2.get())
#    if var.get() == 4:
#        wynikDzialania = int(text1.get()) / int(text2.get())
#
#    mojtekst = "Wynik działania to: " + str(wynikDzialania)
#    etykieta_text3.config(text = mojtekst) # ustawienie tekstu w kontrolce o nazwie etykieta_text3
#
# okno = Tk()
# var = IntVar()  # ustawienie typu pobieranej zmiennej
# okno.title("Kalkulator")
# okno.geometry("400x200")
# etykieta_text1 = Label(okno, text ="Wpisz pierwszą liczbę: ")
# etykieta_text1.grid(row = 1,column = 1)
# etykieta_text2 = Label(okno, text ="Wpisz drugą liczbę: ")
# etykieta_text2.grid(row = 2,column = 1)
# text1 = Entry(okno,fg='red')
# text1.grid(row = 1,column = 2)
# text2 = Entry(okno,fg='blue')
# text2.grid(row = 2,column = 2)
# R1 = Radiobutton(okno, text=" + ", variable=var, value=1)
# R1.grid(row = 1,column = 3)
# R2 = Radiobutton(okno, text=" - ", variable=var, value=2)
# R2.grid(row = 2,column = 3)
# R3 = Radiobutton(okno, text=" * ", variable=var, value=3)
# R3.grid(row = 3,column = 3)
# R4 = Radiobutton(okno, text=" / ", variable=var, value=4)
# R4.grid(row = 4,column = 3)
# etykieta_text3 = Label(okno, text ="Wynik działania to: 0")
# etykieta_text3.grid(row = 3,column = 1)
# przycisk3 = Button(okno , text = "Enter", command = wyswietlWynik, fg="red")
# przycisk3.grid(row = 4,column = 1)
# okno.mainloop()

#############Zadanie 5 ######################
# Rozbuduj kalkulator danych o opcje potęgowania
#############Zadanie 6 ######################
# Utwórz program który będzie grą dla dzieci:
# wyświetlana jest treść zagadki dla dziecka
# dziecko ma dwie opcje odpowiedzi do wyboru
# jeśli dziecko wybierze poprawną odpowiedź wyświeli się
# tekst "Brawo, jestes super"
# jeżeli dziecko wybierze błedną odpowidź
# wyświeli się tekst: "To nic, następnym razem ci się uda"

# def wyswietlWynik():   # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#    if var.get() == 1: # sprawdzam ktora kontrolka radiobutton jest wcisnieta R1 czy R2
#         wynikDzialania = "To nic, następnym razem ci się uda"
#    if var.get() == 2:
#        wynikDzialania =  "Brawo, jestes super"
#    etykieta_text2.config(text = wynikDzialania) # ustawienie tekstu w kontrolce o nazwie etykieta_text3
#
# okno = Tk()
# var = IntVar()  # ustawienie typu pobieranej zmiennej
# okno.title("Zagadka")
# okno.geometry("400x200")
# etykieta_text1 = Label(okno, text ="Jaki kolor ma słońce ?")
# etykieta_text1.grid(row = 1,column = 1)
# R1 = Radiobutton(okno, text=" kolor zielony ", variable=var, value=1,command = wyswietlWynik)
# R1.grid(row = 2,column = 1)
# R2 = Radiobutton(okno, text=" kolor żółty ", variable=var, value=2,command = wyswietlWynik)
# R2.grid(row = 3,column = 1)
# etykieta_text2 = Label(okno, text ="")
# etykieta_text2.grid(row = 4,column = 1)
# okno.mainloop()

#############Przykład 7 ######################
# Utwórz program który będzie grą dla dzieci:
# wyświetlana jest treść zagadki dla dziecka
# dziecko wpisuje odpowiedź do pola (kontrolka Entry)
# następnie dziecko wciska przycisk z napisem "Sprawdź"(kontrolka Button)
# jeśli dziecko wybierze poprawną odpowiedź wyświeli się
# tekst "Brawo, jestes super"
# jeżeli dziecko wybierze błedną odpowidź
# wyświeli się tekst: "To nic, następnym razem ci się uda"
# def wyswietlWynik():   # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#    if text1.get() == 'zolty': # sprawdzam ktora kontrolka radiobutton jest wcisnieta R1 czy R2
#        wynikDzialania = "Brawo, jestes super"
#    else:
#        wynikDzialania = "To nic, następnym razem ci się uda"
#    etykieta_text2.config(text = wynikDzialania) # ustawienie tekstu w kontrolce o nazwie etykieta_text3
# #
# okno = Tk()
# var = IntVar()  # ustawienie typu pobieranej zmiennej
# okno.title("Zagadka")
# okno.geometry("400x200")
# etykieta_text1 = Label(okno, text ="Jaki kolor ma słońce ?")
# etykieta_text1.grid(row = 1,column = 1)
# etykieta_text2 = Label(okno, text ="Twoja ocena zadania")
# etykieta_text2.grid(row = 3,column = 1)
# text1 = Entry(okno,fg='red')
# text1.grid(row = 2,column = 1)
# przycisk3 = Button(okno , text = "Sprawdz wynik", command = wyswietlWynik, fg="red")
# przycisk3.grid(row = 4,column = 1)
# okno.mainloop()

#############Zadanie 6 ######################
# Rozbuduj Program 6 o swoje własne zagadki min.3
#############################################