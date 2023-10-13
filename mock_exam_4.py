import math
import test1
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
# D = {1: "First", 2: "Second", 3: "Third", 4: "Four"}
# if(D[4] != None):
#     del D[4]
# for i in D: # iterasi hanya key saja
#     print(i, end=" ")

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

# 11. Choose the correct output of the following code: -
# D = {1: "First", 2: "Second", 3: "Third", 4: "Four"}
# if(D[4] != None):
#     del D[4]
# for i in D.items():  # iterasi seluruh key dan value
#     print(i, end=" ")

# answer: (1, 'First') (2, 'Second') (3, 'Third')


'''
breakdown
Kode ini hampir sama dengan kode sebelumnya, kecuali ada 
sedikit perbedaan dalam perulangan for. Mari kita bahas kode 
ini langkah demi langkah:
Kamus (dictionary) D dibuat dengan empat pasangan kunci-nilai:
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
Selanjutnya, kita memiliki perulangan for i in D.items(). 
Ini mengiterasi melalui seluruh pasangan kunci-nilai (item) 
dalam kamus D. Di setiap iterasi, i akan menjadi pasangan 
kunci-nilai tersebut.
Kemudian, kita mencetak pasangan kunci-nilai i, tetapi 
dengan end=" " yang akan menghasilkan spasi di antara 
setiap pasangan kunci-nilai yang dicetak. Hasilnya 
adalah item kamus yang dicetak dalam satu baris dengan 
spasi di antara mereka.
'''

# 12. Consider that the below code is written inside 'test1.py' file.
# print("print of test1: ", __name__)

# Consider that the below code is writen inside 'test2.py' file.
# print("print of test2: ", __name__)
# Choose the correct output when the test2.py file is executed.

# answer:
# print of test1:  test1
# print of test2:  __main__


'''
breakdown
Ketika Anda menjalankan 'test2.py', inilah yang terjadi:
'test2.py' dijalankan.
Saat 'test2.py' mengimpor 'test1.py' dengan perintah import
test1, 'test1.py' juga dijalankan. Ini karena ketika suatu 
modul diimpor, kode di dalamnya dijalankan.
Di dalam 'test1.py', perintah print("print of test1: ", __name__) 
dijalankan, dan nilai dari __name__ pada saat itu adalah "test1". 
Nilai ini ditampilkan sebagai "print of test1: test1".
Kemudian, 'test1.py' selesai dieksekusi dan kendali kembali ke 
'test2.py'.
Di dalam 'test2.py', perintah print("print of test2: ", __name__) 
dijalankan, dan nilai dari __name__ pada saat itu adalah "main". Nilai ini ditampilkan sebagai "print of test2: main".
'''


# 13. Choose the correct output of the following code: -
# print(math.factorial('4'))
# answer : TypeError (TypeError: 'str' object cannot be interpreted as an integer)


# 14. Choose the correct output of the following code: -
# def SUM(*x):
#     result = 0
#     for i in range(len(x)):
#         result = result + int(x[i])
#     print(result)


# SUM(5, 4, 1, 2, 3)
# answer : 15

'''
breakdown
Iterasi pertama: result = 0 + 5 (elemen pertama dari x)
Iterasi kedua: result = 5 + 4 (elemen kedua dari x)
Iterasi ketiga: result = 9 + 1 (elemen ketiga dari x)
Iterasi keempat: result = 10 + 2 (elemen keempat dari x)
Iterasi kelima: result = 12 + 3 (elemen kelima dari x)
'''


# 15. If the file 'sys.text' alreadu contain the text "JAVA" then what will be printed in the console after the execution of the following code: -
# file = open("sys.txt", 'rb')
# print(file.read())
# file.close()

# answer : b'JAVA'

'''
breakdown
Kode yang diberikan bertujuan untuk membuka file "sys.txt" 
dalam mode membaca biner ('rb'), kemudian membaca isi file
dan mencetaknya ke konsol. Jawaban yang benar adalah "b'JAVA'"
karena file "sys.txt" berisi teks "JAVA."
Mari kita jelaskan langkah-langkahnya secara detail:
file = open("sys.txt", 'rb'): Kode ini membuka file "sys.txt" 
dalam mode "rb" (read binary), yang berarti membaca file dalam 
bentuk biner. File "sys.txt" harus sudah ada sebelumnya, dan 
kode ini membuka file tersebut.
print(file.read()): Setelah membuka file, kode ini menggunakan
metode read() untuk membaca seluruh isi file. Hasilnya adalah 
byte-string (b'JAVA') yang mencerminkan isi file dalam bentuk
biner.
file.close(): Kode ini menutup file setelah selesai membacanya.
Hasil yang aka
'''


