import math
import test3

# 1. Choose the correct output of the following code: -
# class A:
#     num = 0

#     def __str__(self):
#         A.num = A.num + 1
#         return str(A.num)


# class B(A):
#     def __init__(self):
#         super().__init__()


# obj = A()
# print('A(): ', obj)  # 1
# print('A(): ', obj)  # 2
# print('B(): ', B())  # 3
# answer: 1 2 3


# 2. Choose the correect statement from the following.A
# answer:

''' 
print("-%07d" % 555.55)
print("-%07d" % 555)

print("-%02d" % 555.55)
print("-%2d" % 555.55)

print("-%02d" % 555.55)
print("-%02d" % 555) 
'''

# 3. Which among the following code when executed results
# in '24.0' as the output.
# answer :
# print(10.0//2*3+9)
# print(10/2*3+9)
# print(10//2.0*3+9)


# 4. Choose the correct statement regarding the following code: -
# class Car:
#     def __init__(self):
#         self.price = 2000
#         self.__No_Seats = 4

#     def details(self):
#         print(self.price)
#         print(self.__No_Seats)

#     class a:
#         pass


# obj = Car()
# obj.details  # karna ngk pake tanda () jadi ngk kecetak nilainya
# answer : The code will work fine and does not print anything


# 5. If they sys.txt file contains the 3 lines,
# 1st line 'Welcome'
# 2st line 'To Python'
# 1st line 'Programming'
# What will be the output of the following code: -
# file = open('sys.txt', 'r')
# file.readline()  # skip baris 1
# file.readline()  # skip baris 2
# file.readline()  # skip baris 3
# print(file.readline())  # cetak baris 4
# file.close()

# answer: The code will work fine and does not print any value.


# 6. Consider the following code is written in 'test_a.py' file.
# A = "A"
# _B = "B"
# __C = "C"

# Consider the following code is written in 'test_b.py' file.
# print(A)
# print(_B)
# print(__C)

# Both 'test_a.py and 'test_b.py' files are in the same folder.
# Choose the correct statements from the following when 'test_b.py file is executed as the main file: -
# answer
'''
print(A)
print(_B) error
print(__C) error
'''

# 7. Fill the blank, So that the below code will print 3Oranges
# a = str(3) + "Oranges"
# print(a)


# 8. Which of the following will raise the Syntax Error?
# answer : print(`Java`)


# 9. Fill the blank, So that the below code will print 'JAVA': -
# small = "java"
# big = ""
# for i in small:
#     big += chr(ord(i)-32)
# print(big)
# answer : -32

# 10. Choose the correct output of the following code: -
# text = "Certified Associate in Python Programming"
# x = text.split('i')
# for c in x:
#     print(c, end=' ')


# 11. Consider the following code is written in test1.py file.
# class List:
#     _name = "List"

#     def __init__(self):
#         self._l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         for i in range(0, len(self._l)):
#             if self._l[i] % 2 == 0:
#                 self._l[i] = self._l[i]/2


# Consider the follwing code is written in test2.py file.
# class List1(test3.List):
#     def __init__(self):
#         super().__init__()
#         print("One: ", self._l)
#         print("Two: ", test3.List._name)


# List1()
# answer:
# One: [1,1.0,3,2.0,5,3.0,7,4.0,9,5.0]
# Two: List


# 12. Choose the correct output of the following code: -
# print(math.floor(5.45))
# print(math.floor(-5.45))
# answer:
# 5
# -6

