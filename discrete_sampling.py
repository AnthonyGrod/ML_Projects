import numpy as np
import matplotlib.pyplot as plt


def losuj():
    return np.random.randint(0, tablica.size)


def probkowanie():
    liczbaProb = 0
    dni = set()
    while True:
        dzien = losuj()
        if np.random.rand() * (1 + e) * q[dzien] < p[dzien]:
            if dzien not in dni:
                dni.add(dzien)
                liczbaProb += 1
            else:
                return liczbaProb + 1


dane = np.loadtxt('us_births_69_88.csv', delimiter=',', skiprows=1, dtype=int)
tablica = np.zeros(12 * 31)
licznik = 0
suma = 0
for rzad in dane:
    tablica[licznik] = rzad[2]
    licznik += 1
    suma += rzad[2]

q = [1 / tablica.size] * tablica.size
p = np.zeros(tablica.size)
for i in range(tablica.size):
    p[i] = tablica[i] / suma

e = 0.0
for i in range(tablica.size):
    e = max(e, p[i]/q[i] - 1)


wyniki = np.array([probkowanie() for wynik in range(100000)])

plt.hist(wyniki, bins=range(1, 101))
plt.show()