# 16. Choose the correct output of the following code: -
# print("SpaceX : %1s" % ("Tesla"))
# print("SpaceX : %4s" % ("Tesla"))
# print("SpaceX : %10s" % ("Tesla"))

# answer :
# SpaceX : Tesla
# SpaceX : Tesla
# SpaceX :      Tesla


'''
breakdown
Kode yang Anda berikan mencetak string dengan format 
tertentu menggunakan notasi % yang digunakan dalam
pemformatan string. Format %Ns digunakan untuk memformat 
string dengan lebar total sebanyak N karakter. Jika panjang 
string yang diberikan kurang dari N, maka spasi akan digunakan
untuk mengisi sisa lebar. Mari kita bahas setiap baris kode 
secara terperinci:
print("SpaceX : %1s" % ("Tesla")): Pada baris ini, kita 
menggunakan %1s untuk memformat string "Tesla" dengan lebar 
total sebanyak 1 karakter. Namun, "Tesla" memiliki lebih 
dari 1 karakter, jadi lebar ini tidak akan cukup. Hasilnya
adalah "Tesla" dicetak tanpa perubahan.
print("SpaceX : %4s" % ("Tesla")): Di sini, kita 
menggunakan %4s untuk memformat string "Tesla" dengan 
lebar total sebanyak 4 karakter. "Tesla" memiliki 5 karakter,
jadi spasi akan digunakan untuk mengisi sisa lebar. 
Hasilnya adalah "Tesla" dicetak dengan satu spasi sebelumnya 
untuk membuat total lebar mencapai 4 karakter.
print("SpaceX : %10s" % ("Tesla")): Pada baris ini, kita 
menggunakan %10s untuk memformat string "Tesla" dengan lebar 
total sebanyak 10 karakter. "Tesla" memiliki 5 karakter, 
sehingga akan ada 5 spasi yang digunakan untuk mengisi sisa 
lebar. Hasilnya adalah "Tesla" dicetak dengan lima spasi 
sebelumnya untuk mencapai total lebar 10 karakter.

Perhatikan bahwa %Ns adalah salah satu cara untuk 
memformat string dalam Python, dan ada juga cara-cara 
lain seperti f-strings (diperkenalkan dalam Python 3.6) 
atau metode str.format().

Untuk menghasilkan karakter tab dalam format string, 
Anda bisa menggunakan karakter escape \t.

'''


# 17. Choose the correct output of the following code: -
# print(~10)
# print(~~10)

# answer:
# -11
# 10


'''
breakdown
Kode yang Anda berikan menggunakan operator bitwise NOT (~) 
pada bilangan 10 dan kemudian operator bitwise NOT ganda (~~) 
pada bilangan 10. Mari kita jelaskan hasil dari masing-masing 
ekspresi:
print(~10): Pada ekspresi ini, operator bitwise NOT (~)
digunakan pada bilangan 10. Operator bitwise NOT akan 
mengambil representasi biner dari bilangan tersebut, 
kemudian membalik setiap bitnya (0 menjadi 1 dan 1 menjadi 0).
Hasilnya adalah nilai yang terbalik dalam representasi biner. 
Setelah itu, nilai tersebut dikonversi kembali ke bentuk desimal. 
Hasilnya adalah -11.
Proses:
Representasi biner dari 10 adalah 00001010.
Menggunakan bitwise NOT, kita mendapatkan 11110101.
Ini adalah representasi biner dari -11 dalam notasi complement
dua.
Dikonversi kembali ke desimal, hasilnya adalah -11.
print(~~10): Pada ekspresi ini, operator bitwise NOT ganda 
(~~) digunakan pada bilangan 10. Operator bitwise NOT ganda 
(~~) adalah operasi yang menghasilkan bilangan asli kembali 
setelah dua operasi bitwise NOT. Dengan kata lain, ~~x adalah 
setara dengan x untuk bilangan bulat x. Sehingga, ekspresi ini 
akan menghasilkan 10.

example : 
-5 = (1 * -2^7) + (1 * 2^6) + (1 * 2^5) + (1 * 2^4) + (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
   = (-128) + 64 + 32 + 16 + 8 + 0 + 2 + 1
   = -5
'''