'''
breakdown
math.floor untuk membulatkan bilangan desimal ke bawah menjadi 
bilangan bulat. Mari kita bahas perinciannya:
print(math.floor(5.45)): Ini mengambil angka desimal positif 
5.45 dan membulatkannya ke bawah menjadi bilangan bulat terdekat 
yang lebih kecil atau sama dengan 5.45. Hasilnya adalah 5.
print(math.floor(-5.45)): Ini mengambil angka desima l negatif 
-5.45 dan juga membulatkannya ke bawah menjadi bilangan bulat 
terdekat yang lebih kecil atau sama dengan -5.45. Hasilnya adalah -6.
Hasil ini terjadi karena math.floor selalu membulatkan angka 
desimal ke bilangan bulat yang lebih rendah (lebih kecil) dari
angka desimal tersebut. Sebagai catatan, hasilnya selalu merupakan
bilangan bulat, bahkan jika angka desimal yang diberikan adalah 
bilangan bulat negatif.

Bulatkan bilangan desimal ke atas
math.ceil yang disediakan oleh modul math di Python. 
Fungsi math.ceil akan selalu membulatkan angka desimal ke 
bilangan bulat yang lebih besar atau sama dengan angka desimal 
tersebut.

'''
# 13. Choose the correct output of the following code : -
# try:
#     print("Hello")
# except:
#     print("Error is Code")
# else:
#     print("No Error in Code")
# finally:
#     print("finally")

# answer:
# Hello
# No Error Code
# finally


# 14. Choose the correct output of the following code: -
# A = [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]]
# print(A)
# answer : [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]]

# 15. If the file 'sys.txt' already contain the text "Welcome"
# then what will be the text present in the file after the execution
# of the following code: -

# file = open('sys.txt', 'a')
# file.write("To programing")
# file.close()
# answer: WelcomeTo Programming


# 16. Choose the correct output of the following code: -
# not(10 != 10) and bool(10 != 10)
# answer : No Output / False


# 17. Which among the following are the correct ways to delete the length attribut from the Box class
class Box:
    def __init__(self):
        self.length = 3
        self.height = 9
        self.breadth = 5


obj = Box()
# answer:
# delattr(obj, 'length')
# or
# del obj.length


# 18. Which among the following can not be used to create a variable?
# answer = in


# 19. Choose the correct output of the following code: -
class Car:
    speed = 10

    def BoostSpeed():
        result = 10*Car.speed
        return result


# print(Car.BoostSpeed())
# answer: 100


# 20. Choose the correct output of the following code: -
sets = {0, 0, 1, 4, 6}
print(sets)
# answer: {0, 1, 4, 6}

# 21. Choose the correct output of the following code: -
T1 = (1)
T2 = (3, 4)
T3 = T1+T2
print(T3)  # Error
# answer: Error (TypeError: unsupported operand type(s) for +: 'int' and 'tuple')

'''
breakdown
 "TypeError: unsupported operand type(s) for +: 'int' and 'tuple'", terjadi karena Anda mencoba menjumlahkan dua objek dengan tipe data yang tidak dapat dijumlahkan secara langsung, yaitu integer (int) dan tuple. Mari kita jelaskan secara terperinci mengapa pesan error ini muncul.

Pertama, mari kita periksa bagaimana T1 dan T2 didefinisikan:

T1 adalah sebuah tuple dengan satu elemen, yaitu 1. Ini adalah contoh dari tuple dengan satu elemen.
T2 adalah sebuah tuple dengan dua elemen, yaitu 3 dan 4.
Kemudian, Anda mencoba menjumlahkan T1 dan T2 dalam baris kode ini:

python
Copy code
T3 = T1 + T2
Mari kita bahas mengapa pesan error muncul:
Saat Anda menjumlahkan dua variabel tuple, Python akan mencoba untuk menggabungkannya. Dalam hal ini, 
Python mencoba menggabungkan T1 dan T2.
Namun, masalah terjadi karena T1 adalah sebuah tuple yang berisi satu elemen, yaitu integer 1, sedangkan T2 
adalah sebuah tuple dengan dua elemen, yaitu 3 dan 4.
Python tidak dapat secara otomatis menggabungkan tuple dengan integer karena operasi penambahan yang dijelaskan 
dalam kode Anda adalah operasi penjumlahan matematika.
Oleh karena itu, Python menganggap bahwa Anda mencoba menjumlahkan integer (1 dari T1) dengan tuple (T2), yang 
tidak valid dalam hal aritmatika Python.
Inilah sebabnya mengapa Anda mendapatkan pesan error "TypeError: unsupported operand type(s) for +: 'int' and 'tuple'" 
yang mengindikasikan bahwa operasi penjumlahan antara tipe data int dan tuple tidak didukung.

Solution
Untuk memperbaiki kesalahan ini, Anda perlu memastikan bahwa Anda menjumlahkan objek dengan tipe data yang sesuai. 
Jika Anda ingin menggabungkan T1 dan T2, Anda bisa menggunakan operator + untuk menggabungkan dua tuple atau mengubah 
T1 menjadi tuple dua elemen dengan menambahkan koma setelah angka 1, sehingga T1 menjadi (1,). Berikut contoh perbaikan 
kode:
T1 = (1,)
T2 = (3, 4)
T3 = T1 + T2
print(T3)  # Output: (1, 3, 4)
Dengan ini, Anda dapat menjumlahkan dua tuple dengan benar dan mendapatkan hasil (1, 3, 4).
'''

