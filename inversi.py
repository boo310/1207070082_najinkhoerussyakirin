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
plt.title("Inversi Grayscale")#judul 

plt.show()#fungsi plot

inversi_rgb(255)#melakukan inversi gambar grayscale dengan nilai 255 dan menyimpan hasilnya pada array img_inversi
plt.imshow(img_inversi)#menampilkan gambar
plt.title("Inversi RGB")#judul
plt.show()#fungsi plot

img_log = np.zeros(img.shape, dtype=np.uint8)#array kosong untuk ukuran gambar dan tipe gambar

def log(c):# mendefinisikan sebuah fungsi bernama log dengan satu parameter c.
    for y in range(0, img_height):#loop tinggi gambar
        for x in range(0, img_width):#loop lebar gambar
            red = img[y][x][0]#pixel merah
            green = img[y][x][1]#pixel hijau
            blue = img[y][x][2]#pixel biru
            gray = (int(red) + int(green) + int(blue)) / 3#rata-rata rjb di bagi 3 jadi grey
            gray = int(c * np.log(gray + 1))#Menghitung logaritma natural dari nilai keabuan + 1, kemudian mengalikan dengan "c" dan mengkonversi hasilnya menjadi bilangan bulat.
            if gray > 255:#jika grey 255 lebih dari 255 maka 255
                gray = 255
            if gray < 0:#jika grey kurang dari 0 maka 0
                gray = 0
            img_log[y][x] = (gray, gray, gray)#Menetapkan piksel pada koordinat (x,y) pada gambar menjadi nilai keabuan yang baru (gray) untuk masing-masing komponen warna (merah, hijau, dan biru).

log(30)#log diberi nilai 30 
plt.imshow(img_log)#menampilkan gambar
plt.title("Log")#judul gambar
plt.show()#fungsi tampil


img_inlog = np.zeros(img.shape, dtype=np.uint8)#array kosong untuk ukuran dan tipe

def inlog(c):#definisi inlog dengan c
    for y in range(0, img_height):#loop y
        for x in range(0, img_width):#loop x
            red = img[y][x][0]#pixel merah
            green = img[y][x][1]#pixel hijau
            blue = img[y][x][2]#pixel biru
            gray = (int(red) + int(green) + int(blue)) / 3#rata-rata rjb di bagi 3 jadi grey
            gray = int(c * np.log(255 - gray + 1))#Menghitung logaritma natural dari nilai keabuan + 1, kemudian mengalikan dengan "c" dan mengkonversi hasilnya menjadi bilangan bulat.
            if gray > 255:#jika grey 255 lebih dari 255 maka 255
                gray = 255
            if gray < 0:#jika grey kurang dari 0 maka 0
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)#Menetapkan piksel pada koordinat (x,y) pada gambar menjadi nilai keabuan yang baru (gray) untuk masing-masing komponen warna (merah, hijau, dan biru).

inlog(30)#log diberi nilai 30 
plt.imshow(img_inlog)#menampilkan gambar
plt.title("Inversi & Log")#judul gambar
plt.show()#fungsi tampil


img_nthpower = np.zeros(img.shape, dtype=np.uint8)#array kosong untuk ukuran dan tipe


def nthpower(c, y):#mendefinisikan fungsi dengan nama "nthpower" yang memiliki 2 parameter yaitu "c" dan "y"
    thc = c / 100# variabel "thc" diinisialisasi dengan nilai "c" dibagi 100
    thy = y / 100# variabel "thy" diinisialisasi dengan nilai "y" dibagi 100
    for y in range(0, img_height):#melakukan iterasi pada setiap pixel pada sumbu y (tinggi) dari gambar
        for x in range(0, img_width):#melakukan iterasi pada setiap pixel pada sumbu x (lebar) dari gambar
            red = img[y][x][0]#variabel "red" diinisialisasi dengan nilai piksel warna merah pada koordinat (x, y) dari gambar
            green = img[y][x][1]#variabel "green" diinisialisasi dengan nilai piksel warna hijau pada koordinat (x, y) dari gambar
            blue = img[y][x][2]#variabel "blue" diinisialisasi dengan nilai piksel warna biru pada koordinat (x, y) dari gambar
            gray = (int(red) + int(green) + int(blue)) / 3#variabel "gray" diinisialisasi dengan rata-rata dari nilai piksel warna merah, hijau, dan biru pada koordinat (x, y) dari gambar
            gray = int(thc * pow(gray, thy))#variabel "gray" diubah menjadi nilai dari "thc" dikalikan dengan "gray" pangkat "thy"
            if gray > 255:#jika grey 255 lebih dari 255 maka 255
                gray = 255
            if gray < 0:#jika grey kurang dari 0 maka 0
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)#Menetapkan piksel pada koordinat (x,y) pada gambar menjadi nilai keabuan yang baru (gray) untuk masing-masing komponen warna (merah, hijau, dan biru).


nthpower(50, 100)#Memanggil fungsi nthpower dengan parameter c=50 dan y=100.
plt.imshow(img_nthpower)#tampil gambar
plt.title("Nth Power")#judul
plt.show()#fungsi tampil


img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)#array kosong untuk ukuran dan tipe


def nthrootpower(c, y):#mendefinisikan fungsi dengan nama "nthpower" yang memiliki 2 parameter yaitu "c" dan "y"
    thc = c / 100# variabel "thc" diinisialisasi dengan nilai "c" dibagi 100
    thy = y / 100# variabel "thy" diinisialisasi dengan nilai "y" dibagi 100
    for y in range(0, img_height):##melakukan iterasi pada setiap pixel pada sumbu y (tinggi) dari gambar
        for x in range(0, img_width):#melakukan iterasi pada setiap pixel pada sumbu x) dari gambar
            red = img[y][x][0]#pixel merah
            green = img[y][x][1]#pixel hijau
            blue = img[y][x][2]#pixel biru
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

nthrootpower(50, 100)#Memanggil fungsi nthpower dengan parameter c=50 dan y=100.
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()