# 18. Choose the correct statement regarding a constructor in python.
# answer:
# A Constructor can return the None value.
# A Constructor can return no value.

'''
Dalam bahasa pemrograman Python, konstruktor, yang biasanya 
didefinisikan dalam metode __init__, tidak mengembalikan nilai 
secara eksplisit. Ini berarti bahwa konstruktor secara default
mengembalikan None (tidak mengembalikan apa-apa). Ini adalah 
perilaku standar dalam Python untuk konstruktor.
'''


# 19. Choose the correcct output of the following code: -
# a = "Tesla"
# b = "electric"
# c = "makes"
# d = "cars"
# str = '{0}{2}{1}{3}'.format(a, b, c, d)
# print(str)

# answer: Teslamakeselectriccars

'''
breakdown
Kode di atas menggunakan metode str.format() untuk 
menggabungkan string a, b, c, dan d dalam urutan tertentu.
Hasil akhirnya adalah string str yang dihasilkan dengan 
menggabungkan string tersebut sesuai dengan urutan yang di 
tentukan dalam metode format().

Di dalam metode format(), Anda menggunakan kurung kurawal {} 
dengan indeks yang menunjukkan urutan argumen yang akan 
dimasukkan ke dalam string. Indeks dimulai dari 0.

{0} mengacu pada argumen pertama, yaitu string a yang berisi "Tesla".
{2} mengacu pada argumen ketiga, yaitu string c yang berisi "makes".
{1} mengacu pada argumen kedua, yaitu string b yang berisi "electric".
{3} mengacu pada argumen keempat, yaitu string d yang berisi "cars".
Menggabungkan mereka sesuai dengan urutan indeks tersebut 
menghasilkan string "Teslamakeselectriccars".

'''


# 20. What will be printed in the console when the first number entered is '20' and the second number
# entered is '10'

a = input("Enter first number: ")
b = input("Enter second number: ")
print(a+b)

# answer: 2010

# 21. Choose the correct output of the following code: - 
x = 'Python Java'
for i in x:
    if(i==" "): print()
    else: print(i,end="")
# answer:
# Python
# Java

# 22. Choose the correct output of the following code: - 
for i in range(0,5):
    for j in range(0,i+1):
        print('* ', end="")
    print(" ")
# answer:
# *  
# * *  
# * * *  
# * * * *  
# * * * * *


# 23. Choose the correct output of the following code: - 
a = Orange
print(a)
# answer:
# NameError: name 'Orange' is not defined



# 24. Choose the correct output of the following code: - 
x = (9,5,1)
x.append((7,5,3))
length = len(x)
print(length) # Error
# answer:
# AttributeError: 'tuple' object has no attribute 'append'



# 25. Choose the correct output of the following code: - 
try: 
    print(1/0)
except ZeroDivisionError:
    print("Zero Division Error")
except: 
    print("Error is raised")
else:
    print("No Error is Raised")
# answer:
# Zero Division Error


# 26. Fill the blank in the below code so that when its executed it will print 'true'
class Employee:
    company_name = 'Google'
    def __init__(self):
        self.name = 'Enma'

print(hasattr(Employee(),'company_name')) # True
print(hasattr(Employee,'company_name')) # True
print(hasattr(Employee(),'name')) # True
print(hasattr(Employee,'name')) # False
print(hasattr(Employee,'salary')) # False

# answer:
# print(hasattr(Employee(),'company_name')) # True
# print(hasattr(Employee,'company_name')) # True
# print(hasattr(Employee(),'name')) # True