# 22. Fill the blank, So that the below code prints
# Language is: Python


class language:
    def __init__(self):
        self.name = "Java"

    def call_me(self):
        print("Language is: ", self.name)


obj = language()
______________
obj.call_me()
# answer:
# setattr(obj,'name',"Python") # Language is: Python
# obj.name = "Python" # Language is: Python

'''
breakdown
Fungsi setattr sebenarnya hanya memiliki dua parameter. Parameter tersebut adalah:
Objek: Ini adalah objek yang atributnya akan diubah.
Nama Atribut: Ini adalah nama atribut yang akan diubah.
Nilai Atribut (opsional): Ini adalah nilai baru yang akan diberikan pada atribut.

'''

# 23. Choose the correct output of the following code: -
try:
    print("Hello")
finally:
    print("End of Code")
# answer:
# Hello
# End of Code


# 24. Choose the correct output of the following: -
x = 50


def Calculate():
    global x
    x = 20
    print("Calculation inside of a function:", x*2+5-9)


Calculate()
print("Calculate outside a function:", x*2+5-9)
# answer:
# Calculation inside of a function: 36
# Calculate outside a function: 36

'''
breakdown
Variabel x didefinisikan di luar fungsi sebagai variabel global dan diatur ke nilai 50.
Kemudian, ada fungsi yang disebut Calculate. Di dalam fungsi ini, kita mendeklarasikan bahwa 
kita akan menggunakan variabel x yang ada di luar fungsi (variabel global) dengan menggunakan kata 
kunci global. Ini berarti bahwa kita akan merujuk ke variabel global x dalam fungsi ini.
Di dalam fungsi Calculate, variabel x diberi nilai baru yaitu 20.
Selanjutnya, ada pernyataan print yang mencetak hasil perhitungan yang melibatkan variabel x. Hasil 
perhitungan adalah x*2 + 5 - 9. Di dalam fungsi ini, nilai x adalah 20 (nilai yang diatur di dalam fungsi), 
sehingga hasil perhitungannya adalah 36. Oleh karena itu, pesan "Calculation inside of a function: 36" akan dicetak.
Kemudian, fungsi Calculate() dipanggil.
Setelah pemanggilan fungsi, kita mencetak hasil perhitungan yang melibatkan variabel x lagi di luar fungsi. 
Karena kita menggunakan variabel global x, nilai yang digunakan adalah yang telah diubah di dalam fungsi, yaitu 20.
Hasil perhitungan tetap sama, yaitu x*2 + 5 - 9, yang menghasilkan 36. Oleh karena itu, pesan "Calculate outside a 
function: 36" akan dicetak.
Jadi, meskipun kita mengubah nilai variabel x di dalam fungsi, karena kita menggunakan variabel global x 
dengan kata kunci global, perubahan tersebut berlaku di seluruh program, dan nilai x yang diubah akan digunakan 
baik di dalam maupun di luar fungsi.

'''

# 25. Choose the correct output of the following code: -
i = 6
while True:
    if i % 0O14 == 0:
        break
    i += 1
