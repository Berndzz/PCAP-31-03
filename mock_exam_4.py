# 1. Choose the correct output of the following code: -
# x = '10' - '20'
# print(x)
# answer : TypeError (TypeError: unsupported operand type(s) for -: 'str' and 'str')


# 2. Choose the correct output of the following code: -
# def LetterWord(*inp):
#     print(type(inp))


# LetterWord('P', 'y', 't', 'h', 'o', 'n')
# answer: <class 'tuple'>

'''
breakdown
Fungsi LetterWord adalah sebuah fungsi Python yang menerima sejumlah 
argumen posisional. Argumen-argumen ini dikumpulkan ke dalam parameter 
*inp, yang berarti argumen-argumen ini akan dibuat menjadi sebuah tuple 
dalam bentuk inp.
Pada contoh yang diberikan, saat Anda memanggil LetterWord('P', 'y', 't', 'h', 'o', 'n'),
Anda memberikan 6 argumen berupa karakter (string tunggal) ke dalam fungsi.
Argumen-argumen ini akan dikumpulkan menjadi sebuah tuple, sehingga inp 
akan menjadi tuple yang berisi karakter-karakter tersebut.
Hasil cetak print(type(inp)) akan mencetak tipe data dari inp. Karena inp 
adalah sebuah tuple yang berisi karakter, hasil cetaknya adalah <class 'tuple'>, 
yang merupakan tipe data dari inp. Jadi, jawabannya adalah <class 'tuple'>.


Penggunaan tanda asterisk * sebelum parameter dalam deklarasi fungsi, 
seperti *inp, adalah cara untuk mengumpulkan sejumlah argumen posisional 
yang dilewatkan ke fungsi ke dalam sebuah tuple. Ini memungkinkan Anda 
untuk mengatasi sejumlah argumen yang bervariasi tanpa harus menyebutkan 
satu per satu.
Jadi, ketika Anda memanggil fungsi LetterWord('P', 'y', 't', 'h', 'o', 'n'),
semua karakter 'P', 'y', 't', 'h', 'o', dan 'n' dikumpulkan menjadi sebuah
tuple dengan nama inp. Sehingga, inp akan menjadi ('P', 'y', 't', 'h', 'o', 'n').
Hasil dari type(inp) adalah <class 'tuple'> karena inp adalah sebuah tuple. 
Artinya, inp adalah sebuah objek yang tipe datanya adalah tuple, dan
itulah yang dicetak oleh print(type(inp)).


'''


# 3.Choose the correct output of the following code: -
List = [1, 2, 4, 5, 6, 7, 8]
for i in range(0, len(List)):
    if(List[i] % 5 == 0):
        List.append(9)
    if((len(List)-1) == i):  # if ((len(List)-1) == i):, itu memeriksa apakah i adalah indeks terakhir dari List
        print(List[i] + List[2])

# answer: No Output


# 4. Choose the correct output of the following code: -
# List = [1, 2, 4, 5, 6, 7, 8]
# for i in List:
#     if(i % 5 == 0):
#         List.append(9)
#     if((List[len(List)-1]) == i):
#         print(i + List[2])

# answer : 13


# 5. Which among the following line of code will raise an error?
# class BioData:
#     def __init__(self, x, y):
#         self.name = x
#         print("Name : ", self.name)
#         self.age = y print("Age : ", self.age)


# BioData("Emma", 23)
# answer : line4


# 6. Choose the correct output of the following code: -
# class Circle:
#     def __init__(self, x):
#         self.__radius = x


# class Sphere(Circle):
#     def volume(self):
#         r = self.__radius  # solution : self._Circle__radius
#         print((4/3)*3.14*r*r*r)


# Sphere(5).volume()
# answer: Error
# (AttributeError: 'Sphere' object has no
# attribute '_Sphere__radius'. Did you mean: '_Circle__radius'?)


