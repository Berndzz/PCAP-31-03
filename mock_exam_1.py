# 1. Is the below statement true regarding the variable name?
# Statment: For the default encoding in python 3, A variable name can
# contain the letters from the English language only.
# answer: No


# 2. Choose the correct output of the following code:
# list bisa berbagaai elemen yah
import math

list1 = [("abc", "bca"), 24.56, 23.64, [1, 2, 3]]
list2 = list(list1)  # [("abc", "bca"), 24.56, 23.64, [1, 2, 3]]
list2[1] = "abc"  # [("abc", "bca"), "abc", 23.64, [1, 2, 3]]
list1[3] = "bca"  # [("abc", "bca"), 24.56, 23.64, "bca"]
# print(list1)
# print(list2)
# answer:
# [('abc', 'bca'), 24.56, 23.64, 'bca']
# [('abc', 'bca'), 'abc', 23.64, [1, 2, 3]]


# 3. Choose the correct output of the following code:
# s = '0123456789'
# obj = range(0, len(s), 0)  # range(start,finish,steps)
# l = []
# for i in obj:
#     l.append(int(s[i]))
# add = 0
# for i in obj:
#     add = add+l[i]
# print(add)  # error karena parameter range untuk stepsnya tidak bisa (range() arg 3 must not be zero)
# answer: Error


# 4. Choose the correct output of the following code:
# i = ""
# while i in "          ":
#     print("Python", end=i)  # infinity loop
# answer: PythonPythonPython........

'''
breakdown
Anda mendefinisikan variabel i sebagai string kosong ("").
Kemudian, Anda memulai loop while dengan kondisi i in " ". Ini berarti loop akan berjalan selama i adalah 
substring dari string " ".
Pada setiap iterasi loop, Anda mencetak string "Python" menggunakan print, dan Anda mengatur argumen 
end menjadi nilai dari i. 
end digunakan untuk menentukan karakter yang akan ditambahkan setelah mencetak teks. Dalam kasus ini, 
karakter dari i yang kosong 
akan ditambahkan setiap kali mencetak "Python".
Namun, masalahnya adalah bahwa i selalu adalah string kosong (""). Oleh karena itu, kondisi i in " " selalu 
benar karena 
string kosong adalah substring dari string " ".
Karena kondisi loop selalu benar, loop ini akan berjalan terus-menerus tanpa henti (infinite loop). 
Outputnya akan 
terus mencetak "Python" dengan string kosong di akhirnya, dan loop tidak akan pernah berhenti.
'''

# 5. The ouput of the following code is:
# print(not('False'))  # False
# print(not(0))  # True
# print(not(''))  # True
# print(not(' '))  # False
# print(not(["Python"]))  # False
# print(not([]))  # True

# answer:
# False
# True
# True
# False
# False
# True

'''
breakdown
not adalah operator logika yang digunakan untuk menghasilkan kebalikan dari nilai kebenaran (boolean).

print(not('False')):

'False' adalah string yang bukan nilai boolean, dan tidak kosong. Karena itu, itu dianggap sebagai "truthy" (bukan False), 
dan ketika Anda menerapkan not kepadanya, hasilnya adalah False.
print(not(0)):

Angka 0 dianggap sebagai nilai "falsy" dalam Python, sehingga ketika Anda menerapkan not kepadanya, hasilnya adalah True, 
yang adalah kebalikan dari False.
print(not('')):

String kosong '' dianggap sebagai nilai yang "falsy", sehingga ketika Anda menerapkan not kepadanya, hasilnya adalah True, 
yang adalah kebalikan dari False.
print(not(' ')):

String yang berisi hanya spasi ' ' dianggap sebagai nilai "truthy" (tidak kosong). Ketika Anda menerapkan not kepadanya, 
hasilnya adalah False, yang adalah kebalikan dari True.
print(not(["Python"])):

Daftar (list) yang tidak kosong dianggap sebagai nilai "truthy". Ketika Anda menerapkan not kepadanya, hasilnya adalah False, 
yang adalah kebalikan dari True.
print(not([])):

Daftar (list) yang kosong dianggap sebagai nilai yang "falsy". Ketika Anda menerapkan not kepadanya, 
hasilnya adalah True, yang adalah kebalikan dari False.
'''

