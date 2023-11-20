from PIL import Image
import numpy as np

# ZADANIE 1 tryb l
def rysuj_ramke(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(int(h/grub)):
        if i % 2 == 1:
            tab[i * grub: h - (i * grub), i * grub:w - (i * grub)] = 1
        else:
            tab[i*grub: h-(i*grub), i*grub:w-(i*grub)] = 0
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)


img = rysuj_ramke(200, 200, 10)
img.save("obraz z lab 2.png")
# Zadanie 1


def rysuj_ramke_szara(w, h, grub, kolor): # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    ile = int((h/grub)/2)
    for k in range(ile):
        for i in range(int(h/grub)):
            if i % 2 == 1:
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub)] =(kolor+k)+30
            else:
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub)] = (kolor+k)
    return Image.fromarray(tab)


tab_szare1 = rysuj_ramke_szara(200, 200, 10, 100)
tab_szare1.save("obraz1_1.png")
tab_szare1.save("obraz1_1.jpg")

def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return Image.fromarray(tab_neg)


tab_negatyw1 = negatyw_szare(tab_szare1)
tab_negatyw1.save("obraz1_1N.jpg")
tab_negatyw1.save("obraz1_1N.png")

def rysuj_pasy_pionowe_lab2(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab*255
    return Image.fromarray(tab)
tab = rysuj_pasy_pionowe_lab2(200, 200, 1)
tab.save("obraz_2_z_lab_2.jpg")

def rysuj_pasy_pionowe(w, h, grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = (k+kolor)%256
    tab = tab*255
    return Image.fromarray(tab)

tab_pasy = rysuj_pasy_pionowe(200, 200, 1, 50)
tab_pasy.save("obraz1_2.jpg")
tab_pasy.save("obraz1_2.png")
tab_pasy_negatyw = negatyw_szare(tab_pasy)
tab_pasy_negatyw.save("obraz1_2N.jpg")
tab_pasy_negatyw.save("obraz1_2N.png")


# ZADANIE 2 TRYB RGB

def rysuj_ramke_kolorowa(w, h, grub, kolor1, kolor2): # grub grubość ramki w pikselach
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    ile = int((h/grub)/2)
    for k in range(ile):
        for i in range(int(h/grub)):
            if i % 2 == 1:
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub), 0] =kolor1[0]
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub), 1] =kolor1[1]
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub), 2] =kolor1[2]
            else:
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub), 0] = kolor2[0]
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub), 1] = kolor2[1]
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub), 2] = kolor2[2]
    return Image.fromarray(tab)


tab_kolor = rysuj_ramke_kolorowa(200, 200, 10, kolor1=[100, 250, 100], kolor2=[60, 34, 200])
# tab_neg_kolor = negatyw_kolor(tab_kolor)
# tab_neg_kolor.save("neg.jpg")
tab_kolor.save("obraz2_1.png")
tab_kolor.save("obraz2_1.jpg")


# NEGATYW KOLOROWE
def rysuj_ramke_kolorowa_neg(w, h, grub, kolor1, kolor2): # grub grubość ramki w pikselach
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    ile = int((h/grub)/2)
    for k in range(ile):
        for i in range(int(h/grub)):
            if i % 2 == 1:
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub), 0] = 255 - kolor1[0]
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub), 1] = 255 - kolor1[1]
                tab[i * grub: h - (i * grub), i * grub:w - (i * grub), 2] = 255 - kolor1[2]
            else:
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub), 0] = 255 - kolor2[0]
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub), 1] = 255 - kolor2[1]
                tab[i*grub: h-(i*grub), i*grub:w-(i*grub), 2] = 255 - kolor2[2]
    return Image.fromarray(tab)


tab_kolor_neg = rysuj_ramke_kolorowa_neg(200, 200, 10, kolor1=[100, 250, 100], kolor2=[60, 34, 200])
tab_kolor_neg.save("obraz2_1N.png")
tab_kolor_neg.save("obraz2_1N.jpg")


# FUNKCJA NUMER 2
def rysuj_pasy_pionowe_kolorowe(w, h, grub, kolor1, kolor2):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                if k %2 == 1:
                    tab[j, i, 0] = kolor1[0]
                    tab[j, i, 1] = kolor1[1]
                    tab[j, i, 2] = kolor1[2]
                else:
                    tab[j, i, 0] = kolor2[0]
                    tab[j, i, 1] = kolor2[1]
                    tab[j, i, 2] = kolor2[2]

    tab = tab*255
    return Image.fromarray(tab)

tab_pasy_kol = rysuj_pasy_pionowe_kolorowe(200, 200, 10, kolor1=[100, 230, 90], kolor2=[230, 20, 56])
tab_pasy_kol.save("obraz2_2.jpg")
tab_pasy_kol.save("obraz2_2.png")


def rysuj_pasy_kolorowe_neg(w, h, grub, kolor1, kolor2):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                if k %2 == 1:
                    tab[j, i, 0] = 255 - kolor1[0]
                    tab[j, i, 1] = 255 - kolor1[1]
                    tab[j, i, 2] = 255 - kolor1[2]
                else:
                    tab[j, i, 0] = 255 - kolor2[0]
                    tab[j, i, 1] = 255 - kolor2[1]
                    tab[j, i, 2] = 255 - kolor2[2]

    tab = tab*255
    return Image.fromarray(tab)

tab_pasy_negatyw_kolor = rysuj_pasy_kolorowe_neg(200, 200, 10, kolor1=[100, 230, 90], kolor2=[230, 20, 56])
tab_pasy_negatyw_kolor.save("obraz2_2N.jpg")
tab_pasy_negatyw_kolor.save("obraz2_2N.png")


# ZADANIE 3

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

inicjaly = Image.open("inicjaly1.bmp")
obraz3 = Image.fromarray(koloruj_obraz(inicjaly, [0, 191, 255]))
obraz3.save("obraz3.jpg")
obraz3.save("obraz3.png")

obraz4 = Image.fromarray(koloruj_obraz(inicjaly, [-5, 191, 255]))
obraz4.save("obraz4.jpg")
