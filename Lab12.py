## Klasa, z punktu widzenia programowania, jest to typ zmiennej.
## Natomiast w ujęciu projektowym jest to ogólna definicja pewnej grupy powiązanych ze sobą obiektów,
## które różnią się tożsamością. Klasa definiuje metody, czyli funkcjonalności, które są dostarczane przez obiekty.
## Poza tym definiuje również atrybuty, które są indywidualne (choć nie zawsze) dla konkretnych obiektów.
## Czym jest obiekt? Jest to konkretna zmienna danego typu czyli instancja danej klasy.

## Janek, Ania, Zosia to obiekty klasy Człowiek in. to poszczególne egzemplarze danej klasy czyli instancje
## Każde z nich może spać, jeść, poruszać się i to są właśnie metody zdefiniowane w klasie Człowiek.
## Oprócz tego każdy człowiek posiada imię oraz datę urodzenia, jednak są one indywidualne dla każdego obiektu,
## czyli nie są bezpośrednio powiązane z klasą, a z jej instancją (obiektem)

## Zapamiętaj w programowaniu  obiektowym  tworzymy/wykorzystujemy: klasy i obiekty.
## Klasa  tworzy nowy typ.(coś zaprojektować) Obiekty to są  egzemplarze (instancje) danej klasy.
## Klasa zawiera:
## a) elementy opisujące  stan (pola klasy)
## b) zachowania (metody klasy)
##
## Wyobraź sobie dwa różne obiekty: Samochód i Motyla  - to są dwie różne klasy
## Samochód: jeździ, wyrzuca spaliny, psuje się - to są metody klasy Samochód
## Motyl: lata, pije nektar  - to są metody klasy Motyl
## Samochód ma: masę, rok produkcji, typ silnika, pojemność silnika - to są pola/dane klasy Samochód
## Motyl ma: rozmiar skrzydeł, wagę, kolorystykę itp. - to są pola/dane klasy Motyl
##
## Ale jeżeli będziesz mieć  konkretny Samochód lub Motyla (np. Twoje własne)  to  będą one
## konkretnymi egzemplarzami, czyli obiektem klasy Samochód lub obiektem klasy Motyl

####################################################################################
# print('##########################################################')
# print('Przykład 1: Tworzymy klasę o nazwie Komputer1 oraz metodę o nazwie powitanie')
# print('Parametr ”self” to specjalny parametr (wpisuj go zawsze jako pierwszy argument w funkcji),')
# print('który przekazuje do każdej metody obiekt klasy na jakiej ma operować.')
# print('##########################################################')
# class Komputer1:
#     def powitanie(self):   # metoda powitanie
#         print('Witaj użytkowniku to ja Twój PC')

#
#
# mojKomputer = Komputer1() #Tworzymy obiekt klasy Komputer -> struktura: nazwa_obiektu = nazwa_Klasy()
# mojKomputer.powitanie()# Wywołujemy metodę -> metodę powitanie na obiekcie mojKomputer

# print('###################################################################')
# print('Zadanie 1')
# print('Utwórz klasę Imiona z metodą o nazwie zapytaj,'
#       'metoda zapytaj po wywołaniu na obiekcie klasy Imiona'
#       'powinna wyświetlić pytanie "Jak masz na imie?')
# print('###################################################################')

# class Imiona:
#     def (self):
#         print('Jak masz na imie?')

################################################################################
# print('Przykład 2: Utworzymy klasę o nazwie Komputer w której')
# print('zdefiniujemy pola: rodzajMatrycy, pojemnoscDysku w/w pola to zmienne proste')
# print('ustawimy też początkowe wartości w/w własności dla przykładowej instancji/konkretnego obiektu')
# class Komputer:
#     rodzajMatrycy = 'LCD' # zmienna widoczna tylko wewnątrz klasy
#     pojemnoscDysku = 100
#
#     def jakirodzajMatrycy(self):
#         return(self.rodzajMatrycy)  # wywołanie metody na obiekcie   self.nazwa_metody
#
#     def jakapojemnoscDysku(self):
#         return(self.pojemnoscDysku)
#
# mojKomputer = Komputer() #Tworzymy obiekt klasy Komputer
# w1 = mojKomputer.jakirodzajMatrycy()# przypisujemy do zmiennej w1 rezultat wywołania metody jakiRodzajMatrycy na obiekcie mojKomputer
# print(w1) ## wyświetlamy wynik
# w2 = mojKomputer.jakapojemnoscDysku()
# print(w2)

# print('###################################################################')
# print('Zadanie 2')
# print('Utwórz klasę Pies z polami: waga = 10, rasa = "Jamnik" ')
# print('Utwórz metody: jakaWaga, jakaRasa które będą wyświetlały wartości utworzonych pól')
# 

# class Komputer:
#   waga = 10
#   rasa = "Jamnik"