# 6. Which among the following print statment will print 4?
# print(2 << 1)  # 4
# print(2 ^ 2)  # 0
# print(2**2)  # 4
# print(2*2)  # 4
# answer: print(2 << 1) , print(2**2) , print(2*2)

# 7. Choose the correct statement
# answer: 3*2/3*3 and 2&2+3*3**2
print(2 & 2+3*3**2)  # 2


# 8. Choose the correct statement for the below code:
# class Class_A:
#     def __init__(self, var):
#         return var


# obj = Class_A(20)
# print(obj)  # error di return var,
# answer: Error

'''
breakdown 

Kode yang Anda berikan memiliki beberapa masalah sintaksis dan logika. Saya akan menjelaskan setiap bagian 
dan memberikan perbaikan yang diperlukan.

Ini adalah definisi dari kelas Class_A. Konstruktor kelas __init__ seharusnya digunakan untuk menginisialisasi 
objek, bukan untuk mengembalikan nilai. Anda seharusnya tidak mengembalikan nilai dari konstruktor. Biasanya, 
Anda akan menginisialisasi atribut objek di dalam konstruktor.
self.var adalah atribut objek yang diinisialisasi dengan nilai var yang diberikan saat objek Class_A dibuat.

Selanjutnya, Anda mencoba membuat objek Class_A dan mencetak 20, tetapi itu akan menghasilkan kesalahan. 
Seharusnya Anda mencetak objek Class_A dengan atribut var yang diinisialisasi.

'''

# solution


# class Class_A:
#     def __init__(self, var):
#         self.var = var


# obj = Class_A(20)
# print(obj.var)  # 20, jika hanya obj saja maka akan mengembalikan value memory (<__main__.Class_A object at 0x000001EF8CD91990>) bukan hasil yang diharapkan


# 9. Fill in the blank with the correct option, so that the below code will print 'File not Found'
# try:
#     open('sys.txt', 'r')
# except:
#     ___________:
#     print('File not Found')
# except:
#     print("File not opened")

# assume that the file 'sys.txt' does not exist in the system
# answer OSError and IOError


# 10. Assume that the location of the 'sys.txt' file is 'D:\new'
# Whic among the following code will print the data present inside the 'sys.txt' file.
# answer:
# file = open('D:\\New\sys.txt', 'r')
# for each in file:
#     print(each)

# file = open('D:\\New\sys.txt', 'r')
# for each in file:
#     print(each)
# file.close()

'''
jika ingin tetap gunakan hanya satu \ anda perlu menambahkan r didepannya dulu 'untuk menghindari karakter escape' ,
contoh : path = r"E:\folder\file.txt"
 
'''

# 11. Which among the following function is used to close the file in the python program?
# answer: close()


# 12. Which among the following are the correct ways to represent
# 0.000000123
# answer: 1.23e-7 , 1.23E-7 , 1.23 * 10 ** -7

