from PIL import Image
import numpy as np

obraz = Image.open("inicjaly.bmp")
# print("---- Zadanie 2. Informacje o obrazie: ")
# print(f"tryb: {obraz.mode}")
# print(f'format: {obraz.format}')
# print(f'rozmiar: {obraz.size}')


# -------------Zadanie 3 -----------------
# wczytywanie do tablicy
# dane_obrazka = np.asarray(obraz)
# print(dane_obrazka)

# tablica zerojedynkowa
# dane_obrazka1 = dane_obrazka * 1
# print(dane_obrazka1)

# np.savetxt('inicjaly.txt', dane_obrazka1, fmt='%d', delimiter=' ')

# inicjaly = np.loadtxt("inicjaly.txt", dtype=np.int_)
# inicjaly_text = open('inicjaly.txt', 'w')
# for rows in inicjaly:
#     for item in rows:
#         inicjaly_text.write(str(item) + ' ')
#     inicjaly_text.write('\n')
#
# inicjaly_text.close()

# print("---------------- informacje o tablicy obrazu----------------")
# print("typ danych tablicy:", dane_obrazka1.dtype)
# print("rozmiar tablicy:", dane_obrazka1.shape)
# print("liczba elementow:", dane_obrazka1.size)
# print("wymiar tablicy:", dane_obrazka1.ndim)
# print("rozmiar wyrazu tablicy:", dane_obrazka1.itemsize)

#
# pixel_1 = dane_obrazka[30, 50]
# pixel_2 = dane_obrazka[40, 90]
# pixel_3 = dane_obrazka[0, 99]
#
#
# print(f'wartosc pixel (50, 30): {pixel_1}')
# print(f'wartosc pixel (90,40): {pixel_2}')
# print(f'wartosc pixel (99,0): {pixel_3}')

# Zadanie 5
# dane_obrazka = np.asarray(obraz)
# inicjaly = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# print("---------------- porównanie tablicy z pliku txt oraz tablicy obrazka bmp----------------")
# print(f"typ danych tablicy txt: {inicjaly.dtype} typ danych tablicy obrazka: {dane_obrazka.dtype}")
# print(f"rozmiar tablicy txt: {inicjaly.shape}, rozmiar tablicy obrazka {dane_obrazka.shape}")
# print(f"liczba elementow tablicy txt: {inicjaly.size}, liczba elementów tablicy obrazka {dane_obrazka.size}")
# print(f"wymiar tablicy txt: {inicjaly.ndim}, wymiar tablicy obrazka {dane_obrazka.ndim}")
# print(f"rozmiar wyrazu tablicy txt: {inicjaly.itemsize}, rozmiar wyrazu tablicy obrazka {dane_obrazka.itemsize}")


#  Zadanie 6
dane_obrazka = np.asarray(obraz)
inicjaly = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print("---------------- porównanie tablicy z pliku txt oraz tablicy obrazka bmp----------------")
print(f"typ danych tablicy txt: {inicjaly.dtype} typ danych tablicy obrazka: {dane_obrazka.dtype}")
print(f"rozmiar tablicy txt: {inicjaly.shape}, rozmiar tablicy obrazka {dane_obrazka.shape}")
print(f"liczba elementow tablicy txt: {inicjaly.size}, liczba elementów tablicy obrazka {dane_obrazka.size}")
print(f"wymiar tablicy txt: {inicjaly.ndim}, wymiar tablicy obrazka {dane_obrazka.ndim}")
print(f"rozmiar wyrazu tablicy txt: {inicjaly.itemsize}, rozmiar wyrazu tablicy obrazka {dane_obrazka.itemsize}")

ob_d = Image.fromarray(inicjaly)  # tworzenie obrazu z tablicy dane_obrazka (typ uint8)
ob_d.show()

ob_d1 = Image.fromarray(dane_obrazka)
ob_d1.show()
