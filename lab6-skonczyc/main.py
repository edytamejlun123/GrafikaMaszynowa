from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# ZADANIE 1

obraz = Image.open("obraz.png")
inicjaly = Image.open("inicjaly.bmp")


# ZADANIE 2

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]


def rozjasnij_obraz_z_maska(obraz, maska, m, n, a, b, c):  # w miejscu m, n zmienia tylko te pixele,
    # które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1



w_obraz, h_obraz = obraz.size
w_inicjaly, h_inicjaly = inicjaly.size
m = w_obraz-w_inicjaly
n = h_obraz-h_inicjaly

rozjasnij_obraz_z_maska(obraz, inicjaly, m, n, 255, 0, 0).show()
# zamienić rozjaśnij obraz na wstaw inicjały;