'''
breakdown
Cara menghitung notasi eksponensial seperti "1.23e-07" dari angka seperti 0.000000123 cukup mudah dan cepat 
jika Anda memahami prinsipnya. Berikut langkah-langkahnya:

Tentukan mantissa: Mantissa adalah bagian utama dari angka tersebut. Dalam kasus ini, mantissa adalah "1.23". 
Ini adalah angka yang ingin Anda ubah ke notasi eksponensial.

Tentukan eksponen: Eksponen adalah pangkat 10 yang diperlukan untuk mengubah mantissa menjadi angka yang sesuai 
dengan notasi eksponensial. Eksponen ini dapat ditemukan dengan menghitung jumlah digit desimal yang harus digeser 
ke kiri atau ke kanan untuk mendapatkan mantissa antara 1 dan 10.

Jika Anda ingin mengubah 0.000000123 menjadi notasi eksponensial, maka Anda perlu menggeser digit desimal 
ke kanan sebanyak 7 kali untuk mendapatkan mantissa antara 1 dan 10. Ini berarti Anda akan memiliki "1.23" sebagai mantissa.

Tentukan eksponen sebagai jumlah pergeseran digit desimal, yang dalam kasus ini adalah -7.

Gabungkan mantissa dan eksponen dengan simbol "e" untuk mendapatkan notasi eksponensial yang benar: "1.23e-07".

0.0000056 = 5.6e-06: Benar! Ini adalah notasi eksponensial yang benar untuk angka 0.0000056. Anda membaguskan ini dengan 
menggeser digit desimal ke kanan sebanyak 6 kali untuk mendapatkan mantissa "5.6" dan menetapkan eksponen menjadi -6.

780,000,000 = 7.8e8: Benar! Ini adalah notasi eksponensial yang benar untuk angka 780,000,000. Anda membagi angka dengan 
10^8 (karena angka tersebut besar) untuk mendapatkan mantissa "7.8" dan menetapkan eksponen menjadi 8.

0.0000023 x 10^4 = 23: Ini tidak benar. Anda hampir benar. Pertama, angka 0.0000023 adalah notasi eksponensial 
dengan eksponen -6 (karena Anda perlu menggesernya ke kanan 6 kali). Jadi, langkah pertama adalah "2.3e-6". 
Kemudian, Anda akan mengalikannya dengan 10^4, yang setara dengan menggeser mantissa ke kanan sebanyak 4 kali. 
Jadi, hasilnya adalah "2.3e-6" x 10^4 = "2.3e-6+4 = 2.3e-2".

4.2e-6 = 0.0000042: Ini tidak benar. Notasi eksponensial "4.2e-6" sebenarnya sudah benar. Itu berarti 4.2 x 10^(-6), 
yang setara dengan 0.0000042 dalam bentuk desimal. Jadi, jawaban Anda yang pertama adalah benar.

2.5e3 = 2500: Hampir benar! Notasi eksponensial "2.5e3" adalah cara yang benar untuk menyatakan 2500 dalam notasi 
eksponensial. "e3" berarti mengalikan angka dengan 10^3, yang setara dengan menggeser digit desimal ke kanan sebanyak 
3 kali. Jadi, jawaban Anda yang kedua adalah benar.

'''

# 13. Choose the correct output of the following code:
i = 0
# while i < 4:
#     print(i, end="-")
#     i += 1.5
#     if((i < 4) == False):
#         break
#     else:
#         print(0, end=" ")
# # answer: 0-1.5-3.0-

'''
breakdown
Awalnya, nilai i adalah 0. Kondisi i < 4 adalah True, sehingga masuk ke dalam loop.
Mencetak nilai i (0) ke layar dengan tanda "-" sebagai pemisah, sehingga mencetak "0-".
Menambahkan 1.5 ke i, sehingga nilai i sekarang menjadi 1.5.
Kondisi (i < 4) == False adalah False, sehingga tidak menjalankan blok if.
Masuk ke dalam blok else dan mencetak 0 dengan spasi sebagai pemisah, sehingga mencetak "0 ".
Kembali ke atas loop, nilai i sekarang adalah 1.5.
Proses ini berlanjut sampai nilai i menjadi 3.0.
Ketika nilai i mencapai 3.0, kondisi i < 4 masih True, sehingga mencetak "3.0-" dan menambahkan 1.5 
lagi ke i, sehingga nilai i menjadi 4.5.
Kemudian, kondisi (i < 4) == False menjadi True, sehingga program keluar dari loop.
Hasil akhir yang dicetak ke layar adalah "0-1.5-3.0-", sesuai dengan output yang diberikan 
sebagai jawaban.

'''


# 14. Choose the correct output of the following code:
# class Calculate:
#     var1 = 20

#     def __init__(self, var1):
#         self.var1 = var1
#         self.var1 = self.var1 + 7  # 20+7  = 27
#         Calculate.var1 = Calculate.var1 + 7  # 34+7 = 41

#     def Print(self):
#         print(Calculate.var1)
#         print(self.var1)


# Calculate(10).Print()
# Calculate(15).Print()
# answer 27 17 34 22

'''
27, 17 = 
self.var1 = 10
self.var1 = self.var1 + 7 # 10 + 7 = 17
Calculate.var1 = Calculate.var1 + 7 # 20 (var1) + 7 = 27


34, 22 = 
self.var1 = 15
self.var1 = self.var1 + 7 # 15 + 7 = 22
Calculate.var1 = Calculate.var1 + 7 # 27 (var1, karna nilai sebelumnya 27) + 7 = 34 

maka, hasilnya 27 17 34 22
'''


# 15. Choose the correct output of the following code:
# print(tuple[3])
# answer: Type Error

'solution'
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[3])

# 16. Choose the correct output of the following code:
x = 45
y = 25


