# print('############Zadanie 1##################')
# print('Utwórz funkcję o nazwie "SredniaLiczb", która wczyta od użytkownika liczby '
#       '(wariant najprostszy to minimum 3),'
#       ' i obliczy średnią z w/w liczb')
#


# print('############Zadanie 2##################')
# print('Utwórz funkcję o nazwie "cudswiata", która będzie wyświetlała),'
#       ' na ekranie nazwę 7 cudu świata np. "Koloseum",'
#       'następnie używając w/w funkcji napisz tekst reklamujący, opisujący jeden z 7 Cudów świata gdzie '
#       'wywołasz tą funkcję minimum 3 krotnie')
#

# def rys():
#    return 10
#
#
# print('Twoja liczba wynosi', rys() , 'A moja liczba wynosi: ', rys())


# print('############Zadanie 3  ##################')
# print('Utwórz funkcję o nazwie "ZdanieRozdziel", która wczyta od użytkownika pewien tekst,'
#       ' a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
#       ' i dla każdego zdania wyświetli'
#       'ile jest w nim wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu).')
# # użyj metody split do rozdzielenia elementów patrz przykład poniżej

# x = 'Ala ma kota. A Ola ma psa.'
# print(x.split('.'))
# print(len(x.split('.')))


# ############Skrypt dla zrozumienia kolejności operacji##############
# tekst = 'Ala ma kota. A Ola ma psa. Kasia ma chomika i sowę.'
# listazdan1 = tekst.split('.')     # podzieliliśmy tekst na zdania
# #print(listazdan1)
# liczbazdan = len(listazdan1)     # sprawdzamy ilość zdań w tekscie (długość listy listazdan1)
# #print(liczbazdan)
# # w liście listazdan1 na końcu była spacja więc ją omijamy w dalszych analizach
# listazdan2 = listazdan1[0:liczbazdan-1]        # wzięto elementy z listy listazdan1 tylko od indeksu 0 do liczbazdan-1
# print(listazdan2)                              # # [0:liczbazdan-1] <=> nazwalisty[min_element_listy:maksymalny_element_listy]
# 
# for zdanie in listazdan2:          # dla każdego zdania z listy listazdan2
#     listawyrazow = zdanie.split(' ')      # dzielimy zdanie na wyrazy
#     if zdanie == listazdan2[0]:          # jeśli to pierwsze zdanie z listy
#         #print(listawyrazow)
#         print('Liczba wyrazow:', len(listawyrazow))   # oblicz liczbę wyrazów (długość listy)
#     else:                              # każdym innym przypadku
#         #print(listawyrazow)
#         # w innych elementach listy listazdan2 niż pierwszym czyli o indeksie 0, mamy dodatkowy 1 element który jest spacją
#         # dlatego podajamy liczbę wyrazów mniejszą o 1
#         print('Liczba wyrazow:', len(listawyrazow)-1)  # oblicz liczbę wyrazów (długość listy) i obniż jej wymiar o 1
# 
# 
# ################# Funkcja
# 
# def liczbawyrazowwzadaniach(tekst):
#     listazdan1 = tekst.split('.')     
#     liczbazdan = len(listazdan1)    
#     listazdan2 = listazdan1[0:liczbazdan-1]        
#     print(listazdan2)
#     
#     for zdanie in listazdan2:         
#         listawyrazow = zdanie.split(' ')      
#         if zdanie == listazdan2[0]:         
#             print('Liczba wyrazow:', len(listawyrazow))   
#         else:                             
#             print('Liczba wyrazow:', len(listawyrazow)-1)
# 
# 
# t = 'Ala ma kota. A Ola ma psa. Kasia ma chomika i sowę.'
# liczbawyrazowwzadaniach(t)     # lub liczbawyrazowwzadaniach(tekst = t) 


# print("############Zadanie 4###########################")
# print('Zdefiniuj funkcję "Sylaby", która dla parametru będącego '
#       'wyrazem w języku polskim, zwróci listę jego sylab. '
#       'Funkcja nie musi być perfekcyjna i nie musi uwzględniać tzw. wyjątków')
#
# samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
# # sylaby = []
# # sylaba = ""
# # slowo = 'kognitywistyka'
# # for znak in slowo:
# #     if znak in samogloski:
# #         sylaba += znak    #  odpowiednik:  sylaba = sylaba + znak
# #         sylaby.append(sylaba)
# #         sylaba = ""
# #     else:
# #         sylaba += znak
# #
# # if sylaba:
# #     sylaby.append(sylaba)
# #
# # print(sylaby)
#
# print("############Zadanie 5###########################")

# print('Utwórz funkcję "Gwiazda", która wyświetli określony ciąg znaków'
#       'dla 3 podanych argumentów wejściowych:'
#       ' imie, nazwisko, lat'

#       'Przykład działania programu:'
#       '*******************'
#       ' Ala'
#       '*******************'
#       ' Kowalska'
#       '*******************'
#       ' 16 lat'
#       '*******************'
# print("############Zadanie 6###########################")
# print('Zdefiniuj funkcję "CiagGometryczny", która dla podanych trzech parametrów:'
#       ' n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie 1),'
#       ' q=wartość iloczynu ciągu geometrycznego (domyślnie 2) '
#       'zwróci n-ty element ciągu geometrycznego.')
#
#