print(i)
# answer: 12
'''
breakdown
Variabel i didefinisikan dengan nilai awal 6.
Loop while dibuka dengan kondisi True, yang berarti loop akan terus berjalan sampai kondisi dalam loop 
dipenuhi sehingga kita perlu menggunakan break untuk keluar dari loop.
Di dalam loop, ada sebuah kondisi if yang memeriksa apakah sisa hasil bagi (modulus) dari i dengan 014 
(angka oktal) sama dengan 0. Dalam notasi oktal, angka 014 adalah desimal 12.
Kita mencoba mencari nilai i yang, jika dimodulus dengan 12 (0O14 dalam notasi oktal), hasilnya akan menjadi 0.
Kondisi dalam if di atas akan selalu salah pada nilai i awal yang adalah 6, karena hasil dari 6 mod 12 
bukanlah 0. Oleh karena itu, pernyataan break tidak akan dieksekusi dan program akan terus berjalan dalam loop.
Setiap kali loop berjalan, nilai i akan ditingkatkan dengan 1 menggunakan pernyataan i += 1.
Loop akan terus berjalan hingga i mencapai nilai 12. Pada saat itu, 12 mod 12 adalah 0, yang memenuhi kondisi dalam if. 
Sehingga, pernyataan break dieksekusi, dan loop dihentikan.
Setelah keluar dari loop, program mencetak nilai i. Karena i terakhir adalah 12, hasil cetakan adalah 12.

How to count?
Misalkan kita memiliki bilangan oktal 014 (berdasarkan notasi oktal).

Tulis bilangan oktal: 014
Tentukan nilai desimal dari setiap digit oktal:
Digit kanan: 4 (di posisi 0)
Digit kiri: 1 (di posisi 1)
Hitung nilai desimalnya:
Nilai desimal dari digit kanan adalah 4 * 8^0 = 4 * 1 = 4.
Nilai desimal dari digit kiri adalah 1 * 8^1 = 1 * 8 = 8.
Jumlahkan nilai desimal dari kedua digit: 4 + 8 = 12.
Jadi, bilangan oktal 014 setara dengan bilangan desimal 12. 
Dalam notasi desimal, bilangan tersebut adalah 12.
'''

# 26. Which among the following operator have the highest precedence?
# answer: **

'''
breakdown
"precedence" atau prioritas adalah aturan yang menentukan urutan operasi matematika mana
yang dievaluasi terlebih dahulu dalam sebuah ekspresi. Python mengikuti aturan urutan operasi 
matematika yang dikenal sebagai "precedence rules" atau "rules of precedence." Dengan aturan ini, 
operasi dengan prioritas lebih tinggi akan dievaluasi terlebih dahulu daripada operasi dengan prioritas 
lebih rendah.
'''

# 27. Choose the correct output of the following code: -


class Parent:
    def __init__(self, age):
        self.age = age

    def get_parent_age(self):
        return self.age


class Child(Parent):
    def __init__(self):
        super().__init__(55)
        self.age = super().get_parent_age() - 25

    def get_child_age(self):
        return self.age


obj = Child()
print("Child age is: ", obj.get_child_age())
print("Parent age is: ", obj.get_parent_age())
# answer :
# Child age is:  30
# Parent age is:  30

'''
breakdown
Kelas Parent:

Kelas Parent memiliki satu atribut age yang diinisialisasi melalui konstruktor __init__.
Terdapat metode get_parent_age yang mengembalikan nilai dari atribut age.
Kelas Child:
Kelas Child adalah kelas anak dari kelas Parent, yang berarti Child mewarisi sifat dan metode dari Parent.
Dalam konstruktor __init__ dari kelas Child, Anda menggunakan super().__init__(55) untuk memanggil konstruktor kelas 
Parent dan menginisialisasi atribut age dengan nilai 55.
Kemudian, Anda menginisialisasi atribut age lagi dengan mengambil nilai dari super().get_parent_age() (nilai 55 yang 
diwarisi dari kelas Parent) dan mengurangkan 25 dari nilai tersebut. Jadi, self.age dalam kelas Child diatur menjadi 55 - 25,
yaitu 30.
Terdapat metode get_child_age yang mengembalikan nilai dari atribut age dalam kelas Child.
Objek obj:
Anda membuat objek obj dari kelas Child.
Pencetakan hasil:
Anda mencetak usia anak (Child age is: 30) dengan memanggil metode get_child_age dari objek obj. Ini menghasilkan nilai 30,
yang sesuai dengan nilai atribut age dalam kelas Child.
Anda juga mencetak usia orangtua (Parent age is: 30) dengan memanggil metode get_parent_age dari objek obj. Ini juga
menghasilkan nilai 30, yang merupakan nilai dari atribut age dalam kelas Parent. Karena Child mewarisi atribut age 
dari Parent, keduanya memiliki nilai yang sama.
'''


