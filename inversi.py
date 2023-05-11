import numpy as np                  #import library numpy untuk melakukan operasi array dan matematika
import imageio.v2 as imageio        #import library imageio untuk membaca gambar
import matplotlib.pyplot as plt     #import library matplotlib untuk menampilkan gambar

img = imageio.imread("keretaa.jpg")  #membaca gambar "keretaa.jpg" dengan menggunakan imageio dan menyimpannya di variabel img
img_height = img.shape[0]           #mendapatkan tinggi gambar dengan mengakses dimensi pertama dari array img
img_width = img.shape[1]            #mendapatkan lebar gambar dengan mengakses dimensi kedua dari array img
img_channel = img.shape[2]          #mendapatkan jumlah channel gambar dengan mengakses dimensi ketiga dari array img

img_inversi = np.zeros(img.shape, dtype=np.uint8)    #membuat array kosong dengan ukuran yang sama dengan img, tipe data unsigned integer 8 bit, untuk menyimpan gambar yang telah di-inversi

def inversi_grayscale(nilai):         #fungsi untuk melakukan inversi gambar grayscale
    for y in range(0, img_height):    #looping untuk setiap baris gambar
        for x in range(0, img_width): #looping untuk setiap kolom gambar
            red = img[y][x][0]       #mendapatkan nilai warna merah pada pixel (y,x)
            green = img[y][x][1]     #mendapatkan nilai warna hijau pada pixel (y,x)
            blue = img[y][x][2]      #mendapatkan nilai warna biru pada pixel (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  #menghitung nilai grayscale pada pixel (y,x) dengan rata-rata nilai warna RGB
            gray = nilai - gray      #melakukan inversi nilai grayscale dengan menggunakan parameter nilai
            img_inversi[y][x] = (gray, gray, gray)  #menyimpan nilai grayscale yang telah di-inversi pada array img_inversi

def inversi_rgb(nilai):              #fungsi untuk melakukan inversi gambar RGB
    for y in range(0, img_height):    #looping untuk setiap baris gambar
        for x in range(0, img_width): #looping untuk setiap kolom gambar
            red = img[y][x][0]       #mendapatkan nilai warna merah pada pixel (y,x)
            red = nilai - red        #melakukan inversi nilai warna merah dengan menggunakan parameter nilai
            green = img[y][x][1]     #mendapatkan nilai warna hijau pada pixel (y,x)
            green = nilai - green    #melakukan inversi nilai warna hijau dengan menggunakan parameter nilai
            blue = img[y][x][2]      #mendapatkan nilai warna biru pada pixel (y,x)
            blue = nilai - blue      #melakukan inversi nilai warna biru dengan menggunakan parameter nilai
            img_inversi[y][x] = (red, green, blue)  #menyimpan nilai RGB yang telah di-inversi pada array img_inversi

inversi_grayscale(255)              #melakukan inversi gambar grayscale dengan nilai 255 dan menyimpan hasilnya pada array img_inversi
plt.imshow(img_inversi)             #menampilkan gambar
plt.title("Inversi Grayscale")
plt.show()

inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()

img_log = np.zeros(img.shape, dtype=np.uint8)

def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray)

log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()


img_inlog = np.zeros(img.shape, dtype=np.uint8)

def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(255 - gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)

inlog(30)
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()


img_nthpower = np.zeros(img.shape, dtype=np.uint8)

def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()


img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)

def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()