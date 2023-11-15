from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt

# # Zadanie1
im1 = Image.open("obraz.jpg").convert("RGB")
# # im1.show()
#
# # Zadanie 2
# # a
# T = np.array(im1)
#
# t_r = T[:, :, 0]
# im_r = Image.fromarray(t_r)
#
#
# t_g = T[:, :, 1]
# im_g = Image.fromarray(t_g)
#
#
# t_b = T[:, :, 2]
# im_b = Image.fromarray(t_b)
#
# # b
# im2 = Image.merge("RGB", (im_r, im_g, im_b))
# porownanie = ImageChops.difference(image1 = im1, image2 = im2)
#
# # if porownanie.getbbox():
# #     porownanie.save("roznica.jpg")
# #     print("roznice przedstawione są w obrazie 'roznica.jpg'")
# # else:
# #     print("obrazy są identyczne.")
#
# # c
# plt.figure(figsize=(32, 16))
# plt.subplot(2, 2, 1) # ile obrazów w pionie, ile w poziomie, numer obrazu
# plt.imshow(im1)
# plt.axis('off')
# plt.subplot(2, 2, 2)
# plt.imshow(im2)
# plt.axis('off')
# plt.subplot(2, 2, 3)
# plt.imshow(porownanie)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig1.png')
# # plt.show()

# # Zadanie 3

# Pobierz kanały R, G, B obrazu im1
im1_r, im1_g, im1_b = im1.split()

# Utwórz obraz im3 przez dowolną nieidentycznościową
# permutację kanałów
channel_permutation = [im1_g, im1_b, im1_r]
im3 = Image.merge("RGB", tuple(channel_permutation))

# a. Zapisz im3 w formacie JPG i PNG
im3.save("im3.jpg", "JPEG")
im3.save("im3.png", "PNG")

# b. Wczytaj zapisane obrazy
im3_jpg = Image.open("im3.jpg")
im3_png = Image.open("im3.png")

# c. Porównaj obrazy i zapisz wynik porównania
diff_jpg = ImageChops.difference(im3_jpg, im3)
diff_png = ImageChops.difference(im3_png, im3)

# Zapisz obrazy z różnicami
diff_jpg.save("diff_jpg.jpg")
diff_png.save("diff_png.png")

# Umieść obrazy na jednej figurze i wyświetl
fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(im3)
axes[0].set_title('im3')
axes[1].imshow(im3_jpg)
axes[1].set_title('im3.jpg')
axes[2].imshow(im3_png)
axes[2].set_title('im3.png')
axes[3].imshow(diff_jpg, cmap='gray')
axes[3].set_title('Difference (JPG)')
plt.savefig('fig2.png')
# plt.show()

# Sprawdź, czy obrazy są identyczne
are_images_identical_jpg = np.array_equal(np.array(im3), np.array(im3_jpg))
are_images_identical_png = np.array_equal(np.array(im3), np.array(im3_png))

print(f"Czy obrazy im3 i im3.jpg są identyczne: {are_images_identical_jpg}")
print(f"Czy obrazy im3 i im3.png są identyczne: {are_images_identical_png}")

# # Zadanie 5
# gray_array = np.random.randint(0, 256, size=(im1.height, im1.width), dtype=np.uint8)
#
# # Utwórz obraz im4 z tablicy odcieni szarości
# im4 = Image.fromarray(gray_array, mode='L')
#
# # a. Utwórz 3 różne obrazy przez podmienianie jednego kanału obrazu wejściowego obrazem im4
# im1_r, im1_g, im1_b = im1.split()
# im1_with_im4_r = Image.merge('RGB', (im4, im1_g, im1_b))
# im1_with_im4_g = Image.merge('RGB', (im1_r, im4, im1_b))
# im1_with_im4_b = Image.merge('RGB', (im1_r, im1_g, im4))
#
# # b. Przedstaw wszystkie 3 obrazy na jednej figurze plt i zapisz jako fig4.png
# fig, axes = plt.subplots(1, 4, figsize=(15, 5))
# axes[0].imshow(im1)
# axes[0].set_title('Original')
# axes[1].imshow(im1_with_im4_r)
# axes[1].set_title('odcień czerwonego z im4')
# axes[2].imshow(im1_with_im4_g)
# axes[2].set_title('odcień zielonego z im4')
# axes[3].imshow(im1_with_im4_b)
# axes[3].set_title('odcień niebieskiego z im4')
# plt.savefig('fig4.png')
# plt.show()
#
#
# # Zadanie 6
#
# # trzy czarno-białe obrazy
# size = (200, 200)  # rozmiar obrazów
# shape1 = np.zeros(size, dtype=np.uint8)
# shape2 = np.zeros(size, dtype=np.uint8)
# shape3 = np.zeros(size, dtype=np.uint8)
#
# # kształty na obrazach
# shape1[50:150, 50:150] = 255
# shape2[75:175, 75:175] = 255
# shape3[100:200, 100:200] = 255
#
# # a. Dostosuj obrazy jako kanały RGB
# im_rgb1 = Image.merge('RGB', (Image.fromarray(shape1), Image.fromarray(shape2), Image.fromarray(shape3)))
# im_rgb2 = Image.merge('RGB', (Image.fromarray(shape2), Image.fromarray(shape3), Image.fromarray(shape1)))
# im_rgb3 = Image.merge('RGB', (Image.fromarray(shape3), Image.fromarray(shape1), Image.fromarray(shape2)))
#
# # b. Stwórz obrazy RGB z wszystkich permutacji kanałów
# fig, axes = plt.subplots(1, 4, figsize=(15, 5))
# axes[0].imshow(im_rgb1)
# axes[0].set_title('RGB (Shape1, Shape2, Shape3)')
# axes[1].imshow(im_rgb2)
# axes[1].set_title('RGB (Shape2, Shape3, Shape1)')
# axes[2].imshow(im_rgb3)
# axes[2].set_title('RGB (Shape3, Shape1, Shape2)')
#
# # Permutacja kanałów RGB
# im_rgb_permuted = Image.merge('RGB', (Image.fromarray(shape2), Image.fromarray(shape1), Image.fromarray(shape3)))
# axes[3].imshow(im_rgb_permuted)
# axes[3].set_title('RGB (Shape2, Shape1, Shape3)')
#
# # Zapisz figurę jako fig5.png
# plt.savefig('fig5.png')
# plt.show()
#
# # Zadanie 7
# import numpy as np
# from PIL import Image
#
# def czy_rowne(oryginal, test):
#
#     ssim_wartosc, _ = ssim(oryginal, test, full=True)
#     return ssim_wartosc
#
# # Przykład użycia:
# obraz_oryginalny = np.array(im1)
# obraz_testowy = np.array(im2)
#
# ssim_wartosc = czy_rowne(obraz_oryginalny, obraz_testowy)
# print(f"SSIM: {ssim_wartosc}")