# 28. Choose the correct output of the following code: -
class A:
    def __init__(self):
        print(type(self))


class B(A):
    def __init__(self):
        super().__init__()
        print(type(self))


B()
# answer :
# <class '__main__.B'>
# <class '__main__.B'>


'''
breakdown
Keduanya merujuk ke kelas B karena objek yang diciptakan menggunakan B(), yang berarti objek tersebut 
adalah instansi dari kelas B. Saat Anda membuat objek dengan B(), Anda sebenarnya membuat sebuah instansi 
dari kelas B, dan objek tersebut memiliki sifat dan metode yang dimiliki oleh kelas B.
Pada dasarnya, saat Anda membuat objek menggunakan B(), Anda membuat objek dari kelas B dan menjalankan 
konstruktor kelas B, yang mencetak tipe objek self dalam kelas B.
Hal ini merupakan prinsip dasar warisan atau inheritance dalam pemrograman berorientasi objek, di mana 
kelas anak (B) mewarisi sifat dan metode dari kelas induk (A) dan memiliki kemampuan untuk mengekstend 
atau mengubah perilaku kelas induk. Dalam hal ini, meskipun Anda memanggil super().__init__() untuk 
menjalankan konstruktor kelas induk (A), objek yang dihasilkan tetap berada dalam kelas B dan mengacu 
pada tipe objek kelas B.

Dalam konsep warisan (inheritance), ketika Anda membuat objek dari kelas anak (subclass), objek 
tersebut adalah instansi dari kelas anak, dan secara default, ia akan mengikuti sifat dan metode 
yang didefinisikan dalam kelas anak. Hal ini sesuai dengan prinsip bahwa kelas anak mewarisi sifat
dan metode dari kelas induk, tetapi kelas anak juga dapat mengganti atau menambahkan perilaku sesuai kebutuhan.
Jika Anda ingin objek kelas anak untuk merujuk pada tipe kelas induk, Anda masih dapat melakukannya 
dengan mengakses metode atau atribut dari kelas induk. Misalnya, dalam metode kelas anak, Anda dapat 
mengakses metode dari kelas induk dengan menggunakan super().
Namun, secara umum, ketika Anda membuat objek dari kelas anak, objek tersebut dianggap sebagai objek 
kelas anak dan merujuk pada tipe kelas anak, kecuali Anda secara eksplisit mengakses sifat atau metode 
dari kelas induk.
'''

# 29. Choose the correct output of the following code: -
a = '62' + '14'
print(a, type(a))

# answer:
# 6214 <class 'str'>


# 30. Choose the correct ways to call the constructor explicitly.
class language:
    def __init__(self):
        self.name = "Java"
        print(self.name)

# answer:
# language().__init__()
# language.__init__(language())


'''
breakdown
Dalam Python, konstruktor (metode __init__) biasanya dipanggil secara implisit ketika 
Anda membuat objek dari suatu kelas. Namun, ada cara untuk memanggil konstruktor secara
eksplisit jika diperlukan. Di bawah ini adalah dua cara yang benar untuk memanggil konstruktor 
dari kelas language secara eksplisit:
language().__init__(): Ini adalah cara yang sah untuk memanggil konstruktor kelas language secara 
eksplisit. Dalam hal ini, Anda membuat objek dari kelas language dengan language() dan kemudian 
memanggil konstruktor __init__ objek tersebut dengan ().__init__().
language.__init__(language()): Dalam cara ini, Anda secara langsung memanggil metode __init__ dari 
kelas language dengan objek language(). Ini membuat objek dari kelas language dengan language(), 
dan kemudian Anda memanggil konstruktor __init__ dari objek tersebut dengan .__init__().
Kedua cara di atas akan memanggil konstruktor kelas language dan menjalankan kode di dalamnya. 
Namun, penting untuk diingat bahwa memanggil konstruktor secara eksplisit seperti ini jarang 
dibutuhkan dalam praktek sehari-hari, dan konstruktor biasanya dipanggil secara implisit saat 
Anda membuat objek dari kelas.
'''


