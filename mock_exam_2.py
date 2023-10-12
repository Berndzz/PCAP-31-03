import copy
import math

# 1. Choose the correct output of the following code:
# class Car:
#     def __init__(self, x, y):
#         self.name = x
#         self.price = y


# obj1 = Car('Audi', 2000)
# obj2 = Car('Audi', 2000)
# print(obj1 == obj2)
# answer: False

'''
breakdown
Dalam kode di atas, Anda telah mendefinisikan kelas Car dengan metode konstruktor __init__ yang 
menerima dua argumen, x dan y, yang digunakan untuk menginisialisasi atribut name 
dan price dalam objek.
Selanjutnya, Anda menciptakan dua objek dari kelas Car, yaitu obj1 dan obj2. 
Kedua objek ini memiliki nilai yang sama untuk atribut name dan price, yaitu 
'Audi' dan 2000.
Kemudian, kode mencoba untuk membandingkan kedua objek dengan operator ==:
print(obj1 == obj2)
Hasilnya adalah False. Hal ini terjadi karena dalam Python, operator == digunakan 
untuk membandingkan objek berdasarkan identitasnya, bukan nilai-nilai atributnya. 
Meskipun kedua objek memiliki nilai yang sama untuk atribut name dan price, mereka 
adalah objek yang berbeda secara individu dengan alamat memori yang berbeda. Oleh 
karena itu, meskipun isi atributnya sama, kedua objek dianggap berbeda secara identitas.
Jika Anda ingin membandingkan objek berdasarkan nilai-nilai atributnya, Anda dapat 
mendefinisikan metode __eq__ (equal) di dalam kelas Car. Metode ini memungkinkan 
Anda untuk menentukan bagaimana perbandingan objek seharusnya dilakukan berdasarkan 
nilai-nilai atributnya.
'''


# 2. Choose the correct output of the following code:
# var1 = '5555'
# var2 = '56'
# print(var2 > var1) # True

'''
breakdown
var2 > var1. Ini akan membandingkan string '56' dengan '5555' berdasarkan urutan leksikal karakter pertama ke 
karakter terakhir. Karena karakter '5' dalam '56' lebih besar dari karakter '5' dalam '5555', maka hasilnya adalah True.
'''

# var1 = '5555'
# var2 = '55'
# print(var2 > var1) # False

'''
breakdown
var2 > var1. Ini akan membandingkan string '55' dengan '5555' berdasarkan urutan leksikal karakter 
pertama ke karakter terakhir. Karena karakter pertama adalah sama ('5'), maka Python akan membandingkan 
karakter kedua. Karena karakter '5' sama lagi, maka Python akan terus membandingkan karakter berikutnya. 
Karena tidak ada karakter dalam '55' yang lebih besar dari karakter '5' dalam '5555', hasilnya adalah False.
'''

# var1 = '5555'
# var2 = '54'
# print(var2 > var1) # False
# answer:
# True
# False
# False

'''
breakdown
var2 > var1. Ini akan membandingkan string '54' dengan '5555' berdasarkan urutan leksikal karakter pertama ke karakter terakhir. 
Karena karakter pertama adalah sama ('5'), maka Python akan membandingkan karakter kedua. Karena karakter '4' lebih kecil dari 
karakter '5', hasilnya adalah False.
'''


# 3. Choose the correct output of the following code:
# for i in range(5):
#     pass
# print(i)
# answer: 4

'''

breakdown
Dalam loop for ini, Anda menggunakan range(5) untuk menghasilkan 
urutan angka dari 0 hingga 4. Loop ini akan dieksekusi sebanyak 
lima kali, dengan i mengambil nilai dari 0 hingga 4 pada setiap iterasi.
Penting untuk diingat bahwa variabel i yang dideklarasikan 
dalam loop for akan tetap ada setelah loop selesai, dan nilai 
terakhir yang diassign ke i selama iterasi adalah 4 (iterasi terakhir 
dalam range(5)).
Kemudian, setelah loop selesai, Anda mencetak nilai dari variabel i:
print(i)
Hasil cetakan ini akan menjadi 4 karena i memiliki nilai terakhir 
yang diassign selama iterasi loop for, yaitu 4.

'''

