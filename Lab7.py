import os   ## moduł obsługi plików, katalogów, dysków

'''
######################################################################
Uwaga: wymienione w przykładach nazwy katalogów i plików
nie występują w Twoim PC-cie, dostosuj ich nazwy do istniejących.

###############  Operacje na plikach i katalogach   ###################
Aby zmieniać, tworzyć katalogi, oglądać ich zawartość itp. będziemy stosować funkcje
i metody z bibioteki o nazwie os, ta biblioteka ma szereg metod, każda metoda umożliwia
zrealizowania pewnych operacji na katalogach. Zapoznaj się z przykładami metod poniżej
a następnie wykonaj zadania
#######################################################################
'''

####################### Przykład 1 #####################################
## Metoda getcwd() pozwala sprawdzić jaką ścieżkę ma bieżacy folder, czyli ten w którym
## znajduje się Twój plik z programem

# moj_obecny_folder = os.getcwd()
# print(moj_obecny_folder)
# print(os.getcwd())

######################### Przykład 2 ####################################
### metoda listdir('.') służy do sprawdzania zawartości katalogu
#
# zawartosc_biezacego_folderu = os.listdir('.')
# print(zawartosc_biezacego_folderu)

######################### Przykład 3 ####################################
### listdir('ścieżka dostępu do folderu') - zawartosc_konkretnego_folderu

# zawartosc_wskazanego_folderu = os.listdir('c:/Windows')  # jeśli pracujesz w replit to wpisz '/home'
# print(zawartosc_wskazanego_folderu)

# ######################### Przykład 4 ####################################
# print(os.getcwd())   # sprawdzamy jaki jest nasz katalog roboczy/bieżący
# os.chdir('c:/Users') # zmiana bieżącego katalogu dyskowego na inny np. c:/Users
# print(os.getcwd()) # sprawdzamy jaki jest roboczy po wywołaniu instrukcji zmiany

########################## Zadanie 1 #########################
### Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
### użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
### funkcja będzie wyświetlała zawartość wskazanego przez użytkownika katalogu
import os

# wariant podstawowy
# def zmienkatalog(pathkatalog):
#     print('Poprzednia lokalizacja:', os.getcwd())
#     os.chdir(pathkatalog)
#     print('Obecna lokalizacja:', os.getcwd())
#     print('Zawartość:', os.listdir(pathkatalog))
#
# katalog_uzytkownika = input('Podaj katalog wraz ze ściezką dostępu:')
# # katalog_uzytkownika = 'c:/Users'  # do testu
# zmienkatalog(katalog_uzytkownika)

# wariant z dokumentacją (opisem funkcji)
# def zmienkatalog(pathkatalog):
#     # ponizej jest dokumentacja funkcji
#     '''
#     to jest funkcja ktora zmienia katalog na wskazany przez użytkownika
#     Args:
#         pathkatalog (str): nazwa katalogu waraz ze scieżką dostępu do tego katalogu
#     Returns:
#         wyświetla nazwę bieżącego katalogu po zmianie
#     '''
#
#     print('Poprzednia lokalizacja:', os.getcwd())
#     os.chdir(pathkatalog)
#     print('Obecna lokalizacja:', os.getcwd())
#     print('Zawartość:', os.listdir(pathkatalog))
#
# katalog_uzytkownika = input('Podaj katalog wraz ze ściezką dostępu:')
# # katalog_uzytkownika = 'c:/Users'  # do testu
# zmienkatalog(katalog_uzytkownika)

## help(zmienkatalog)  # wyswietlenie dokumentacji do funkcji

########################## Zadanie 2 #########################
### Korzystając z utworzonej funkcji napisz program który będzie zmieniał bieżący katalog
### dyskowy na inny wskazany przez użytkownika oraz będzie wyświetlał zawartość wskazanego przez
### użytkownika katalogu ale tylko wówczas gdy użytkownik odpowie "TAK" na pytanie:
### "Czy mam zmienić katalog?


