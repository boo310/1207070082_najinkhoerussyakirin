?import numpy as np #Mengimport library numpy untuk manipulasi array dan melakukan alias dengan np.  
import imageio.v2 as imageio#Mengimport imageio versi 2 untuk membaca gambar dan melakukan alias dengan imageio.
import matplotlib.pyplot as plt#Mengimport library matplotlib.pyplot untuk plot grafik dan melakukan alias dengan plt.

img = imageio.imread("gambar4.jpg")#Mendefinisikan variabel img dengan nilai dari membaca gambar "gambar4.jpg" menggunakan imageio.imread().

img_height = img.shape[0]#mendefinisikan variabel img_height dengan nilai tinggi
img_width = img.shape[1]#mendefinisikan variabel img_widht dengan nilai lebar
img_channel = img.shape[2]#mendefinisikan variabel img_chanel dengan nilai jumlah saluran warna
img_type = img.dtype#mendefinisikan variabel img_type dengan nilai tipe data gambar

img_flip_horizontal = np.zeros(img.shape, img_type)#Membuat array kosong img_flip_horizontal dengan ukuran dan tipe data yang sama dengan gambar img.
img_flip_vertical = np.zeros(img.shape, img_type)#Membuat ARRARY img_flip_vertical dengan ukuran dan tipe data yang sama dengan gambar img.

for y in range(0, img_height):5
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]

for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]

plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()