# 31. Choose the correct output of the below code: -
class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


print(A.__bases__)
print(B.__bases__)
print(C.__bases__)
# answer:
# (<class 'object'>,)
# (<class '__main__.A'>,)
# (<class '__main__.B'>, <class '__main__.A'>

'''
breakdown
secara terperinci:
Kelas A:
Kelas A adalah kelas dasar (base class) yang tidak memiliki definisi tambahan. 
Itu hanya berisi pernyataan pass, yang menunjukkan kelas kosong.
Kelas B:
Kelas B adalah kelas anak (subclass) dari kelas A. Ini berarti bahwa kelas B mewarisi 
semua sifat dan metode dari kelas A.
Kelas C:
Kelas C adalah kelas anak dari kelas B dan juga kelas A. Ini berarti bahwa kelas C mewarisi 
sifat dan metode dari kedua kelas B dan A. Dalam konstruksi kelas C, B dan A disebutkan dalam 
urutan seperti ini: class C(B, A). Urutan ini menentukan urutan pengecekan pewarisan dalam Python 
(MRO, Method Resolution Order).

Penjelasan:
Kelas A memiliki kelas dasar yang disebut <class 'object'>. Ini karena dalam Python,
semua kelas adalah turunan dari kelas dasar object.
Kelas B adalah turunan dari kelas A, sehingga kelas dasar dari B adalah A.
Kelas C adalah turunan dari kelas B dan juga kelas A. Oleh karena itu, kelas dasar 
dari C adalah B dan A dalam urutan tersebut.

Atribut __bases__ adalah atribut bawaan dalam Python yang digunakan untuk mendapatkan 
informasi tentang kelas dasar (superclass) dari suatu kelas. Dengan atribut __bases__, 
Anda dapat melihat kelas mana yang menjadi kelas dasar dari suatu kelas dalam hierarki pewarisan.
Atribut __bases__ adalah bagian dari objek kelas dan digunakan untuk inspeksi hierarki pewarisan 
kelas. Ketika Anda mengaksesnya, Anda akan mendapatkan tupel yang berisi semua kelas dasar dari 
kelas tersebut. Setiap elemen dalam tupel adalah objek kelas yang mewakili kelas dasar.
Misalnya, jika Anda memiliki kelas Child yang mewarisi dari kelas Parent, Anda dapat menggunakan 
Child.__bases__ untuk melihat bahwa kelas dasar dari Child adalah Parent.

'''

# 32. Choose the correct statement: -


# 33. What is the output of the following program, when the below code is executed in python version 3.6?
top_speed = {"audi_r8": 320, "audi_a4": 120, "audi_q5": 147}
for (key, values) in top_speed .items():
    print(key, values, end=" ")
# answer:
# All of the above


# 34. Choose the correct output of the following code: -
speed = {320, 120, 200, 100}
print(speed)
# answer:
# {320, 100, 120, 200}

'''
breakdown
Anda sebenarnya membuat sebuah himpunan (set) dalam Python. Himpunan adalah koleksi elemen yang 
bersifat unik dan tidak berurutan. Dalam hal ini, Anda membuat himpunan yang berisi 
empat elemen: 320, 120, 200, dan 100. Namun, himpunan tidak menjamin urutan tertentu saat Anda mencetaknya.
Sebagai akibatnya, ketika Anda mencetak himpunan speed, urutan elemennya tidak dapat 
diprediksi dan bisa muncul dalam urutan yang berbeda-beda setiap kali program dijalankan. 
Hasil cetaknya mungkin mirip dengan yang Anda sebutkan dalam jawaban (yaitu {320, 100, 120, 200}), 
tetapi urutan elemen dalam himpunan tidak memiliki arti khusus.
Sebagai contoh, hasil cetakan yang berbeda mungkin adalah {320, 120, 200, 100} atau bahkan 
urutan yang sepenuhnya berbeda, tetapi itu semua adalah representasi yang valid dari 
himpunan {320, 120, 200, 100}.
'''


