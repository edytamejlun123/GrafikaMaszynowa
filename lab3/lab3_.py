from PIL import Image
import numpy as np


# Zadanie 3/ 1.1
def rysuj_ramke(w, h, grub):  # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    ile = int(h / grub)
    for k in range(ile):
        tab[grub:h * w - grub, grub:k * w - grub] = 1  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu
        # tablicy [zakresy wysokości, zakresy szerokości] tablicy

    tab1 = tab.astype(np.bool_)
    # return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    return tab1


tab = rysuj_ramke(120, 60, 8)
im_ramka = Image.fromarray(tab)


# im_ramka.show()


def rysuj_ramke_odcienie_szarego(w, h, grub, kolor):  # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab[:] = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[grub:h - grub, grub:w - grub] = (k+kolor)%256  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu
                # tablicy [zakresy wysokości, zakresy szerokości] tablicy
    tab1 = tab.astype(bool)
    # return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    return tab


tab = rysuj_ramke_odcienie_szarego(120, 60, 10, 10)
im_ramka = Image.fromarray(tab)
im_ramka.show()


# Zadanie 3/ 1.2
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)


obraz2 = rysuj_pasy_pionowe(480, 320, 10)


# obraz2.save("obraz2.bmp")
# obraz2.show()


# Zadanie 3/ 1.3
def rysuj_kwadrat_w_punkcie(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[0:n, 0:m] = 0
    tab[m:h, m:w] = 0
    tab = tab.astype(bool)
    return Image.fromarray(tab)


obraz3 = rysuj_kwadrat_w_punkcie(480, 320, 100, 50)


# obraz3.save("obraz3.bmp")
# obraz3.show()


# Zadanie 3/ 1.4
def stworz_przekatna_dla_kwadratu(w, h, grubosc):
    obraz = np.full((h, w), 255, dtype=np.uint8)
    min_dimension = min(w, h)
    for i in range(min_dimension):
        for j in range(grubosc):
            if i + j < min_dimension:
                obraz[i + j, i] = 0
    return obraz


obraz4 = stworz_przekatna_dla_kwadratu(200, 200, 10)
img4 = Image.fromarray(obraz4)
# img4.save("obraz4.bmp")
# img4.show()