# def Sum(x):
#     global x
#     print("Sum inside Sum() :", x+y)


# Sum(25)
# print("Sum outside Sum() :", x+y)
# answer: Error


# 17. If the sys.txt file contains the 3 lines,
# 1st line (Welcome),
# 2nd line (To Python)
# 3rd line (Programming)
# What will be the output of the following code:
file = open('sys.txt', 'r')
# print(file.read(500))
# file.close()
# answer:
# Welcome
# To Python
# Programming


# 18. Choose the correct output of the following code:
result1 = '{0},{2} and {1}'.format('a', 'b', 'c')
result2 = '{},{} and {}'.format('a', 'b', 'c')
# print(result1)
# print(result2)
# answer:
# a,c and b
# a,b and c

'''
breakdown
result1 = '{0},{2} and {1}'.format('a', 'b', 'c'): Di sini, Anda menggunakan indeks-posisi {0}, {1}, dan {2} untuk 
menggantikan nilai dengan argumen yang Anda berikan dalam metode format(). Argumen yang Anda berikan adalah 'a', 'b', dan 'c'. 
Jadi, penggantian akan dilakukan berdasarkan urutan indeks-posisi.

{0} akan diganti dengan 'a'.
{1} akan diganti dengan 'b'.
{2} akan diganti dengan 'c'.
Sehingga, hasil dari result1 adalah 'a,c and b', karena 'a' menggantikan {0}, 'b' menggantikan {1}, dan 'c' menggantikan {2}.

result2 = '{},{} and {}'.format('a', 'b', 'c'): Di sini, Anda tidak menggunakan indeks-posisi, tetapi hanya {} tanpa indeks. 
Ini akan secara otomatis menggantikan nilai dengan argumen dalam urutan yang sama seperti dalam metode format().

{} pertama akan diganti dengan 'a' (karena itu adalah argumen pertama).
{} kedua akan diganti dengan 'b' (argumen kedua).
{} ketiga akan diganti dengan 'c' (argumen ketiga).
Sehingga, hasil dari result2 adalah 'a,b and c', sesuai dengan urutan argumen yang Anda berikan.
'''


# 19. Will the bellow code will raise an error or not.
a = '😁'
b = '🤗'
c = '😎'
d = '😞'
# print(a+b+c+d)
# answer: No


# 20. Choose the correct output of the following code:
# print(1**2**2.)
# answer: 1.0

'''
breakdown
Pertama, 1**2 akan dievaluasi, menghasilkan 1.
Kemudian, 1**1.0 (karena 2**2.0 adalah 4.0) juga akan dievaluasi, dan hasilnya tetap 1.
'''


# 21. The Output of the following code is:
print("%.2o" % (25))
print("%.5o" % (25))
# answer:
# 31
# 00031


'''
breakdown
print("%.2o" % (25)): Pada baris ini, kita mencetak angka 25 dalam format oktal dengan dua digit. % digunakan untuk 
memasukkan nilai ke dalam string format. %.2o adalah format string yang digunakan untuk mengonversi angka menjadi format 
oktal dengan dua digit. Angka 25 dalam format oktal adalah 31 (2 dalam basis 8).

print("%.5o" % (25)): Pada baris ini, kita mencetak angka 25 dalam format oktal dengan lima digit. %.5o adalah format 
string yang digunakan untuk mengonversi angka menjadi format oktal dengan lima digit. Dalam hal ini, karena kita meminta 
lima digit, kita harus menambahkan angka 0 di depan angka oktal sehingga total panjangnya menjadi lima digit. Angka 25 
dalam format oktal adalah 31, dan kita menambahkan tiga angka 0 di depannya untuk mencapai panjang lima digit, sehingga 
hasilnya adalah "00031".


Desimal (Basis 10):
%d atau %i

Biner (Basis 2):
%b

Oktal (Basis 8):
%o

Heksadesimal (Basis 16):
%x (huruf kecil)
%X (huruf besar)

Float (Bilangan Pecahan):
%f

Scientific Notation (Notasi Ilmiah):
%e (notasi ilmiah dengan huruf kecil)
%E (notasi ilmiah dengan huruf besar)

Percentage (Persentase):
% (persentase)

Dengan Angka: 
%2d - Integer Desimal dengan lebar minimum lapangan 2.
%5.2f - Angka Pecahan dengan lebar minimum lapangan 5 dan 2 digit desimal.
%3o - Bilangan Oktal dengan lebar minimum lapangan 3.
%4X - Bilangan Heksadesimal dengan huruf besar dan lebar minimum lapangan 4.
%.2e - Notasi Ilmiah dengan 2 digit desimal.

'''