'''
breakdown
Kode di atas mendefinisikan sebuah kelas Employee dengan beberapa atribut dan
menggunakan fungsi hasattr() untuk memeriksa keberadaan atribut dalam kelas atau objek. 
Mari kita bahas setiap baris dengan lebih detail:
print(hasattr(Employee(),'company_name')): Pada baris ini, kita menggunakan hasattr()
untuk memeriksa apakah objek yang dibuat dari kelas Employee memiliki atribut company_name. 
Karena company_name adalah atribut kelas (bukan atribut instance), hasilnya adalah True.
print(hasattr(Employee,'company_name')): Pada baris ini, kita menggunakan hasattr() untuk 
memeriksa apakah kelas Employee sendiri memiliki atribut company_name. Karena company_name 
adalah atribut kelas, hasilnya juga adalah True.
print(hasattr(Employee(),'name')): Pada baris ini, kita menggunakan hasattr() untuk memeriksa 
apakah objek yang dibuat dari kelas Employee memiliki atribut name. Karena dalam konstruktor 
(__init__) objek Employee, atribut name diinisialisasi, hasilnya adalah True.
print(hasattr(Employee,'name')): Pada baris ini, kita menggunakan hasattr() untuk memeriksa 
apakah kelas Employee sendiri memiliki atribut name. Karena name adalah atribut instance (objek),
bukan atribut kelas, maka hasilnya adalah False.
print(hasattr(Employee,'salary')): Pada baris ini, kita menggunakan hasattr() untuk memeriksa apakah
kelas Employee sendiri memiliki atribut salary. Karena tidak ada atribut dengan nama salary yang 
didefinisikan dalam kelas Employee, hasilnya adalah False.
Jadi, hasattr() digunakan untuk memeriksa keberadaan atribut dalam kelas atau objek, 
dan hasilnya bergantung pada apakah atribut tersebut ada dalam konteks yang sesuai.
'''


# 27. Choose the correct output of the following code: - 
def calculate(x):
    z = lambda x: return x**2  # Error here 
print(z(x)) 
calculate(4)

# answer: Error (SyntaxError: invalid synt

'''
breakdown
Anda mencoba mendefinisikan ekspresi lambda yang mengambil argumen x 
dan mencoba mengembalikan nilai x**2 dengan menggunakan kata kunci return. 
Kesalahan di sini adalah bahwa dalam ekspresi lambda, Anda tidak perlu menggunakan 
kata kunci return. Lambda secara otomatis mengembalikan hasil dari ekspresi yang 
ditentukan tanpa perlu kata kunci return. Oleh karena itu, Anda hanya perlu menulis:

z = lambda x: x**2

perbaikan code:
def calculate(x):
    z = lambda x: x**2
    return z(x)

result = calculate(4)
print(result)

'''
 

# 28. Choose the correct output of the following code: - 
T1 = (1,)
T2 = (2,)
T3 = (3,)
print(T1+T2+T3)

# answer: (1, 2, 3)

'''
other example:
T1 = [1]
T2 = [2,4]
print(T2+T2)
'''


# 29. Which among the following can not be used as a variable name: - 
# answer : 3Version


# 30. Fill in the blank in the below code so that when it is executed it will print true.
class Student:
    def __init__(self):
        self.name = "Olivia"
    def set_rollNo(self):
        self.rollNo = 45786
        
print(hasattr(Student(),'name')) # True
print(hasattr(Student(),'rollNo')) # False
print(hasattr(Student(),'set_rollNo')) # True
print(hasattr(Student(),'Student')) # False

# answer : 
# print(hasattr(Student(),'name')) # True
# print(hasattr(Student(),'set_rollNo')) # True

