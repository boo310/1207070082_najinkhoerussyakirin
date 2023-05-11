import numpy as np#manipulasi array
import imageio.v2 as imageio#mengolah gambar baca gambar
import matplotlib.pyplot as plt#ploting grafik

img = imageio.imread("gambar5.jpg")#variable img dengan nilai gambar "gambar5,jpg"
img_height = img.shape[0]#devinisi variable dengan nilai tinggi
img_width = img.shape[1]#devinisi variable dengan nilai lebar
img_channel = img.shape[2]#devinisi variable dengan nilai saluran warna

img_grayscale = np.zeros(img.shape, dtype=np.uint8)#array kosong dengan ukuran dan tipe data

for y in range(0, img_height):#loop untuk tiap pixel img untuk nilai y dari 0 sampai ujung gambar
    for x in range(0, img_width):#loop untuk tiap pixel img untuk nilai xdari 0 sampai ujung gambar
        red = img[y][x][0]# Untuk setiap piksel, nilai warna merah, hijau, dan biru diekstraksi menggunakan pengindeksan larik. 
        green = img[y][x][1]
        blue = img[y][x][2]
        gray = (int(red) + int(green) + int(blue)) / 3## Kemudian, nilai rata-rata dari nilai warna tersebut dihitung dan disimpan dalam variabel yang disebut abu-abu.
        img_grayscale[y][x] = (gray, gray, gray)#nilai keabuan dengan  warna abu abu abu

plt.imshow(img_grayscale)#menampilkan citra hasil pemerosesan
plt.title("Grayscale")#judul
plt.show()#menampilkan


hg = np.zeros((256))#Membuat array numpy 1 dimensi baru dengan ukuran 256 yang diisi dengan nilai 0, dan menyimpannya di variabel hg.

for x in range(0, 256):#Melakukan loop pada setiap nilai x dari 0 sampai 255 (inklusif) dan mengisi setiap elemen pada array hg dengan nilai 0. Ini dilakukan untuk memastikan bahwa array hg diinisialisasi dengan nilai 0 sebelum diisi dengan nilai histogram aktual.
    hg[x] = 0

for y in range(0, img_height):#Melakukan loop untuk setiap piksel dalam gambar grayscale img_grayscale untuk menghitung histogram dari gambar. Loop dimulai dari y = 0 sampai img_height-1, dan untuk setiap y, 
    for x in range(0, img_width):#loop x dari 0 sampai img_width-1. Untuk setiap piksel (y, x) dalam gambar, variabel gray diset dengan nilai intensitas warna abu-abu dari piksel tersebut. 
        gray = img_grayscale[y][x][0]#Kemudian nilai hg[gray] ditambah dengan 1, karena setiap kali intensitas warna abu-abu tertentu muncul, frekuensinya akan dihitung dan disimpan pada elemen yang sesuai di dalam array hg. 
        hg[gray] += 1

# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)#Membuat array numpy baru dengan fungsi linspace yang menghasilkan 100 angka dengan jarak yang sama antara 0 hingga 256. Array ini akan digunakan sebagai sumbu x pada plot histogram yang akan dibuat nanti. Array ini disimpan ke dalam variabel bins.
plt.hist(hg, bins, color="black", alpha=0.5)#Membuat plot histogram menggunakan fungsi hist dari library matplotlib. Input pertama adalah array yang akan diplot, yaitu variabel hg yang merupakan array yang berisi frekuensi kemunculan setiap nilai intensitas warna pada gambar. Input kedua adalah array bins yang sudah dibuat sebelumnya, yang menyatakan jarak antar bin pada histogram. Input ketiga adalah warna histogram yang diatur menjadi hitam (black) dan alpha (kejernihan) sebesar 0.5 untuk memberikan efek transparansi.
plt.title("Histogram")#judul
plt.show()#fungsi tampil


hgr = np.zeros((256))#Membuat array numpy  dimensi baru dengan ukuran 256 yang diisi dengan nilai 0, dan menyimpannya di variabel 
hgg = np.zeros((256))#Membuat array numpy  dimensi baru dengan ukuran 256 yang diisi dengan nilai 0, dan menyimpannya di variabel 
hgb = np.zeros((256))#Membuat array numpy  dimensi baru dengan ukuran 256 yang diisi dengan nilai 0, dan menyimpannya di variabel 
hgrgb = np.zeros((768))#Membuat array numpy  dimensi baru dengan ukuran 768 yang diisi dengan nilai 0, dan menyimpannya di variabel 

for x in range(0, 256):#x dalam rentang 0-256
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0

for x in range(0, 768):#x dalam rentang 0-768
    hgrgb[x] = 0

for x in range(0, 256):#x dalam rentang 0-256
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0

for x in range(0, 768):#x dalam rentang 0-768
    hgrgb[x] = 0

# th = int(256/64)
temp = [0]

for y in range(0, img_height):#looping untuk y 
    for x in range(0, img_width):#looping untuk x
        red = img[y][x][0]# Untuk setiap piksel, nilai warna merah, hijau, dan biru diekstraksi menggunakan pengindeksan larik. 
        green = img[y][x][1]
        blue = img[y][x][2]
        hgr[red] += 1#ditambah 1 di red
        hgg[green] += 1#ditambah 1 di green
        hgb[blue] += 1##ditambah 1 di blue