#   def jakaWaga(self):
#     return(self.waga)

#   def jakaRasa(self):
#    return(self.rasa)

# mojKomputer = Komputer()
# w1 = mojKomputer.jakaWaga()
# print(w1) 
# w2 = mojKomputer.jakaRasa()
# print(w2)

# #####################################################################################
# print('Przykład 3: Tworzymy klasę o nazwie Telewizor w której')
# print('zdefiniujemy pole, które będzie listą: listaKanalow')
# print('zdefiniujemy metodę jakieKanaly która wyświetli dostępne kanały')
# class Telewizor:
#     listaKanalow = ['TV1','Polsat','TVN']
#
#     def jakieKanaly(self):
#         for i in self.listaKanalow:
#             print(i)
#
# print('######Wynik działania Przykład 3 ###########')
# mojTelewizor = Telewizor()
# mojTelewizor.jakieKanaly()
# print('###################################################################')

# ###########################################################################################
# print('Zadanie 3')
# print('Utwórz klasę Kwiaty z 1 polem tj. listą zawierająca wartości: Tulipan, Hiacynt, Bez, Dalia')
# print('utwórz metodę: jakiRodzaj która będzie wyświetlała wartości z w/w listy')

# class Telewizor:
#  listaKwiaty = ['Tulipan, Hiacynt, Bez, Dalia'']

#                 def jakiekwiaty(self):
#                   for i in self.listaKwiaty:
#                     print(i)
#   mojTelewizor = Telewizor()
# mojTelewizor.jakieKanaly()








# ############################################################################
# # Metoda która jest wywoływana tylko raz (automatycznie podczas
# # tworzenia przez nas obiektu) nazywana jest konstruktorem.
# # Konstruktor możemy wykorzystać np. do ustalenia wartości początkowej pól klasy,
# # Załóżmy, że tworzysz 5 różnych obiektów (egzemplarzy) dla klasy Pies
# # więc każdego obiektu możesz przypisać inną wartość wagi i rasę bo
# # są różne rasy psów i psy mają różną wagę, ale możesz ustawić jakieś wartości początkowe
# print('Przykład 4: Tworzymy klasę o nazwie TV w której')
# print('zdefiniujemy pole, które będzie listą: listaKanalow oraz pole numerKanalu o wartości 1')
# print('zdefiniujemy konstruktor który ustawi/wyświetli bieżacy kanał włączony w TV')

# class TV:
#     listaKanalow = ['TV1','Polsat','TVN']
#     numerKanalu = 1
#
#     def __init__(self):      # __init__ to metoda, którą nazywamy konstruktorem, ustawia określone wartości pól gdy
#         print('Włączony kanał to: ' + self.listaKanalow[self.numerKanalu])           # obiekt jest tworzony
#
# mojTV = TV() # wywołanie



# print('################################################')
# print('Zadanie 4')
# print('Utwórz klasę Koty z 1 polem tj. listą zawierająca wartości: Pers, Egipski, Bengalski, Sfinks')
# print('utwórz konstruktor który przypisze i wyświetli dowolnie wybrany gatunek kota')
# class Koty:
#     listaKotow = ['Pers, Egipski, Bengalski, Sfinks']
#     kot = 1

#     def __init__(self):      
#         print('Wybrany kot to:' + self.listaKotow[self.kot])          

# mojKot = Koty() 





# print('################################################')
# print('Przykład 5: Nauczymy zmieniać wartości pól, tworzymy klasę o nazwie Muzyka w której')
# print('zdefiniujemy pole, które będzie listą zawierająca typy muzyki oraz pole nrTyp o wartości 0')
# print('zdefiniujemy konstruktor który ustawi/wyświetli początkowy typ muzyki')
# print('następnie zdefiniujemy metody ustawTypMuzyki, wyswietlTypMuzyki do zmiany wartości pola typ muzyki i wyświetlania wyniku ')

# class Muzyka:
#     typyMuzyki = ['ROCK','POP','JAZZ','KLASYKA','DISCO_POLO']
#     nrTyp = 0
#
#     def __init__(self):
#         self.typyMuzyki[self.nrTyp]
#         #print('Początkowy typ muzyki to: ' + self.typyMuzyki[self.nrTyp])
#
#     def ustawTypMuzyki(self, wpisanyNumer):
#         self.nrTyp = wpisanyNumer
#         #print(self.typyMuzyki[self.nrTyp])
#
#     def wyswietlTypMuzyki(self):
#         print('Ustawiony typ muzyki to: ' + self.typyMuzyki[self.nrTyp])
#
# # print('#################')
# mojaMuzyka1 = Muzyka()
# mojaMuzyka1.wyswietlTypMuzyki()
# mojaMuzyka1.ustawTypMuzyki(2)
# mojaMuzyka1.wyswietlTypMuzyki()