# 35. Fill the blank so that the below code will print '2 3'.
class Parent:
    def __init__(self):
        self.a = 2


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.b = 3


obj = Child()
print(obj.a, obj.b)
# answer:
#  super().__init__()
#  Parent.__init__(self)


# 36. Choose tge correct output of the following code:  -
# ceil itu pembulatan ke atas klo floor yg pembulatan ke bawah
print("Output : ", math.ceil(5.45))
# answer:
# Output :  6


# 37. Choose the correct output of the following code: -
print(math.factorial(4.5))
# answer:
# ValueError: factorial() only accepts integral values


# 38. What is the correct output of the following code: -
class Add:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def __str__(self):
        return self.num1 + self.num2


obj = Add(3, 4)
print(obj)
# answer:
# Error

'''
breakdown
Kode yang Anda berikan mencoba mendefinisikan sebuah kelas Add yang memiliki konstruktor (__init__)
untuk menginisialisasi dua atribut, num1 dan num2, serta metode __str__ yang mencoba mengembalikan 
hasil penjumlahan num1 dan num2. Kemudian, Anda mencoba membuat objek dari kelas Add dan mencetak objek 
tersebut. Namun, ada sebuah masalah dalam kode ini, yang akan menghasilkan error.
Masalahnya adalah dalam metode __str__. Metode __str__ seharusnya mengembalikan string (tipe data str),
tetapi Anda mengembalikan hasil penjumlahan num1 dan num2, yang akan menghasilkan tipe data int. Ini 
adalah konflik tipe data yang menyebabkan kesalahan.

solution
class Add: 
    def __init__(self, x, y):
        self.num1 = x 
        self.num2 = y

    def __str__(self):
        return str(self.num1 + self.num2) # tambah str() agar int diubah ke string

obj = Add(3, 4)
print(obj)
'''


# 39. How many except statements can we put below the try block?
# Note: -Do not consider the default except block for the calculation.
# answer: As many except block as we want.


# 40. Choose the correct output of the following code: -
class Student:
    Class = 0

    def __init__(self, x, y, z):
        self.name = x
        self.roll_name = y
        Student.Class = z


obj = Student("Mia", 4578, 10)
print(obj.__dict___)
# answer:
# {'name': 'Mia', 'roll_name': 4578}

'''
breakdown
Kelas Student memiliki tiga atribut:

Class: Ini adalah atribut kelas yang diinisialisasi dengan nilai 0.
name: Ini adalah atribut instance yang diinisialisasi dalam konstruktor dengan nilai x.
roll_number: Ini adalah atribut instance yang diinisialisasi dalam konstruktor dengan nilai y.
Dalam konstruktor (__init__) kelas Student, Anda menginisialisasi atribut name dan roll_number 
dengan nilai yang diberikan saat membuat objek.
Kemudian, Anda mengatur nilai atribut kelas Class dengan nilai z. Ini akan mengubah nilai atribut 
kelas Class menjadi 10.
Ketika Anda mencetak obj.__dict__, Anda mendapatkan dictionary yang berisi atribut-instance dan 
nilai-nilai yang sesuai. Dalam kasus ini, dictionary ini akan berisi {'name': 'Mia', 'roll_number': 4578}.


kenapa z tidak di tampilkan?
Kemungkinan besar kesalahan dalam menampilkan nilai z adalah pada pemanggilan atribut. 
Ketika Anda mencetak obj.__dict__, itu hanya akan mencetak atribut-instance yang ada pada objek 
obj, tetapi tidak akan mencetak atribut kelas seperti Class.

solution:
print(Student.Class)
Dengan demikian, Anda akan dapat menampilkan nilai dari atribut kelas Class yang diubah dalam konstruktor 
saat Anda membuat objek.
Jika Anda ingin melihat atribut kelas yang ada dalam kelas Student, Anda bisa mencetak Student.__dict__.
'''