bins = np.linspace(0, 256, 100)#Baris ini membuat array bernama bins dengan menggunakan fungsi linspace dari NumPy. Linspace digunakan untuk membuat urutan bilangan dengan jarak yang sama antara dua titik yang diberikan, dan menghasilkan array dengan jumlah elemen sebanyak yang ditentukan pada parameter ketiga (dalam hal ini 100).
plt.hist(hgr, bins, color="red", alpha=0.5)#Setiap plt.hist menampilkan histogram menggunakan array frekuensi dan array bins. Parameter color digunakan untuk menentukan warna histogram, sedangkan alpha digunakan untuk menentukan kejernihan histogram
plt.title("Histogram Red")#judul
plt.show()#fungsi tampil

plt.hist(hgg, bins, color="green", alpha=0.5)#Setiap plt.hist menampilkan histogram menggunakan array frekuensi dan array bins. Parameter color digunakan untuk menentukan warna histogram, sedangkan alpha digunakan untuk menentukan kejernihan histogram
plt.title("Histogram Green")#judul
plt.show()#fungsi tampil

plt.hist(hgb, bins, color="blue", alpha=0.5)##Setiap plt.hist menampilkan histogram menggunakan array frekuensi dan array bins. Parameter color digunakan untuk menentukan warna histogram, sedangkan alpha digunakan untuk menentukan kejernihan histogram
plt.title("Histogram Blue")#judul
plt.show()#fungsi tampil


hgk = np.zeros((256))#Membuat array numpy  dimensi baru dengan ukuran 256 yang diisi dengan nilai 0, dan menyimpannya di variabel 
c = np.zeros((256))#Membuat array numpy  dimensi baru dengan ukuran 256 yang diisi dengan nilai 0, dan menyimpannya di variabel 

for x in range(0, 256):#looping untuk x
    hgk[x] = 0
    c[x] = 0

for y in range(0, img_height):#looping untuk y 
    for x in range(0, img_width):#looping untuk x 
        gray = img_grayscale[y][x][0]#untuk setiap pixel x dan y yang telah gray
        hgk[gray] += 1#pada hgk ditambah 1 nilai grey

c[0] = hgk[0]#Menetapkan elemen pertama dari array c sama dengan frekuensi kemunculan piksel dengan intensitas ke-0 pada histogram.
for x in range(1, 256):#Menghitung kumulatif frekuensi kemunculan piksel pada setiap intensitas dengan mengakumulasikan frekuensi sebelumnya 
    c[x] = c[x - 1] + hgk[x]#

hmaxk = c[255]#Menetapkan variabel hmaxk dengan nilai kumulatif frekuensi intensitas piksel maksimum (yaitu 255).

for x in range(0, 256):# Menormalisasi kumulatif frekuensi piksel pada setiap intensitas agar tidak melebihi nilai maksimum intensitas (yaitu 255) dan kemudian dikalikan dengan faktor 190 untuk meningkatkan kontras gambar.
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)#Setiap plt.hist menampilkan histogram menggunakan array frekuensi dan array bins. Parameter color digunakan untuk menentukan warna histogram, sedangkan alpha digunakan untuk menentukan kejernihan histogram
plt.title("Histogram Grayscale Kumulatif")#judul
plt.show()#fungsi tampil


hgh = np.zeros((256))#Inisialisasi array hgh, h, dan c dengan nol
h = np.zeros((256))#Lakukan loop untuk menghitung histogram grayscale pada array hgh
c = np.zeros((256))#Hitung nilai kumulatif dari histogram pada array h

for x in range(0, 256):#Normalisasi array h dengan membaginya dengan ukuran gambar
    hgh[x] = 0 
    h[x] = 0
    c[x] = 0

for y in range(0, img_height):#loop untuk mengakses setiap piksel pada sumbu y (tinggi) pada gambar.
    for x in range(0, img_width):# loop untuk mengakses setiap piksel pada sumbu x (lebar) pada gambar.
        gray = img_grayscale[y][x][0]#mengambil nilai intensitas warna grayscale pada piksel yang sedang diakses.
        hgh[gray] += 1# menambahkan frekuensi kemunculan intensitas warna grayscale pada array hgh.

h[0] = hgh[0]#menyalin nilai frekuensi munculnya intensitas warna grayscale dengan intensitas 0 ke dalam array h.
for x in range(1, 256):#loop untuk menghitung CDF dari intensitas warna grayscale dengan menggunakan nilai kumulatif dari frekuensi kemunculan intensitas warna grayscale.
    h[x] = h[x - 1] + hgh[x]#menghitung nilai kumulatif dari frekuensi munculnya intensitas warna grayscale pada setiap nilai intensitas.

for x in range(0, 256):#loop untuk menghitung probabilitas kemunculan intensitas warna grayscale.
    h[x] = h[x] / img_height / img_width#menghitung probabilitas kemunculan intensitas warna grayscale pada setiap nilai intensitas.

for x in range(0, 256):# loop untuk mengisi array hgh dengan nilai 0.
    hgh[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255#mengambil nilai intensitas warna grayscale pada piksel yang sedang diakses.
        hgh[int(gray)] += 1# menambahkan frekuensi kemunculan intensitas warna grayscale baru pada array hgh.

c[0] = hgh[0]#menyalin nilai frekuensi munculnya intensitas warna grayscale baru dengan intensitas 0 ke dalam array c.


for x in range(1, 256):#loop untuk menghitung nilai hequalisasi dari intensitas warna grayscale dengan menggunakan nilai kumulatif dari frekuensi kemunculan intensitas warna grayscale baru.
    c[x] = c[x - 1] + hgh[x]#menghitung nilai kumulatif dari frekuensi muncul


for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()