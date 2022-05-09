import os
import pandas as pd  # pd to skrót dla pandas
import matplotlib.pyplot as plt #biblioteka do rysowania wykresów
import numpy as np

x = [1,2,3,8]
y = [1,4,9,16]
plt.plot(x, y, marker = 'o') #
plt.axis([0,10,0,20]) #ustaw zakres osi X i Y
plt.xlabel('OX') #podpisz oś x
plt.ylabel('OY') #podpisz oś Y
plt.show() #narysuj wykres


x = np.linspace(1.0, 4.0, 90, endpoint=True) # x =<1,4> złożony z 90 punktów
y = x**2 - 5*x + 6
plt.plot(x, y) #wykres liniowy parabola
plt.plot(x,0*x, color='pink') # nałożenie na wykres kolejnego tj. linii,
# # 0*x - wektor złożony z zer o liczbie elementów równej zmiennej x
plt.plot([2,3], [0,0], 'o', color='green') # zaznaczenie punktów na linii
# # współrzedne narysowanych punktów: [2,0] i [3,0]
plt.show()

x = 100 + 20*np.random.randn(10000)
print(np.random.randn(10000))
# metoda random.randn losuj 10000 liczb z sigma=1 wokół średniej = 0
plt.hist(x, 100, facecolor ='blue')
# histogram dla danych podzielonych na 100 przedziałów
plt.xlabel('Przedziały')
plt.ylabel('Prawdopodobienstwo')
plt.title('Rownanie cos')
plt.grid(True) # wstaw siatkę na wykresie
plt.show()

miu=100
sigma = 20
x = miu + sigma*np.random.randn(10000)
plt.hist(x, 50) # histogram dla danych podzielonych na 50 przedziałów
plt.xlabel('Przedziały')
plt.ylabel('Prawdopodobienstwo')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=20$')
plt.axis([40, 160, 0, 800])
plt.grid(True) # wstaw siatkę na wykresie
plt.show()




labels = ['Tulipany', 'Róże', 'Lilie', 'Żonkile']
sizes = [25, 20, 40, 15]   #procenty części
explode = (0, 0.1, 0, 0)  # wysunięcie określonej części
fig1, ax1 = plt.subplots() # subplots - wiele wykresów w 1 oknie
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90) # explode wysunięcie wykresu,
# startangle obrót wykresu
ax1.axis('equal')  # osie kwadratowe
plt.show()