# 22. Choose the correct output of the following code:
# print("% 10E" % (85792229130))
# answer:  8.579223E+10


# 23. Which among the following are unary operators?
# answer: ~ , not , - , +


# 24. Choose the correct output of the following code:
D = {5: 5, 15: '15', '5': 5, '15': 25}  # dict
D[str(15)] = 100
L = list(D)
L.append("Python")
# print(L)

'''
breakdown
Pertama, kita mendefinisikan sebuah dictionary (D) dengan beberapa pasangan kunci-nilai:

5: 5
15: '15'
'5': 5
'15': 25
Dictionary ini memiliki empat pasangan kunci-nilai yang berbeda.

Kemudian, kita mengakses dictionary (D) dengan menggunakan kunci 'str(15)' dan mengatur nilainya menjadi 100. 
Ini akan mengubah pasangan kunci '15' menjadi 100 dalam dictionary. Hasilnya sekarang menjadi:

5: 5
15: 100 # Kunci '15' diubah menjadi 100
'5': 5
'15': 25
Selanjutnya, kita membuat sebuah list (L) dari dictionary (D) dengan menggunakan list(D). Ini akan mengambil 
semua kunci dari dictionary (D) dan membuat list baru (L) yang berisi kunci-kunci tersebut. Hasilnya adalah:
L = [5, 15, '5', '15']
Terakhir, kita menambahkan string "Python" ke list (L) dengan menggunakan L.append("Python"). 
Setelah operasi ini, list (L) akan menjadi:
L = [5, 15, '5', '15', 'Python']
Jadi, hasil akhirnya adalah list (L) yang berisi beberapa kunci dari dictionary (D) dan string "Python"
yang telah ditambahkan. Hasil cetaknya adalah [5, 15, '5', '15', 'Python'].

'''

# 25. Choose the correct output of the following code:
# print(0x3 | 0x9)
# answer: 11

'''
breakdown
0x3 dalam heksadesimal adalah representasi bilangan desimal 3. Ini diwakili dalam bentuk biner oleh 0011, 
karena 3 dalam biner adalah 11.
0x9 dalam heksadesimal adalah representasi bilangan desimal 9. Ini diwakili dalam bentuk biner oleh 1001, 
karena 9 dalam biner adalah 1001.
Sekarang, kita akan melakukan operasi bitwise OR (|) antara kedua bilangan ini. Operasi bitwise OR akan 
menghasilkan bit yang di-set menjadi 1 jika ada setidaknya satu bit 1 dalam dua bilangan yang sedang 
dioperasikan.
0011
1001
----
1011

Hasil operasi bitwise OR adalah 1011 dalam bentuk biner.
1011 dalam biner adalah 11 dalam desimal.
Jadi, hasil dari 0x3 | 0x9 adalah 11 dalam desimal.
'''


# 26. Choose the correct ouput of the following code:
# try:
#     print(30/0)
# except ZeroDivisionError:
#     print("Zero Divison Error")
# else:
#     print("Nothing went wrong")
# except:
#     print("Something went wrong")
# answer: SyntaxError will be raised


# 27. Which among the following operators have the lowest binding among all the operatos present in python.
# answer: =


# 28. Choose the correct output of the following code:
# i = ""
# for i in "    ":
#     print("Java", end=i)
# answer: Java Java Java Java


# 29. Which among the following is the correct way to delete the file 'sys.txt' from the hard drive using the python program.
# answer:
'''
import os 
os.remove(sys.txt)
'''


# 30. Choose the correct statement for the below code:
class Class:
    def __init__(self, var):
        self.var1 = var
        self._var1 = var
        self.__var1 = var


obj = Class(20)
# print(obj.__var1)
# print(obj._var1)
# print(obj.var1)
# answer: The code raises an error due to line 8.


# 31. Choose the correct ouput of the following code:
class A:
    def __init__(self):
        self.num1 = 10


class B(A):
    def __init__(self):
        self.num2 = 20

    def show_num2(self):
        print(self.num2)