# 4.Choose the correct output of the following code:
# L = [1.5, 'Python', False]
# T = (1.2, 'Java', 'True')
# for i in range(len(L)):
#     if L[i]:
#         L[i] = L[i] + T[i]
#     else:
#         T[i] = L[i] + T[i]
# print(L)
# answer: Error as a string value can not be concatenated with a boolean value

'''
breakdown
Anda memiliki dua struktur data: L adalah daftar (list) yang berisi 
elemen-elemen seperti float (1.5), string ('Python'), dan boolean (False). 
T adalah tupel (tuple) yang berisi elemen-elemen seperti float (1.2), 
string ('Java'), dan string ('True').
Anda menggunakan loop for untuk mengiterasi melalui indeks dari 
elemen-elemen dalam daftar L, yang dihitung dengan range(len(L)).
Di dalam loop, Anda menggunakan pernyataan kondisional if untuk 
memeriksa apakah elemen saat ini dalam daftar L adalah True (1.5 dan 
'Python' dianggap True, sedangkan False adalah boolean False). Jika elemen 
tersebut dianggap True, Anda mencoba untuk menggabungkannya dengan elemen 
yang sesuai dari tupel T dan menyimpan hasilnya kembali ke daftar L.
Jika elemen saat ini dalam daftar L adalah False (boolean False), 
Anda mencoba untuk menggabungkannya dengan elemen yang sesuai dari 
tupel T, yang dalam hal ini adalah string 'True'. Ini adalah tempat 
kesalahan terjadi.
Akhirnya, Anda mencetak daftar L setelah iterasi selesai.
Namun, pada langkah ke-4, terjadi kesalahan. Anda mencoba untuk 
menggabungkan boolean (False) dengan string ('True'), yang tidak 
valid dalam Python. Itulah mengapa Anda mendapatkan kesalahan yang 
mengatakan "Error as a string value cannot be concatenated with a boolean value."
Untuk menghindari kesalahan ini, pastikan bahwa Anda menggabungkan 
jenis data yang kompatibel saat melakukan operasi penggabungan 
(concatenation) atau operasi lainnya dalam Python.

'''


# 5. Which among the following are the wrong ways to create a variable in python?
# answer:
'''
True = 3
and = 3
None = 3
'''


# 6. Choose the correct output of the following code:
# print(None + None)
# answer: Error


# 7. Choose the correct number of static, local or instance variables in the below code:
class Animal:
    price = 500  # Atribut kelas (static)

    def __init__(self, x):  # Konstruktor (local)
        self.bread = x  # Variable instance (local)

    def name_me(self, y):  # Metode Instance (local)
        self.name = y  # Atribut instance (local)
# answer: static: 1, local: 4, instance: 2


# 8.What will be printed on the console after executing the below code:
# print(float('25.65'))
# print(int('25.65'))
# answer:
# 25.65
# Error


# 9. The output of the following code:
# list1 = [10, 20, 30, ['A', 'B', 'C']]
# list2 = list1.copy()
# list3 = copy.deepcopy(list1)
# list1[3][1] = 0000
# list1[1] = 0000
# print(list1)
# print(list2)
# print(list3)
# answer:
# [10, 0, 30, ['A', 0, 'C']]
# [10, 20, 30, ['A', 0, 'C']]
# [10, 20, 30, ['A', 'B', 'C']]


# 10. Choose the correct output of the following code:
# i = 0
# for i in range(0, 4):
#     print(i, end=" ")
#     i = i + 1
# else:
#     print("Python")
# answer: 0 1 2 3 Python

# 11. Fill the blank in the below code, So that the 'brand: ford' will be printed successfully
# class Vehicle:
#     def ________:
#         print('Brand', 'Ford')