# print('######A teraz odblokuj kod który jest jeszcze bardziej uniwersalny########################')
# mojaMuzyka2 = Muzyka()
# mojaMuzyka2.ustawTypMuzyki(int(input("Wskaz numer typu muzyki od 1-5: "))-1)
# mojaMuzyka2.wyswietlTypMuzyki()
# #
#################
# print('Zadanie 5: Utwórz klasę o nazwie Egzamin w której')
# print('zdefiniujemy pole Przedmioty, które będzie listą zawierającą nazwy przedmiotów które zdajesz w tym semestrze
# oraz pole nrPrzedmiotu,
# wartość tego pola odpowiada nr przedmiotu który zdajesz jako pierwszy w sesji')
# print('zdefiniujemy konstruktor który ustawi/wyświetli początkowy przedmiot który będziesz zdawał w sesji')
# print('następnie zdefiniujemy 2 metody ustawPrzedmiot, wyswietlPrzedmiot do zmiany wartości w/w pola i wyświetlania wyniku ')
# print('wstaw odpowiedni komentarz dla wyświetlanej odpowiedzi, przetestuj swój program')

# class Egzamin:
#     Przedmioty = ['Logika Formalna','Programowanie', 'Filozofia umysłu']
#     nrPrzedmiot = 0
#
#     def __init__(self):
#         self.Przedmioty[self.nrPrzedmiot]
#
#     def ustawPrzedmiot(self, wpisanyNumer):
#         self.nrPrzedmiot = wpisanyNumer
#
#     def wyswietlPrzedmiot(self):
#         print('Zdaję teraz przedmiot: ' + self.Przedmioty[self.nrPrzedmiot])
#
# # print('#################')
# mojEgzamin = Egzamin()
# mojEgzamin.wyswietlPrzedmiot()
# mojEgzamin.ustawPrzedmiot(2)
# mojEgzamin.wyswietlPrzedmiot()

######################################################################
# print(' Przykład 6. Utwórz klasę Prostokat, ktora bedzie miała możliwość obliczenia pola powierzchni '
#       'prostokąta o bokach dowolnie zdefiniowanych przez użytkownika, początkowe wartości
# boków ustaw na 2 i 5')

# # ####wariant 1
# class Prostokat:
#     def __init__(self):
#         self.bokA = 2
#         self.bokB = 5
#         #return(print('Poczatkowe wartosci bokow to a = ' + str(self.bokA) + ' oraz b = ',str(self.bokB)))
#
#     def podajBokA(self,podanybokA):
#         self.bokA = podanybokA
#
#     def podajBokB(self, podanybokB):
#         self.bokB = podanybokB
#
#     def obliczpole(self):
#         S = self.bokA * self.bokB
#         return(print('Pole wynosi: '+ str(S)))
# # #
# mojProstokat = Prostokat()
# mojProstokat.obliczpole()  # bez ustawiania wartości boku A i B, program korzysta z wartości początkowych
# mojProstokat.podajBokA(10)  # ustawianie wartości boku A, początkowa wartość 2 zamieniana jest na 10
# mojProstokat.podajBokB(20)  # ustawianie wartości boku B, początkowa wartość 5 zamieniana jest na 20
# mojProstokat.obliczpole()

# ####wariant 2
# class Prostokat():
#     def __init__(self):
#         self.bokA = 2
#         self.bokB = 5
#
#     def podajBoki(self,bokA,bokB):
#         self.bokA = bokA
#         self.bokB = bokB
#
#     def obliczpole(self):
#         S = self.bokA * self.bokB
#         return(print('Pole wynosi: '+ str(S)))
#
# mojProstokat = Prostokat()
# mojProstokat.obliczpole()
# mojProstokat.podajBoki(3,15)
# mojProstokat.obliczpole()
#
# # ####wariant 3
# class Prostokat():
#     def __init__(self,bokA,bokB):
#         self.bokA = bokA
#         self.bokB = bokB
#
#     def obliczpole(self):
#         S = self.bokA * self.bokB
#         return(print('Pole wynosi: '+ str(S)))
#
# mojProstokat = Prostokat(2,5)
# mojProstokat.obliczpole()
######################################################################
# print(' Zadanie 6. Utwórz klasę Koło, ktora bedzie miała możliwość obliczenia pola powierzchni i
# obwodu koła'
#       'o promieniu dowolnie zdefiniowanym przez użytkownika,
#  początkową wartość promienia ustaw na 1')

class Koła():
#     def __init__(self,r,pi):
#         self.r = r
#         self.pi = pi
#     import math.pi 
#     def obliczpole(self):
#         S = 
#         return(print('Pole wynosi: '+ str(S)))
# mojProstokat = Prostokat(2,5)
# mojProstokat.obliczpole()