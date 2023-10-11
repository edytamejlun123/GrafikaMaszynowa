from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly1.bmp")  # wczytywanie obrazu

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", t_inicjaly.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka

# %%
# inicjaly.show()



# %%
def rysuj_ramke_w_obrazie(obraz, grub):  # rysuje pionowy pas grubości grub po lewej stronie oraz po prawej stronie
    tab_obraz = np.asarray(obraz) * 1  # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0

    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h - grub, h):
            tab_obraz[j][i] = 0

    tab = tab_obraz.astype(bool)  # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)


inicjaly_paski5 = rysuj_ramke_w_obrazie(inicjaly, 5)
inicjaly_paski10 = rysuj_ramke_w_obrazie(inicjaly, 10)
# %%
inicjaly_paski5.show()
inicjaly_paski10.show()

# %%
def rysuj_ramke(w, h, grub):  # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    tab[grub:h - grub, grub:w - grub] = 1  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
    tab1 = tab.astype(np.bool_)
    # return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    return tab1


tab = rysuj_ramke(120, 60, 8)
print("typ danych tablicy", tab.dtype)
print("rozmiar wyrazu tablicy:", tab.itemsize)
im_ramka = Image.fromarray(tab)
# im_ramka.show()


# %%
# def rysuj_pasy_poziome(w, h, grub):  # w, h   -  rozmiar obrazu
#     t = (h, w)  # rozmiar tablicy
#     tab = np.ones(t, dtype=np.uint8)
#     # jaki bedzie efekt, gdy np.ones zamienimy na np.zeros?
#     ile = int(h / grub)  # liczba pasów = 9 o grubości 10
#     for k in range(ile):  # uwaga k = 0,1,2,3,4,5,8   bez dziewiatki
#         for g in range(grub):
#             i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
#             for j in range(w):
#                 tab[i, j] = k % 2  # reszta z dzielenia przez dwa
#     tab = tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
#     return Image.fromarray(tab)  # tworzy obraz
#
#
# obraz = rysuj_pasy_poziome(100, 180, 18)
# obraz.show()


# %%
# def wstaw_obraz(w, h, m, n, obraz):  # w,h rozmiary nowego obrazu, m<=w,  n<=h (m,n miejsce wstawienia obrazu )
#     tab_obraz = np.asarray(obraz) * 1
#     h0, w0 = tab_obraz.shape
#     t = (h, w)  # rozmiar tablicy nowego obrazu
#     tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej jedynkami - biała
#     n_k = min(h, n + h0)  # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
#     m_k = min(w, m + w0)  # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
#     n_p = max(0, n)  # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w górę), to przycinamy
#     m_p = max(0, m)  # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w lewo), to przycinamy
#     print(n_k, m_k)
#     print(n_p, m_p)
#     for i in range(n_p, n_k):
#         for j in range(m_p, m_k):
#             tab[i][j] = tab_obraz[i - n][j - m]
#     tab = tab.astype(bool)  # zapisanie tablicy w typie bool (obrazy czarnobiałe)
#     return Image.fromarray(tab)
#
#
# wstaw_obraz(200, 100, 50, 20, inicjaly_paski).show()