# Vehicle()
# answer:
# __init__(brand)
# __init__(self)


# 12. Fill the blank, So that the below code will print 'Bella'.
# class Pet:
#     def call_me(name):
#         print("Bella")


# obj = Pet()
# _______
# answer :
# obj.call_me()
# Pet.call_me("Bella")

# 13. Choose the correct output of the following code: -
# try:
#     print(hello)
# except NameError:
#     print("Something went wrong")
# except NameError:
#     print("Everything went wrong")
# finally:
#     print("End of Code")

# answer:
# Something went wrong
# End of Code

'''
breakdown
Pada baris pertama (try:), Anda mencoba mencetak variabel Hello. Namun, 
variabel ini tidak didefinisikan sebelumnya dalam kode, yang akan 
mengakibatkan NameError yang seharusnya tertangkap oleh blok except.
Pada baris kedua (except NameError:), kode mencetak pesan "Something 
error". Ini adalah blok penanganan yang akan dijalankan jika terjadi 
NameError.
Pada baris ketiga (except NameError:), Anda mencoba menangani NameError 
sekali lagi. Namun, dalam Python, hanya satu blok except yang akan 
dieksekusi saat terjadi kesalahan. Dalam hal ini, pesan "Something error" 
akan dicetak dan blok except kedua tidak akan pernah dieksekusi.
Pada baris keempat (finally:), blok finally akan selalu dieksekusi, 
terlepas dari apakah terjadi kesalahan atau tidak. Pesan "End of code" 
akan dicetak setelah eksekusi blok try atau except.

'''

# 14. Choose the correct output of the following code: -
# print({1, 2, 3, 4}+{2, 3, 4, 4})
# answer : Error (TypeError: unsupported operand type(s) for +: 'set' and 'set')


# 15. The output of the following code: -
# L = [lambda x: x+8, lambda y:y+9, lambda z:z+3]
# for i in range(0, len(L)):
#     print(L[i])
# answer :
# <function <lambda> at 0x0000023FF30F3E20>
# <function <lambda> at 0x0000023FF3791870>
# <function <lambda> at 0x0000023FF3791900>

'''
solution:
L = [lambda x: x + 8, lambda y: y + 9, lambda z: z + 3]

# Menggunakan lambda pertama (x + 8)
result1 = L[0](5)  # Memanggil lambda pertama dengan nilai x = 5
print(result1)     # Output: 13 (5 + 8)

# Menggunakan lambda kedua (y + 9)
result2 = L[1](10)  # Memanggil lambda kedua dengan nilai y = 10
print(result2)      # Output: 19 (10 + 9)

# Menggunakan lambda ketiga (z + 3)
result3 = L[2](7)   # Memanggil lambda ketiga dengan nilai z = 7
print(result3)      # Output: 10 (7 + 3)
'''

# 16. Choose the correct output of the following code: -
# print({a+1 for a in range(4)})
# print([a+1 for a in range(4), 1, 2, 3, 4, 6, 8])
# answer:
# {1, 2, 3, 4}
# Error

# 17. Which among the following code is used for writing into a file in binary format?

# answer :
'''
✅
file = open("sys.txt",'rb+')
file.write(b'Welcome to python programming')
file.close()

✅
file = open("sys.txt",'wb+')
file.write(b'Welcome to python programming')
file.close()

✅
file = open("sys.txt",'wb')
file.write(b'Welcome to python programming')
file.close()
'''

# 18. Which among the following print statement will print a boolean value 'true or false' ?
# answer:
# print(None == None)
# print(None != None)


