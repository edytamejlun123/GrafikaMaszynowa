from PIL import Image
import numpy as np


def rysuj_ramke_szare(w, h, grub, kolor_ramki, kolor):  # kolor od 0 do 255
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki  # wypełnienie tablicy szarym kolorem o wartości kolor_ramki
    tab[grub:h-grub, grub:w-grub] = kolor  # wypełnienie podtablicy kolorem o wartości kolor
    return Image.fromarray(tab)


im_ramka = rysuj_ramke_szare(120, 60, 8, 100, 200)
# im_ramka.show()




def rysuj_pasy_poziome_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = (k + zmiana_koloru) % 256
    return tab


tab1 = rysuj_pasy_poziome_szare(100, 246, 1, 10)
obraz1 = Image.fromarray(tab1)
# obraz1.show()


def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg


tab_neg = negatyw_szare(obraz1)
obraz_neg = Image.fromarray(tab_neg)
obraz_neg.show()


def rysuj_po_przekatnej_szare(w):
    t = (w, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(w):
        for j in range(w):
            tab[i, j] = (i + j)
    return tab


tab = rysuj_po_przekatnej_szare(256)
im = Image.fromarray(tab)
# im.show()


def rysuj_ramke_kolor(w, h, grub, kolor_ramki, kolor):  # kolor_ramki, kolor podajemy w postaci [r, g, b]
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy
    tab[:] = kolor_ramki  # wypełnienie tablicy kolorem kolor_ramki
    tab[grub:h - grub, grub:w - grub, 0] = kolor[0]   #  wartości kanału R
    tab[grub:h - grub, grub:w - grub, 1] = kolor[1]   #  wartości kanału G
    tab[grub:h - grub, grub:w - grub, 2] = kolor[2]   #  wartości kanału R
    # tab[grub:h - grub, grub:w - grub] = kolor # wersja równoważna
    return tab


tab = rysuj_ramke_kolor(120, 60, 8, [255, 0, 0], [255, 255, 255])
im_ramka = Image.fromarray(tab)
# im_ramka.show()


def rysuj_pasy_poziome_3kolory(w, h, grub):  # funkcja rysuje pasy poziome na przemian czerwony, zielony, niebieski
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if k % 3 == 0:
                    tab[i, j] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[i, j] = [0, 255, 0]
                else:
                    tab[i, j] = [0, 0, 255]
    return tab


tab1 = rysuj_pasy_poziome_3kolory(200, 100, 10)
obraz1 = Image.fromarray(tab1)
# obraz1.show()


def rysuj_pasy_poziome_kolor(w, h, grub, kolor,
                             zmiana_koloru):  # funkcja rysuje pasy poziome, przy czym kazda składowa koloru zwieksza się o "zmiana_koloru"
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    ile = int(h / grub)
    for k in range(ile):
        r = (kolor[0] + k * zmiana_koloru)
        g = (kolor[1] + k * zmiana_koloru)
        b = (kolor[2] + k * zmiana_koloru)
        for m in range(grub):
            i = k * grub + m
            for j in range(w):
                tab[i, j] = [r, g, b]
    return tab


tab1 = rysuj_pasy_poziome_kolor(200, 100, 10, [100, 200, 0], 32)
obraz1 = Image.fromarray(tab1)
# obraz1.show()


def koloruj_obraz(obraz, kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
    return tab


gwiazdka = Image.open("gwiazdka.bmp")
obraz2 = Image.fromarray(koloruj_obraz(gwiazdka, [120, 240, 50]))
# obraz2.show()


def rysuj_ramki_kolorowe(w, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = 6
    kolor_g = 4
    kolor_b = 2
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = kolor_r - zmiana_koloru_r
        kolor_g = kolor_g - zmiana_koloru_g
        kolor_b = kolor_b - zmiana_koloru_b
    return tab


tab = rysuj_ramki_kolorowe(200, 2, 4, 6)
obraz3 = Image.fromarray(tab)
# obraz3.show()