# obj = B()
# obj.show_num1()
# obj.show_num2()
# answer: Error


# 32. Choose the correct ouput of the following code:
class Parent:
    def __init__(self, age):
        self.age = age

    def get_Parent_age(self):
        return self.age


class Child(Parent):
    def __init__(self, age1, age2):
        self.age = age1
        super().__init__(age2)

    def get_Child_age(self):
        return self.age


son = Child(20, 40)
# print("Parent age :", son.get_Parent_age())
# print("Child age :", son.get_Child_age())
# answer:
# Parent age : 40
# Child age : 40


# 33. Choose the correct output of the following code:
# try:
#     print("Pytho"n")
# except:
#     print("Error is raised")
# finally:
#     print("Code End")
# answer: None of the print function will print anything


# 34. Due to Which type of error the code will terminate:
# str = " , ".join(["Java", "Python", "Ruby"])
# l = (str, " are", " Programming", "languages")
# print(l[-5])
# answer: IndexError


# 35. Which among the following way will convert the binary value 'Ob100'
# to the decimal value 4?
# answer:
# print(int('0b100', 2))
# print(int('100', 2))


# 36. Choose the correct output of the following code:
var = round(0.5) + round(0.6) + round(0.4)
# print(var)
# answer: 1

'''
breakdown
Pertama, fungsi round() digunakan untuk membulatkan angka ke bilangan bulat terdekat. 
Jika angka desimal kurang dari 0.5, maka akan dibulatkan ke bawah, dan jika 0.5 atau 
lebih besar, maka akan dibulatkan ke atas.

Di dalam ekspresi tersebut, kita memiliki tiga pemanggilan fungsi round():

round(0.5) akan menghasilkan 0 karena 0.5 akan dibulatkan ke bawah menjadi 0.
round(0.6) akan menghasilkan 1 karena 0.6 akan dibulatkan ke atas menjadi 1.
round(0.4) akan menghasilkan 0 karena 0.4 akan dibulatkan ke bawah menjadi 0.
Setelah itu, kita menjumlahkan hasil pembulatan: 0 + 1 + 0, yang menghasilkan nilai 1.


'''


# 37. Choose the correct output of the following code:
# a = {2+3}*5+2**2 #ngk bisa dilakukan operasi matematikan dengan set
# print(a)
# answer: Error (TypeError)


# 38. Choose the correct output of the following code:
class Calculate:
    A = 20
    B = 20

    def __init__(self, a, b):
        A = a
        B = b
        print(self.A + self.B / 2 + 1)
#         # 20 + 20 / 2 + 1  = 20 + 10 + 1 = 30.1


Calculate(4, 10)
# answer: 31.0


# 39. Which among the following is the correct way to comment multiple lines in python?
# answer:
'''Hello
World
Python'''


# 40. Choose the correct output of the following code:
# print(math.factorial(0.6))
# answer: TypeError OR ValueError

'''
breakdown
Fungsi math.factorial() dari modul math dalam Python adalah untuk 
menghitung faktorial dari bilangan bulat positif. Faktorial adalah hasil 
perkalian semua bilangan bulat positif dari 1 hingga bilangan tersebut.
Namun, faktorial hanya didefinisikan untuk bilangan bulat positif. Itu berarti, 
Anda tidak dapat menghitung faktorial dari bilangan non-bulat atau bilangan negatif 
menggunakan fungsi math.factorial(). Jika Anda mencoba melakukannya, Anda akan 
mendapatkan kesalahan, dan jenis kesalahan yang muncul tergantung pada versi Python yang 
Anda gunakan.
TypeError: Pada beberapa versi Python, Anda akan mendapatkan TypeError 
karena argumen yang diberikan harus berupa bilangan bulat positif. Fungsi 
math.factorial() hanya menerima bilangan bulat positif sebagai argumen.
ValueError: Pada beberapa versi Python lainnya, Anda mungkin mendapatkan 
ValueError dengan pesan yang menyatakan bahwa faktorial tidak dapat dihitung 
untuk bilangan non-bulat atau negatif.
Jadi, kesalahan yang muncul bisa berupa TypeError atau ValueError, 
tergantung pada implementasi Python yang Anda gunakan. Namun, yang pasti, 
Anda tidak dapat menghitung faktorial dari bilangan non-bulat seperti 0.6 
menggunakan math.factorial().

'''
