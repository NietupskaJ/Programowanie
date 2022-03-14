### Zapoznaj się z prostymi typami zmiennych
 # print('Hello kognitywistyka') # funkcja (dalej jako fun) print wyświetla wynik na ekranie
#
## nazwa zmiennej powinna mieć znaczenie, staraj się nie używać pojedyńczych liter a,b,c, lub liter+numer  x1,x2,x3
## kod w j.polskim lub angielskim, mix w/w jest możliwy ale nieprofesjonalny
## Konwencja w zapisie nazw zmiennych: snake vs camel  wybierz 1 z nich
'''
Raw: user login count
Camel Case: userLoginCount
Snake Case: user_login_count
'''
# name_of_car = 'mercedes'  # zmienna name_of_car jest typu string
# print(name_of_car) # 
# print('Lubię samochód marki mercedes a moja rodzina też lubi samochód marki: ' + name_of_car)  

############Zmienne numeryczne vs łańcuchowe (łańcuch znaków = wyraz, tekst) ###############
# num1 = 2  # zmienna a ma typ integer (liczba całkowita)
# num2 = 7.345134   # zmienna b typ float (liczba zmiennoprzecinkowa)
# num3 = num1 + num2
# # pot_num2_num3 = num2 ** num3  # ** to operator potęgowania  num2^num3
# print(num3)
# # print(pot_num2_num3)
# print(type(num2)) # fun type sprawdza typ zmiennej

# print("#####################")
# z = 'Ala'
# x = "ma"
# y = "koty"
# zdanie = y + x + z
# print(zdanie)
# print(y,x,z)
# X = 2     # python rozróżnia małe i duże litery (X to nie to samo co x)
# Y = '2'
# print("Zmienna X ma typ: ",type(X))
# print("Zmienna Y ma typ: ",type(Y))
# print(X+Y)
# print(X+int(Y))

### Komunikacja/interakcja z użytkownikiem
### Wpisz w konsoli liczby, zwróć uwagę na różnice między zmienną numeryczną i łańcuchową 
# zm1 = input("Podaj zmienną x =") # fun input służy do wprowadzania wartości przez uzytkownika w konsoli
# zm2 = input("Podaj zmienną y =") # wynik funkcji (argument wyjściowy funkcji) input ma typ string
# zm3_string = zm1 + zm2  # konwersję zmiennej string na  float
# print(zm3_string)

# zm1 = input("Podaj zmienną x =") # fun imput służy do wprowadzania wartości przez uzytkownika w konsoli
# zm2 = input("Podaj zmienną y =") # wynik funkcji (argument wyjściowy funkcji) input ma typ string
# zm3 = float(zm1) + float(zm2)  # konwersję zmiennej string na  float
# print(zm3)

############ Zmienne logiczne ###############
# a = True
# b = False # zmienna b typ logiczny bool
# print(type(a))
# x = '1'
# y = 1
# print(x == y)   # operator ==  oznacza czy x równe y?
# print(x != y)   # operator !=  oznacza czy x różny od y?
# a = 3
# b = 5
# print(a < b)
# print(a >= b)

##############Zadania do wykonania, Twoje pierwsze algorytmy
# 1. Wykonaj odejmowanie, mnożenie i dzielenie 2 dowolnych liczb

# #zm1 = float(input("Podaj zmienną x = "))
# #zm2 = float(input("Podaj zmienną y = "))
# wynik = zm1 + zm2
# print(zm1,'+', zm2, '=', wynik)

# zm1 = float(input("Podaj zmienną x = "))
# zm2 = float(input("Podaj zmienną y = "))
# wynik = zm1 - zm2
# print(zm1,'-', zm2, '=', wynik)


# 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)
# zm1 = float(input("Podaj zmienną x = "))
# zm2 = float(input("Podaj zmienną y = "))
# wynik = 2x+5y
# print('Wynik: ', wynik)


# 3. Popraw zmienną zdanie tak aby wyświetlany był napis: "Ala ma kota"
# z = 'Ala'
# x = "ma"
# y = "koty"
# print(z,x,y)
# z,x,y = 'Ala','ma','kota'



# 4. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
#  gdzie : a-imie, b-nazwisko, c-wiek, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)
# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nazwisko: ")
# wiek = input("Podaj wiek: ")
# kierunek  = input("Podaj nazwe kierunku : ")
# print('Jestem',imie, nazwisko, 'mam',wiek,'lat Studiuje',kierunek)



# 5. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646
# print( 1+2+10+20000001+4+347586970885 ==321784560456434534646)


# 6. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat

# x = int(input("Podaj liczbe:")
# reszta = x%2
# print('Liczba', x,'jest parzysta:', reszta == 0)

# 7. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
# iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
# 8. Sprawdź wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
#(x > 1 and x < 13) and x != 5  , dla x = 2
# Zadania dodatkowe:
# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",


# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nazwisko: ")
# wiek = input("Podaj wiek: ")
# kierunek  = input("Podaj nazwe kierunku : ")
# odzywianie = input("Czy zdrowo sie odzywiasz?")
# sport= input("Czy lubisz sport?")
# psy = input("Czy lubisz psy?")
# nauka= input("Czy lubisz się uczyć?")
# sesja=input("Zdales sesje?")

# print('Jestem', imie , nazwisko,'mam', wiek ,'lat Studiuje', kierunek,'Czy lubie sport?',sport, 'Czy lubie psy?',psy, 'Czy lubie sie uczyc?',nauka, 'Czy zdalam sesje?',sesja)

# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.
# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 10-ciu zdań, które wyświetlisz na ekranie
# print('Urodził się 20.04.1998 r. w Warszawie, na Bielanach. Jest synem nauczycielki polskiego i profesora nauk humanistycznych. Swoją edukację rozpoczął w Szkole Podstawowej  z Oddziałami Integracyjnymi nr. 223  im.Partyzantów Ziemi Kieleckiej. Miał dwie starsze siostry: Elżbietę, która była pielęgniarką  i Marię, która specjalizowała się w badaniach nad czarnymi dziurami, wykładała fizykę na Uniwersytecie Warszawskim. Swoją młodość spędził na Uniwersytecie w Białymstoku,studiował filologię polską. Po skończonych studiach zaczął pracę w renomowanym liceum. Opócz pracy, wiele czasu spędzał w Białowieskim Parku Narodowym.   Z zamiłowaniem oglądał ptaszynę i niepotykane nigdzie gatunki owadów, zwierząt.' )
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.


# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie


# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna
# a=True
# b=False
# print(type(a))

# print(x == y)   
# print(x != y)   
# # a = Grazyna, Janusz