'''
breakdown
Kode yang diberikan mencoba mendefinisikan dua kelas, yaitu 
Circle dan Sphere, yang merupakan contoh pewarisan dalam 
pemrograman berorientasi objek. Sphere adalah kelas anak 
(subkelas) dari Circle, yang berarti Sphere mewarisi sifat 
dan metode dari Circle.
Namun, dalam kode ini, ada masalah yang perlu diperhatikan:
Kelas Circle memiliki konstruktor __init__ yang menerima satu
parameter x dan menginisialisasi atribut __radius dengan nilai x. 
Atribut __radius adalah atribut yang bersifat pribadi karena 
diawali dengan garis bawah ganda (__), yang berarti seharusnya 
hanya dapat diakses secara internal di dalam kelas Circle.
Kelas Sphere mencoba untuk mengakses atribut __radius dari 
kelas induk Circle melalui self.__radius. Namun, ini akan 
menyebabkan kesalahan karena atribut __radius dalam Circle 
adalah atribut pribadi dan seharusnya tidak dapat diakses dari 
luar kelas.
Kode tersebut akan menghasilkan kesalahan yang disebut 
"AttributeError" karena mencoba mengakses atribut pribadi 
yang tidak ada dalam kelas Sphere. Sehingga, jawaban yang
benar adalah "Error".
Untuk mengatasi masalah ini, Anda dapat mengubah atribut 
__radius dalam Circle menjadi atribut yang dapat diakses 
secara publik atau melalui metode-metode publik dalam kelas 
`Circle.
'''

# # 7. Choose the correct output of the following code: -
# num = 65
# for i in range(0, 5):
#     for j in range(0, i+1):
#         ch = chr(num)
#         print(ch, end=" ")
#     num = num + 1
#     print(" ")

# answer:
# A
# B B
# C C C
# D D D D
# E E E E E


# 8. What will be the text show in the sys.txt file after the execution of the following code: -
# file = open("sys.txt", 'wb+')
# file.write(bytearray("JAVA", "ASCII"))
# file.close()
# answer : JAVA


# 9. Consider that the below code is written inside 'test.py' file.
# print(__name__)
# print(type(__name__))  # __name__ itu tipenya string

# answer:
# __main__
# <class 'str'>


# 10. Choose the correct output of the following code: -
D = {1: "First", 2: "Second", 3: "Third", 4: "Four"}
if(D[4] != None):
    del D[4]
for i in D:
    print(i, end=" ")

# answer: 1 2 3


'''
breakdown

Kode yang Anda berikan menciptakan sebuah kamus (dictionary)
yang disebut D dengan beberapa pasangan kunci-nilai. Kemudian,
kode tersebut melakukan beberapa operasi pada kamus ini. Mari 
kita bahas langkah demi langkah:
Kamus D dibuat dengan empat pasangan kunci-nilai:
Kunci 1 memiliki nilai "First"
Kunci 2 memiliki nilai "Second"
Kunci 3 memiliki nilai "Third"
Kunci 4 memiliki nilai "Four"
Kode tersebut melakukan pemeriksaan dengan if(D[4] != None):.
Ini memeriksa apakah nilai yang terkait dengan kunci 4 dalam 
kamus D tidak sama dengan None. Karena ada nilai yang terkait
(nilai adalah "Four"), maka pernyataan dalam blok if dijalankan.
Di dalam blok if, perintah del D[4] digunakan untuk menghapus 
elemen dengan kunci 4 dari kamus D. Setelah perintah ini 
dijalankan, kunci 4 dan nilainya ("Four") dihapus dari kamus.
Kemudian, perulangan for i in D: digunakan untuk mengiterasi
melalui kunci-kunci yang tersisa dalam kamus D setelah 
penghapusan. Dalam setiap iterasi, nilai dari kunci saat
ini dicetak dengan menggunakan print(i, end=" "). Karena 
kunci-kunci yang tersisa adalah 1, 2, dan 3, maka output 
yang dihasilkan adalah "1 2 3".

'''