'''
breakdown
Kode di atas mendefinisikan sebuah kelas Student dengan konstruktor __init__ dan 
ebuah metode set_rollNo(). Setelah itu, kode menggunakan fungsi hasattr() untuk 
memeriksa keberadaan atribut atau metode dalam kelas Student. Mari kita bahas hasil 
dari masing-masing hasattr():
print(hasattr(Student(),'name')): Ini memeriksa apakah objek yang dibuat dari kelas 
Student memiliki atribut name. Karena dalam konstruktor (__init__) kelas Student, 
atribut name diinisialisasi, hasilnya adalah True.
print(hasattr(Student(),'rollNo')): Ini memeriksa apakah objek yang dibuat dari kelas 
Student memiliki atribut rollNo. Dalam kelas Student, atribut rollNo tidak diinisialisasi 
dalam konstruktor atau metode apapun, sehingga hasilnya adalah False.
print(hasattr(Student(),'set_rollNo')): Ini memeriksa apakah objek yang dibuat dari kelas 
Student memiliki metode set_rollNo(). Karena metode ini didefinisikan dalam kelas Student, 
hasilnya adalah True.
print(hasattr(Student(),'Student')): Ini memeriksa apakah objek yang dibuat dari kelas Student
memiliki atribut atau metode bernama Student. Karena Student adalah nama kelas itu sendiri 
dan bukan atribut atau metode objek, hasilnya adalah False.

Tapi kan ada rollNo di class Student kenapa false?

Dalam kelas Student, terdapat metode set_rollNo(), yang pada saat dijalankan akan membuat atribut rollNo di
dalam objek yang dibuat dari kelas tersebut. Namun, perlu diingat bahwa pada saat kode dijalankan dengan 
hasattr(Student(),'rollNo'), kelas Student sendiri belum diinisialisasi atau dibuat sebagai objek.
Fungsi hasattr() bekerja dengan objek atau kelas yang sudah ada. Ketika Anda memeriksa hasattr(Student(),'rollNo'), 
Anda mencoba memeriksa apakah objek dari kelas Student yang baru dibuat memiliki atribut rollNo. Pada saat itu, 
objek belum dibuat, sehingga hasattr() mengembalikan False.
Namun, jika Anda membuat objek dari kelas Student dan kemudian menjalankan metode set_rollNo(), atribut rollNo 
akan dibuat dalam objek tersebut, dan Anda dapat menggunakan hasattr() untuk memeriksa apakah objek memiliki 
atribut tersebut setelah objek dibuat:

student_obj = Student()  # Membuat objek dari kelas Student
student_obj.set_rollNo()  # Menjalankan metode untuk membuat atribut rollNo
print(hasattr(student_obj, 'rollNo'))  # Sekarang hasilnya akan True

Jadi, kesalahan dalam pemahaman kode sebelumnya adalah bahwa hasattr(Student(),'rollNo')
mencoba memeriksa atribut rollNo pada kelas Student sebelum objek dari kelas tersebut dibuat.

'''

# 31. Which among the following code after execution will print 'true'


# 32. Which among the following code after execution will print 'False' . 
class A : pass
class B(A): pass
obj = A()
print(isinstance(obj,B))


# 33. Choose the correct output of the following code: - 
try:
    a = 0
    print(a = 4)
except:
    print("Error is raised in try")
# answer : Error is raised in try



# 34.  If the will 'sys.txt' already contain the next "Welcome" then what 
# will be the text present in the file after the execution of the following code: -

file = open("sys.txt",'w')
file.write("To Programming")
file.close()
# answer: To Programming


# 35. If the 'sys.txt' file contains the 3 lines,
# 1st line (Welcome)
# 2st line (To Python)
# 3st line (Programming)
# Fill the blank, So that the below code will print text as it is written in the file.
file = open('sys.txt','r')
print(_______________)
file.close()
# # answer: 
# file.read()
# file.read(-1)
# file.read(-10)


'''
breakdown
Pemanggilan file.read() tanpa argumen adalah cara yang paling umum untuk
membaca seluruh konten file. Penggunaan -1 atau -10 biasanya digunakan untuk
mengontrol jumlah karakter yang dibaca dari file, di mana -1 akan membaca 
seluruh konten dan -10 akan membaca 10 karakter terakhir.
'''

# 36. Choose the correct output of the following code: - 
class Class_A():
    def info(self):
        print("Class_A")
class Class_B(Class_A):
    pass
obj = Class_B()
obj.info()
# answer: Class_A


# 37. Fill the blank, so that after execution of the below code the code will print 'Please Rate This Course' . 
class A():
    pass
try:
    raise A()
except :
    print("Please Rate This Course")
except:
    print("Write Review for this Course")

# answer: 
# BaseException
# Exception


# 38. Choose the correc output of the following code: - 
class Student:
    def __init__(self,m):
        self.__marks = m
        grace(self)
        print(self.__marks)
    def grace(self):
        self.__marks = self.__marks + 10
Student(23)
# answer : NameError: name 'grace' is not defined


# 39. Choose the correct output of the following code: - 
tp = (1,2)
print(2*tp)
# answer : (1, 2, 1, 2)


# 40. Choose the correct output of the following code: -
set1 = {1,2}
set2 = {1,2}
print(set1+set2) # Error
# answer : TypeError: unsupported operand type(s) for +: 'set' and 'set'













