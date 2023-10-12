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
# answer : No Output


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
T2 = (3,4)
T3 = T1+T2
print(T3) # Error
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
        print("Language is: ",self.name)
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
    print("Calculation inside of a function:",x*2+5-9)
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
    if i%0O14 == 0:
        break
    i += 1
print(i)
# answer: 12
'''
breakdown
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