# def zmienkatalog(pathkatalog):
#     print('Poprzednia lokalizacja:', os.getcwd())
#     os.chdir(pathkatalog)
#     print('Obecna lokalizacja:', os.getcwd())
#     print('Zawartość:', os.listdir(pathkatalog))
#
#
# pytanie_do_uzytkownika = input('Czy chcesz zmienić katalog na inny, wpisz słowo tak: ')
# if pytanie_do_uzytkownika == 'tak':
#     katalog_uzytkownika = input('Podaj katalog wraz ze ściezką dostępu: ')
#     # katalog_uzytkownika = 'c:/Users'  # do testu
#     zmienkatalog(katalog_uzytkownika)
# else:
#     print('nie wpisales tak')


########################### Przykład 5 - Filtrowanie nazw plików i katalogów według określonego wzorca ########

# import fnmatch    # to jest moduł umożliwiający wyszukiwanie określonych ciągów znaków, zapewnia obsługę symboli wieloznacznych.
### funkcja o takiej samej nazwie jak moduł fnmatch(nazwa, wzorzec) sprawdza czy podana nazwa (typ String)
### zaczyna i/lub kończy się na określony wzorzec (typ String)
#
# zdanie = 'Python to jezyk programowania.py'
# czy_to_prawda1 = fnmatch.fnmatch(zdanie,'P*a') # czy zmienna zdanie zaczyna się na literę P i kończy na m
# print(czy_to_prawda1)
# czy_to_prawda2 = fnmatch.fnmatch(zdanie,'*.py') # czy zmienna zdanie kończy na m
# print(czy_to_prawda2)
# czy_to_prawda3 = fnmatch.fnmatch(zdanie,'P*')  # czy zmienna zdanie zaczyna się na literę P
# print(czy_to_prawda3)

############################# Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc, Lab4.txt)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się tym folderze tj. Dokument
## b) korzystając z metody Pythona i pętli wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym
#################################################################
# a)
#print(os.listdir('C:/Users/Student/PycharmProjects/ProgramowaniePython/Dokument'))
#b)
# import fnmatch
# lista_plikow = os.listdir('C:/Users/Student/PycharmProjects/ProgramowaniePython/Dokument')
# for plik in lista_plikow:   # iterujemy się kolejno po nazwach plików w liście
#     czy_doc = fnmatch.fnmatch(plik,'*docx')  # czy nazwa pliku kończy sie na docx
#     if czy_doc == True:   # jeśli tak to
#         print(plik)       # wypisz nazwę pliku

########################## Przykład 6 - sprawdzanie rozmiarów plików w bajtach
# print(os.getcwd())
# rozmiar_pliku = os.path.getsize('C:/Users/Student/PycharmProjects/ProgramowaniePython/Lab7.py')
# print(rozmiar_pliku)

################################  Zadanie 4 ########
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe, graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku

# nazwa_folderu_doc = 'C:/Users/Student/PycharmProjects/ProgramowaniePython/StudentDoc'
# lista_doc = os.listdir(nazwa_folderu_doc)
# # os.path.join(path, nazwa pliku)  ta metoda łączy ścieżke z nazwą pliku

# for plik in lista_doc:  # iterujemy się kolejno po nazwach plików w liście
#     pathplik = os.path.join('C:/Users/Student/PycharmProjects/ProgramowaniePython/StudentDoc/', plik)
#     print('Plik: {} ma rozmiar w bajtach: {}'.format(plik,os.path.getsize(pathplik)))

# #####
# nazwa_folderu_image = 'C:/Users/Student/PycharmProjects/ProgramowaniePython/StudentObrazy'
# lista_image = os.listdir(nazwa_folderu_image)
# for plik in lista_image:
#     pathplik = os.path.join('C:/Users/Student/PycharmProjects/ProgramowaniePython/StudentObrazy/', plik)
#     print('Plik: {} ma rozmiar w bajtach: {}'.format(plik,os.path.getsize(pathplik)))

############################### Przykład 7 ###############
## Metoda makedirs() służy do tworzenia nowego folderu w bieżącym folderze
## jeżeli folder istnieje to program wyrzuci błąd
#os.makedirs('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa')

################################  Przykład 8 - zmiana nazwy folderu
## rename(stara_nazwa,nowa_nazwa)
#os.rename('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa', 'C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa2')
#print(os.listdir('C:\\Users\\aneta\PycharmProjects\Programowanie1'))

################################# Zadanie 5 ###########################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.