# 19. Choose the correct output of the following code: -
result = dict()
result[(1, 2, 3)] = 34
result[(2, 3, 1)] = 40
result[(3, 1, 2)] = 13
l = [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
summ = 0
for i in l:
    summ = summ + result[i]
print(summ)
# answer : 87

# 20. Choose the correct output of the following code: -
# tuple1 = (4, 3, 7, 9)
# tuple2 = (4, 3, 3, 10)
# print(tuple1 > tuple2)
# answer: True

'''
breakdown
Dalam konteks perbandingan tuple, Python membandingkan elemen-elemen tuple 
satu per satu, dimulai dari elemen pertama (indeks 0) hingga elemen terakhir. Perbandingan ini dilakukan dengan cara membandingkan elemen pertama dari kedua tuple. Jika elemen pertama dari tuple1 lebih besar daripada elemen pertama dari tuple2, maka hasilnya adalah True. Jika elemen pertama sama, maka Python akan melanjutkan dengan membandingkan elemen kedua, dan seterusnya, hingga menemukan perbedaan.
Mari kita periksa tuple tuple1 dan tuple2:
•	Elemen pertama tuple tuple1 adalah 4.
•	Elemen pertama tuple tuple2 juga 4.

Karena elemen pertama dari kedua tuple sama, Python akan melanjutkan dengan 
membandingkan elemen kedua:
•	Elemen kedua tuple tuple1 adalah 3.
•	Elemen kedua tuple tuple2 juga 3.

Karena elemen kedua dari kedua tuple juga sama, Python akan melanjutkan 
dengan elemen ketiga:
•	Elemen ketiga tuple tuple1 adalah 7.
•	Elemen ketiga tuple tuple2 adalah 3.

Karena elemen ketiga dari tuple1 (yaitu 7) lebih besar daripada elemen 
ketiga dari tuple2 (yaitu 3), hasil dari perbandingan adalah True.

'''

# 21. Choose the correct output of the following code: -
# l = list('abcdef')
# a, b, c, l[0], l[1], l[2] = l[0], l[1], l[2], l[-1], l[-2], l[-3]
# l[3], l[4], l[5] = c, b, a
# print(l)
# answer: ['f', 'e', 'd', 'c', 'b', 'a']


# 22. Choose the correct output of the following: -
# def say(p, q=42, r=5, s=28):
#     print('p:', p, 'q:', q, 'r:', r, 's:', s)


# say(48, (45, 39), s=30)
# answer: p: 48 q: (45, 39) r: 5 s: 30

# 23. Which among the following is the first line in the output: -
# def show(x):
#     print(x)
#     return 0

# print(show(1) & show(2)+show(3)*show(4)**show(5))
# answer: 1
# or 0

# 24. The output of the following code: -
# print({1.00, 1.0, 1, 3, 3.0, 3.00})
# answer: {1.0, 3}


# 25. Choose the correct output of the following code: -
# if((0.1+0.2) == (0, 3)):
#     print("if")
# elif((0.3+0.4) == (0.7)):
#     print("elif")
# else:
#     print("else")


# 26. Fill in the blank, for the output of the below code to be '97 98 99 100'
# T = ('a', 'b', 'c', 'd')
# L = range(0, 5)
# for i in L:
#     print(_____, end=",")
#     if i >= 3:
#         break
# # answer: ord(T[i])


# 27. Choose the correct output of the following code: -
# set1 = (1, 2, 4)
# set2 = {2, 4, 5}
# set3 = set()
# for i in set1:
#     for j in set2:
#         i = i+1
#         set3.add(i)
#         set3.add(j)
# for i in range(0, len(set3)):
#     print(set3[i], end="")
# answer: Error (TypeError: 'set' object is not subscriptable)

# 28. Choose the correct output of the following code: -
# s = 'pyhtonPYTOHN'
# for i in range(0, len(s)):
#     if (i % 2.0 == 0):
#         s[i].lower()
#     else:
#         s[i].upper()
# print(s)
# answer: pyhtonPYTOHN


'''

breakdown
s adalah string yang berisi karakter "pythonPYTOHN".
Perulangan for dijalankan untuk i dalam rentang 0 hingga 
panjang string s (indeks dari 0 hingga len(s)-1).
Pada setiap iterasi, kode mencoba untuk memeriksa 
apakah indeks i adalah bilangan genap dengan menggunakan 
i % 2.0 == 0. Namun, ini bukan cara yang tepat untuk 
memeriksa apakah indeks i adalah bilangan genap. 
Seharusnya Anda menggunakan i % 2 == 0 untuk melakukan 
periksaan genap.
Kemudian, dalam blok if, Anda mencoba untuk mengubah 
huruf pada posisi genap menjadi huruf kecil dengan s[i].
lower(), dan dalam blok else, Anda mencoba untuk mengubah
huruf pada posisi ganjil menjadi huruf besar dengan s[i].
upper(). Namun, ini tidak akan mengubah string s secara 
langsung, karena string dalam Python bersifat tidak dapat 
diubah (immutable). Anda perlu menangkap hasil perubahan 
ini dalam variabel baru atau menggantikan karakter di 
indeks i dengan hasil perubahan.
Terakhir, Anda mencoba untuk mencetak string s setelah 
iterasi, tetapi karena perubahan yang Anda lakukan 
dalam loop tidak memengaruhi string s, maka hasil 
cetakan akan tetap "pyhtonPYTOHN".

'''

# 29. Choose the correct statement regarding python default Overriding and Overloading.
# answer: Overriding is possible in python


'''
breakdown

Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: "Dog barks"


Overloading
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calculator = Calculator()
result1 = calculator.add(1, 2)  # Tidak ada overloading di Python, yang digunakan adalah metode terakhir yang didefinisikan
result2 = calculator.add(1, 2, 3)  # Ini akan memanggil metode kedua dengan tiga argumen
'''

# 30. Fill the blank, So that the below code will print 'In A'.


# class A:
#     def x(self, a):
#         print("In A")


# class B(A):
#     def __init__(self):
#         self.x(2)

#     def ______:
#         print("In B")


# B()
# answer:
# __x(self,a)
# _x(self,a)


# 31. Choose the correct output of the following code:-
# class Bike:
#     def __init__(self):
#         self.__Company_name = "BMW"
#         self.price = 2000

#     def details(self):
#         print('Name : ', self.__Company_name, 'Price : ', self.price)


# class Car(Bike):
#     def __init__(self):
#         super().__init__()
#         self.__Company_name = "Audi"
#         self.price = 4000


# obj = Car()
# obj.details()
# answer: Name : BMW Price: 4000

'''

breakdown
Kelas Bike memiliki atribut __Company_name yang diberi nilai 
"BMW" dan atribut price yang diberi nilai 2000. Atribut 
__Company_name diawali dengan dua garis bawah (double underscore), 
yang menandakan bahwa atribut ini adalah atribut pribadi (private) 
yang tidak seharusnya diakses dari luar kelas.
Kelas Bike juga memiliki metode details() yang mencetak 
nama perusahaan dan harga sepeda motor.
Kelas Car adalah subclass dari Bike. Dalam konstruktor 
(__init__()) kelas Car, kita menggunakan super().__init__() 
untuk memanggil konstruktor kelas induk (Bike) dan menginisialisasi 
atribut __Company_name menjadi "BMW" dan atribut price 
menjadi 2000, sesuai dengan nilai awal dari kelas Bike. Namun, dalam konstruktor Car, kita juga mengubah nilai atribut __Company_name menjadi "Audi" dan nilai atribut price menjadi 4000.
Objek obj dibuat sebagai instance dari kelas Car.
Kemudian, metode details() dipanggil pada objek obj. 
Metode ini mencetak nilai atribut __Company_name dan 
price dari objek. Namun, perhatikan bahwa saat mencetak 
__Company_name, nilai yang dicetak adalah "BMW", bukan "Audi". 
Ini terjadi karena atribut __Company_name dalam kelas Car 
adalah atribut yang berbeda dari atribut __Company_name 
dalam kelas Bike, meskipun memiliki nama yang sama.

'''


# 32. Choose the correct statement regarding the below code: -
# details = {['Audi','BMW'] : ['Price : 2000', 'Year : 1958']}
# details = dict()
# details = [{'Audi','BMW'}] = {'Price : 2000' , 'Year : 1958'}
# details[{'Audi' : 1, 'BMW': 2}] = {'Price' : 2000, 'Year' : 1958}

# answer:
# ['Audi','BMW'] can not be used as a key in a dictionary
# {'Audi','BMW'} can not be used as a key in a dictionary
# {'Audi':1, 'BMW':2} can not be used as a key in a dictionary


# 33. Choose the correct output of the following code: -
# list1 = [24, 27, 34, 89, 48]
# list2 = list1
# list2[1] = "LIST_2"
# list1[3] = "list_1"
# print(list1)
# print(list2)

# answer:
# [24, 'LIST_2', 34, 'list_1', 48]
# [24, 'LIST_2', 34, 'list_1', 48]


# 34. Choose the correct output of the following code: -
# s = {1, 1, 2, 4, 5, 7, 8}
# var = list(x//1.0 for x in s if x in s and x % 2 == 0)
# print(var)
# answer : [2.0, 4.0, 8.0]


# 35. Choose the correct output of the following code: -
# my_str = "pythonprogramming"  # ngk bisa langsung sorting string menggunakan sort(), ubah dulu ke list lalu balikan lagi ke string ya.
# my_str.sort()
# print(my_str.index('p'))
# answer: Error

# 36. Choose the correct output of the following code: -
# def Reverse(x):
#     x.reverse()
#     return x


# def check_sorted(x):
#     return x.sorted()


# l = list('9876543210')
# print("Status : ", check_sorted(Reverse(l)))
# answer : Error


'''

breakdown
Anda mendefinisikan dua fungsi, Reverse(x) dan check_sorted(x).
Dalam fungsi Reverse(x), Anda mencoba untuk membalikkan 
list x dengan menggunakan metode reverse(). Ini akan 
membalikkan list dengan mengubahnya secara langsung. 
Namun, metode reverse() tidak mengembalikan nilai (None), 
sehingga fungsi Reverse(x) tidak mengembalikan hasil yang
sesuai. Anda hanya mengubah list asli.
Dalam fungsi check_sorted(x), Anda mencoba untuk 
memeriksa apakah list x diurutkan dengan menggunakan
metode sorted(). Ini adalah kesalahan, karena tidak 
ada metode sorted() yang ada dalam Python. Untuk 
memeriksa apakah list diurutkan, Anda dapat menggunakan
fungsi bawaan sorted() di luar fungsi.
Anda membuat list l yang berisi karakter dari 
'9876543210'.
Kemudian, Anda mencoba untuk memeriksa apakah list 
l sudah diurutkan dengan menggunakan fungsi check_sorted(Reverse(l)).
Di sini, Anda mencoba untuk membalikkan list terlebih 
dahulu dengan Reverse(l) dan kemudian memeriksanya dengan 
check_sorted(), tetapi kode ini tidak akan berfungsi.
Hasil yang diharapkan adalah "Error" karena metode 
sorted() yang Anda coba gunakan dalam fungsi check_sorted()
sebenarnya tidak ada, dan metode reverse() hanya mengubah
list tanpa mengembalikan hasil yang perlu diperiksa.

'''

# 37. Choose the correct statement regarding the dictionary.
# answer:
# Dictionary key-value pairs can be accessed using dictionary keys
# Dictionary can hold or store more than one key-value pair with the same values after the code is executed
# Dictionary are mutable


# 38. On which among the following lists, the sort() function does not raise an error.
a = [1, 2, 3, 4, '1', '2', '3', '4']
b = [1.0, 2.0, 3.0, 4.0, 1, 2, 3, 4]
c = ['1', '2', '3', '4', 'a', 'b', 'c', 'd']

# print(a.sort())  # b c d


# 39. In python, the identifiers are case sensitives or not.
# answer: Yes

# 40. Choose the correct output of the followong code: -
# print(math.factorial('S'))
# answer: TypeError
