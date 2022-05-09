#######Teoria########################################

# #def nazwafunkcji(arg.wejsciowy1,arg.wejsciowy2,...,arg.wejsciowyN): # argumenty.wejsciowe - to nazwy zmiennych, których wartości musimy znać aby obliczyć
# #       instrukcje
# #    return arg.wyjsciowy1               #  argument/-y wyjściowe
##
##
##    Wywołanie funkcji:
##   nazwafunkcji(wartość.argumentu.wejsciowego1,wartość.argumentu.wejsciowego2,...,wartość.argumentu.wejsciowegoN)



######'Przykład 1 - porównanie funkcji')
#
#
# ###########standardowy sposób tworzenia funkcji
#def DodajLiczby(x, y):
#     suma = x + y
#     return suma
# #
# k = DodajLiczby(3, 5)
# print(k)
# print(DodajLiczby(3, 5))
# print(DodajLiczby(x = 3, y = 5))
# print('Wynik standardowej:',DodajLiczby(3,5))

############## Przykład dodatkowy ##########
# def DodajLiczby(x, y):  # Pamiętaj zmienne wewnątrz funkcji są lokalne
#     z = x + y           # czyli widoczne tylko wewnątrz funkcji, a nie w całym programie
#     return z
#
# def MnozLiczby(x, y):
#     z = x * y
#     return z


### Jesli jakaś część kodu powtarza się kilkukrotnie w programie utwórz dla niego funkcję
### Oblicz wyrażenie  w = ((x+y)xy + (x+y)^2)/xy  dla dowolnych y i x

# x = int(input('Podaj x = '))
# y = int(input('Podaj y = '))
# w = (DodajLiczby(x, y)*MnozLiczby(x, y) + DodajLiczby(x, y)**2)/MnozLiczby(x, y)
# print(w)

######## Przykłady wykorzystania funkcji wbudowanej o nazwie lambda i map

# ######## funkcja lambda   (to taka funkcja "malutka")
##  nazwaFunkcji = lambda arg1,arg2:instrukcja
# LiczbyDodaj = lambda x, y: x + y
# print('Wynik wywołania funkcji lambda:', LiczbyDodaj(3, 5))
# #
#
#
# ######## funkcja map
# def potega(liczba):
#     wynik = liczba ** 2
#     return wynik
#
# Lista2 = [2, 10, 15, 100, -5]  # to samo można uzyskać korzystając z pętli: [double(n) for n in Lista2]
#
# ### map(nazwaFunkcji,listaWartościPoszczególnychDanych)
# wynik = list(map(potega, Lista2))  # wynik funkcji map wpisz do listy jeśli chcesz obejrzeć rezultat
# print(wynik)
# ########### W/w wariant z lambda#####
#
# potega2 = lambda liczba:liczba**2
# wynik2 = list(map(potega2, Lista2))
# print(wynik2)
#
# # ########funkcja lambda i map
#Lista2 = ['Ala', 'ma', 'kota']
#zamien_jeden_wyraz = lambda jeden_element_listy: jeden_element_listy.upper()
#kapitaliki = map(zamien_jeden_wyraz, Lista2)
#print('Wynik wywołania funkcji map:', list(kapitaliki))

# ###Dodatkowe info
## kod: lambda element_listy: element_listy.upper() - zamienia małe litery w jednym wyrazie
##                                                     który jest elementem listy na duże litery
###########Zadanie 1a###########################")
##### Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
##### z funkcji lambda połącz kolejne litery w jeden wyraz(swoje imie)
# x = ['A','n','a']
# g = lambda x: x[0]+x[1]+x[2]
# print(g(x))
##### ###########Zadanie 1b###########################")
##### Przypisz do zmiennej wartość która będzie twoim nazwiskiem następnie korzystając
##### z funkcji lambda rozdziel wyraz na poszczegolne litery swojego imienia')
# Nazwisko = 'Polewko-Klim'
# mojaFun = lambda wyraz: [wyraz[i] for i in range(0,len(wyraz))]
# print(mojaFun(Nazwisko))

############Zadania do samodzielnej realizacji
########Zadanie 2###################################
##### Utwórz funkcje która obliczy sumę, iloczyn, iloraz 3 liczb


########Zadanie 3###################################')
##### Utwórz funkcje Roznica (która odejmuje 2 liczby) i Iloczyn (która mnoży 2 liczby)
##### nastepnie korzystając z w/w funkcji oblicz dla dowolnych dwóch liczb zadeklarowanych przez użytkownika
##### oblicz wyrażenie [(x*y)-(x-y)]/(x-y)')

##### ###Zadanie 4###################################')
##### Utwórz funkcje która w słowie (1 argument funkcji), które wskaże użytkownik
##### znajdzie literę (2 argument funkcji), którą wskaże użytkownik

#### Możesz wykorzystać przykładowy kod:
#wyraz = 'dom'
#litera = 't'

#lista_wyraz = list(wyraz)  # zapisuję litery wyrazu jako elementy listy
#if  lista_wyraz.count(litera) == 0:   # sprawdzam ilość wystąpień mojej wybranej litery w wyrazie
#    print('Ta litera nie występuje w wyrazie')
#else:
#    index_litery = lista_wyraz.index(litera)
#    numer_litery = lista_wyraz.index(litera)+1
#    print('indeks litery: ', index_litery)
#    print('numer litery w wyrazie: ', numer_litery)

#########Zadanie 5###################################')
##### Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji
##### Utwórz funkcje Pion: która rysuje gwiazdeki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji
##### Korzystając z w/w funkcji narysuj litery: E, L
