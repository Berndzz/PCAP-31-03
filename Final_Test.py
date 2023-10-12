''' 
1. The meaning of the keyword "argument: is determined by:
answer: the argument's name specified along with its value
'''

# 2. Which of the following sentences is true?
str1 = 'string'
str2 = str1[:]  # slicing dengan mengambil seluruh nilai di string tersebut
# print(str1 == str2)
# print(str1)  #string
# print(str2)  #string
# answer: str1 and str2 are different names of the same string


# 3. an operator able to check wheather two values are equel, coded as
# class A:
#     def __init__(self, x):
#         self.a = x


# o1 = A(10)
# o2 = A(10)
# print(o1 == o2)  # false
# print(o1 is o2)  # false
# print(o1 === o2) #error
# print(o1 = o2) #error
# answer : ==


# 4. The following the snippet:
# def f(par2, par1):
#     return par2 + par1

# print(f(par2=1,2)) #error
# answer: is erroneous


# 5. what value will be assigned to the x variable?
z = 2
y = 1
# count from left to right
x = y < z or z > y and y > z or z < y
# print(x) true
# answer: true
''' 
breakdown
Mari kita evaluasi ekspresi x:

a. y < z adalah True karena 1 kurang dari 2.
b. z > y juga True karena 2 lebih dari 1.
c. y > z adalah False karena 1 tidak lebih besar dari 2.
d. z < y adalah False karena 2 tidak kurang dari 1.

Sekarang, kita dapat menyusun ekspresi dengan operator logika sesuai dengan urutannya:

a. y < z or z > y menjadi True or True, yang mengembalikan True karena ada satu True di antara keduanya.
b. z > y and y > z menjadi True and False, yang mengembalikan False karena kedua operandnya harus True untuk menghasilkan True.
c. Karena True or False adalah True, maka hasil akhir dari ekspresi adalah True.
'''

# 6. What will be the output of the following snipet?
str = 'abcdef'
# def fun(s):
#     del s[2]
#     return s

# print(fun(str))
# answer: the program will cause an error


'''
breakdown

 string di Python bersifat immutable, yang berarti Anda 
 tidak dapat mengubah elemennya setelah dibuat.
 
 Hasilnya adalah Anda akan mendapatkan kesalahan berupa TypeError, 
 yang mengindikasikan bahwa string object 
 tidak mendukung operasi penghapusan elemen. 
 Oleh karena itu, pernyataan del s[2] akan menyebabkan error di sini.
 
 bagaimana jika tetap ngotot menghapus elemen menggunakan string?
 Misalnya, jika Anda memiliki string 'abcdef' dan ingin "menghapus"
 karakter 'c' dari string tersebut, Anda dapat melakukan ini dengan
 menggabungkan bagian sebelum 'c' dengan bagian setelah 'c' seperti ini:
 
'''
# Solusi
original_string = 'abcdef'
new_string = original_string[:2] + original_string[3:]
# original_string[:2] ab
# original_string[3:] def
# print(new_string) abdef


# 7. What will be the output of the following piece of code?
x, y, z = 3, 2, 1
z, y, x = x, y, z
# print(x,y,z) #1 2 3
# answer: 1 2 3

'''
breakdown

Nilai x (3) disimpan di variabel z.
Nilai y (2) disimpan di variabel y (jadi tidak ada perubahan pada nilai y).
Nilai z (1) disimpan di variabel x.
Jadi, setelah baris kode dijalankan, nilai-nilai variabel akan menjadi seperti ini:

x akan berisi 1
y akan berisi 2
z akan berisi 3

Hasil cetakan adalah 1 2 3, sesuai dengan nilai-nilai yang telah dipertukarkan.
'''

# 8. What will be the output of the following snippet?
# a = True
# b = False
# a = a or b  # true
# b = a and b  # false
# a = a or b  # true
# print(a,b)
# answer: True False


# 9. What will be the output of the following snippet?
# def fun(x):
#     return 1 if x % 2 != 0 else 2


# print(fun(fun(1))) # 1
# answer: 1
'''
breakdown
Pertama-tama, Anda mendefinisikan sebuah fungsi bernama fun dengan satu parameter x. Fungsi ini mengembalikan 1 jika x adalah bilangan ganjil (jika x % 2 != 0 adalah True), dan mengembalikan 2 jika x adalah bilangan genap (jika x % 2 != 0 adalah False). Ini adalah operator ternary yang digunakan untuk menggantikan pernyataan if-else dalam satu baris.

Kemudian, Anda memanggil fungsi fun dengan argumen 1. Karena 1 adalah bilangan ganjil (karena 1 % 2 adalah 1 != 0), maka pemanggilan pertama fun(1) mengembalikan 1.

Selanjutnya, Anda memanggil fungsi fun lagi dengan hasil dari pemanggilan pertama, yaitu 1. Karena 1 adalah bilangan ganjil, pemanggilan kedua fun(1) juga mengembalikan 1.

Akhirnya, Anda mencetak hasil dari pemanggilan kedua fun(1), yang adalah 1.
'''

# 10. What will be the output of the following line?
# print(len((1,))) #len = mengembalikan jumlah elemen(panjang elemen)
# answer: 1
'''
breakdown
Anda memiliki tuple yang didefinisikan sebagai (1,). Ini adalah tuple dengan satu elemen, yaitu angka 1. 
Perhatikan bahwa ada tanda koma setelah angka 1. Tanda koma ini penting untuk membedakan tuple dengan ekspresi 
dalam tanda kurung biasa.

Anda menggunakan fungsi len() untuk menghitung panjang (jumlah elemen) dari tuple ini. Fungsi len() 
mengembalikan jumlah elemen dalam objek yang diberikan.

Karena tuple ini hanya memiliki satu elemen, yaitu angka 1, maka hasil dari len((1,)) adalah 1.

'''

# 11. What wil be the output of the following piece of code?
d = {1: 0, 2: 1, 3: 2, 0: 1}  # dictionary style
x = 0
for y in range(len(d)):
    x = d[x]
# print(x)
# answer: 0

'''
breakdown

d adalah sebuah dictionary yang memiliki empat pasangan key-value:

1:0
2:1
3:2
0:1
x awalnya diinisialisasi dengan nilai 0.

Loop for y in range(len(d)):

len(d) mengembalikan jumlah pasangan key-value dalam dictionary d, yang dalam hal ini adalah 4.
Loop akan melakukan iterasi 4 kali (y akan berubah dari 0 hingga 3), dan pada setiap iterasi, x akan 
diperbarui dengan nilai yang ada di dalam dictionary d menggunakan key x.
Iterasi 1:
y = 0
x saat ini adalah 0, jadi kita mengambil nilai d[0], yang bernilai 1.
Sehingga, x sekarang adalah 1.

Iterasi 2:
y = 1
x saat ini adalah 1, jadi kita mengambil nilai d[1], yang bernilai 0.
Sehingga, x sekarang adalah 0.

Iterasi 3:
y = 2
x saat ini adalah 0, jadi kita mengambil nilai d[0], yang bernilai 1.
Sehingga, x sekarang adalah 1.

Iterasi 4:
sy = 3
x saat ini adalah 1, jadi kita mengambil nilai d[1], yang bernilai 0.
Sehingga, x sekarang adalah 0.
'''


# 12. What will be the output of the following piece of code if the user enters
# two lines containing 1 and 2 respectively?

# y = input() # tipe string
# x = input()
# print(x+y) # string + string itu concat(gabung) bukan adding so, 1+2 = 21
# answer: 21


# 13. What will be the output of the following piece of code?
# print("a","b","c",sep="'")
# answer: a'b'c


# 14. What will be the output of the following piece of code?
v = 1+1 // 2+1 / 2+2  # count by left to right
# print(v)
# answer: 3.5

# 15. What will be the output of the following code?
t = (1,)  # this tuple style t=(1,) and this not t=(1)
t = t[0] + t[0]
# print(t)
# answer: 2

'''
breakdown

t = (1,): Ini adalah cara yang benar untuk membuat tupel dengan satu elemen, yaitu angka 1. 
Tanda koma setelah angka 1 menunjukkan bahwa ini adalah tupel.

t = (1): Ini sebenarnya bukan tupel, tetapi hanya ekspresi dalam tanda kurung biasa.
Python akan memperlakukannya sebagai angka 1 dalam kasus ini.

Jadi, tanda koma setelah elemen tunggal digunakan untuk menghindari ambiguitas dalam 
sintaksis Python, dan inilah sebabnya mengapa t = (1, ) tidak menghasilkan error.
'''

# 16. What will be the output of the following piece of code?
x = 16
# while x > 0:
#     print('*',end='')
#     x //=2
# answer: *****


# 17. What will be the output of the following snippet?
# d = {'one':1 ,'three':3, 'two':2}
# for k in sorted(d.values()): #sorted asc , kecil ke besar
#     print(k,end=' ')
# answer: 1 2 3

'''
breakdown

d.values() adalah sebuah metode yang digunakan untuk mengambil semua nilai (values) 
yang terdapat dalam sebuah kamus (dictionary) Python. Metode ini mengembalikan tampilan (view) dari 
semua nilai-nilai tersebut dalam bentuk objek tampilan yang dapat diiterasi.

'''


# 18. What will be the output of the following snippet?
# print(len([i for i in range(0,-2)])) # list comprehensions
# answer: 0

'''
breakdown

Ekspresi list comprehension ini adalah [i for i in range(0, -2)]. Dalam ekspresi ini, Anda mencoba membuat daftar (list) yang 
berisi nilai-nilai dari iterasi melalui rentang dari 0 hingga -2. Namun, perhatikan bahwa rentang ini tidak akan menghasilkan 
nilai apa pun, karena tidak ada bilangan bulat yang kurang dari 0 dan lebih besar dari -2.

Ketika Anda mencoba menjalankan list comprehension ini, hasilnya adalah sebuah daftar kosong [] karena 
tidak ada nilai yang dapat dimasukkan ke dalam daftar.

Selanjutnya, Anda menggunakan fungsi len() untuk mengukur panjang (jumlah elemen) dari daftar yang dihasilkan. Karena daftar 
tersebut kosong, maka panjangnya adalah 0.

Jadi, hasil akhir dari kode ini adalah 0. Ini menunjukkan bahwa ekspresi [i for i in range(0, -2)] tidak 
menghasilkan elemen apa pun dalam daftar, dan panjang daftar tersebut adalah 0. 
'''

# 19. Which of the following lines properly invokes the function defined as:
# def fun(a,b,c=0)?
# answer: fun(a=1,b=0,c=0)


# 20. What will be the output of the following snippet?
l = [1, 2, 3, 4]
l = list(map(lambda x: 2*x, l))
# print(l) # [2,4,6,8]
# answer: 2,4,6,8


# 21. How many stars will the following snippet send to the console?
# i = 4
# while i > 0:
#     i -=2
#     print('*')
#     if i == 2:
#         break
# else:
#     print('*')
# answer: * or 1


# 22. What will be the output of the following snippet?
t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
# print(t)
# answer: 3

'''
breakdown
Slicing -2:-1 akan menghasilkan tupel baru yang berisi elemen dengan indeks -2, 
yaitu 3. Jadi, t akan menjadi (3,).

Kemudian, kita kembali melakukan slicing pada tupel t, kali ini dengan indeks -1. 
Ini berarti kita mencoba mengambil elemen dengan indeks terakhir dari tupel. 
Pada saat ini, tupel t hanya memiliki satu elemen, yaitu 3. Jadi, slicing -1 akan 
menghasilkan elemen 3 itu sendiri.

Terakhir, kita mencetak nilai t, yang sekarang hanya berisi 3.

Slicing dalam bahasa pemrograman Python menggunakan titik dua (:) sebagai pemisah antara indeks awal dan indeks akhir, bukan koma (,). 
Alasannya adalah karena pemisah koma (``,) digunakan untuk memisahkan elemen-elemen dalam struktur data seperti tupel, 
daftar, atau set. Sedangkan titik dua (:`) digunakan untuk mengindikasikan rentang indeks yang ingin Anda ambil dalam 
struktur data tersebut.

Misalnya, dalam kode (1, 2, 3, 4)[1:3], kita ingin mengambil elemen dari indeks 1 hingga 3 dalam tupel, 
sehingga kita menggunakan titik dua (:) sebagai pemisah. Jika Anda menggunakan koma (``,) 
seperti yang Anda tunjukkan dalam pertanyaan Anda (-2,-3), Python akan menganggap bahwa Anda 
mencoba membuat tuple baru dengan dua elemen, yaitu -2dan-3`, dan bukan melakukan slicing dalam tupel.
'''

# 23. What will be the output of the following snippet?
# d = {}
# d['2'] = [1,2]
# d['1'] = [3,4]
# for x in d.keys():
#     print(d[x][1],end="")
# answer: 24


'''
breakdown

Pertama, kita mendefinisikan sebuah kamus (dictionary) kosong dengan nama d menggunakan kurung kurawal {}.

Selanjutnya, kita menambahkan dua pasangan kunci-nilai ke dalam kamus d:

Kunci '2' dengan nilai [1, 2]
Kunci '1' dengan nilai [3, 4]
Setiap kunci merujuk pada sebuah daftar (list) yang berisi dua elemen.

Selanjutnya, kita melakukan iterasi melalui kunci-kunci dalam kamus d menggunakan perulangan for x in d.keys(). Di setiap iterasi, 
variabel x akan berisi satu kunci dari kamus d.

Di dalam perulangan, kita mencetak elemen kedua dari daftar yang terkait dengan kunci x menggunakan d[x][1], dan 
kita menggabungkan hasil cetakan ini dengan menggunakan end="". Ini berarti hasil cetakan dari setiap iterasi tidak 
akan diakhiri dengan baris baru (newline), sehingga semua hasil cetakan akan dicetak di samping.

Hasil dari perulangan ini adalah mencetak elemen kedua dari daftar yang terkait dengan setiap kunci dalam kamus d. Dalam 
hal ini, kita mencetak elemen kedua dari daftar [1, 2] (yaitu 2) dan kemudian elemen kedua dari daftar [3, 4] (yaitu 4).
'''


# 24. What will be the output of the following snippet?
def fun(d, k, v):
    d[k] = v


dc = {}
# print(fun(dc,'1','v'))
# answer: None

'''
breakdown
Pertama, Anda mendefinisikan sebuah fungsi dengan nama fun yang menerima tiga parameter:

d: Ini adalah kamus (dictionary) yang akan dimodifikasi.
k: Ini adalah kunci (key) yang akan digunakan untuk menambahkan atau memperbarui elemen dalam kamus d.
v: Ini adalah nilai (value) yang akan dihubungkan dengan kunci k dalam kamus d.
Dalam fungsi ini, Anda menetapkan nilai v ke kamus d menggunakan kunci k.

Selanjutnya, Anda membuat kamus kosong dengan nama dc menggunakan {}.

Kemudian, Anda memanggil fungsi fun dengan dc sebagai kamus, '1' sebagai kunci, dan 'v' sebagai nilai. Ini 
berarti Anda mencoba menambahkan elemen ke dalam kamus dc dengan kunci '1' dan nilai 'v'.

Fungsi fun kemudian mengeksekusi operasi untuk menambahkan atau memperbarui elemen dalam kamus dc. Namun, 
fungsi ini tidak memiliki pernyataan return, sehingga secara default, ia mengembalikan None.

Terakhir, Anda mencetak hasil dari pemanggilan fungsi fun(dc, '1', 'v'). Karena fungsi fun tidak secara 
eksplisit mengembalikan nilai apa pun, hasil cetakan adalah None.
'''

# 25. How many empty lines wil the following snippet send to the console?
l = [[c for c in range(r)]for r in range(3)]
# for x in l:
#     if len(x) < 2:
#         print()
# answer: 2

'''
breakdown
Anda membuat sebuah list yang disebut l menggunakan list comprehension. List comprehension ini memiliki dua tahap iterasi:

Iterasi pertama (for r in range(3)) menghasilkan nilai r dari 0 hingga 2 (karena range(3) menghasilkan 0, 1, dan 2).
Iterasi kedua (for c in range(r)) menghasilkan nilai c dari 0 hingga r - 1. Ini berarti jumlah elemen dalam 
setiap sublist yang dibuat oleh list comprehension akan bervariasi tergantung pada nilai r.
List comprehension menciptakan sublist untuk setiap nilai r. Sublist tersebut berisi angka-angka dari 0 hingga r - 1.

Kemudian, kode melanjutkan dengan iterasi melalui setiap sublist dalam list l dengan perulangan for x in l. 
Di dalam perulangan, Anda memeriksa panjang (jumlah elemen) dari setiap sublist dengan len(x).

Sebagai hasilnya, setelah eksekusi list comprehension, l akan menjadi sebagai berikut:
l = [[], [0], [0, 1]]

Kemudian, Anda menggunakan pernyataan if untuk memeriksa apakah panjang sublist tersebut kurang dari 2 (len(x) < 2). 
Jika panjangnya kurang dari 2, maka Anda mencetak baris kosong (print()).
'''


# 26. Knowing that the function named m{} resides in the module named f, and the code contains
# the following import statement, choose the right way to invoke the function:
# from m import f
# answer: the import statement is invalid


# 27. The packagee directory/folder may contain a file intended to initialize
# the package. It's name is:
# answer: __init__.py


# 28. The folder created by Python used to store pyc files is named:
# answer: __pycache__


# 29. What will be the output of the following code, located in the file module.py?
# print(__name__)
# answer: __main__


# 30. If you want to tell your module's users that a particular variable should not
# be accessed directly, you may:
# answer: start its name with _or__


# 31. If there is a finally: branch inside the try: block, we can say that:
# answer: it will always be executed

'''
breakdown

example:

try:
    pass
    try:
        pass
    finally:
        print("Teks")
except:
    pass
finally:
    print("Teks 2")

'''

# 32. What will be the output of the following snippet?
# try:
#     raise Exception
# except BaseException:
#     print("a",end='')
# else:
#     print("b",end='')
# finally:
#     print("c")
# answer: ac


# 33. What will be the output of the following snippet?
# class A:
#     def __init__(self, name):
#         self.name = name

#     # def __str__(self)-> str:
#     #     return f"{self.name}"
# a = A("class")
# print(a) # <__main__.A object at 0x000001635D87FA00>
# answer: a string ending with a long hexadecimal number


# 34. What will be the output of the following snippet?
# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")
# answer: It will an cause error


# 35. What will be the ouput of the following snipet?
class X:
    pass


class Y(X):
    pass


class Z(Y):
    pass


x = X()
z = Z()
# print(isinstance(x,Z),isinstance(z,X))
# answer False True

'''
breakdown
Anda mendefinisikan tiga kelas: X, Y, dan Z. Kelas Y adalah turunan dari kelas X, dan kelas Z adalah turunan dari kelas Y. 
Ini berarti Y mewarisi semua sifat dan metode dari X, dan Z mewarisi semua sifat dan metode dari Y.

Anda membuat dua objek: x dari kelas X dan z dari kelas Z. Ini berarti x adalah objek dari kelas X, 
dan z adalah objek dari kelas Z.

Anda menggunakan fungsi isinstance() untuk memeriksa apakah objek x adalah instance dari kelas Z dan 
apakah objek z adalah instance dari kelas X. Fungsi isinstance(objek, kelas) mengembalikan True jika objek
adalah instance dari kelas yang ditentukan atau turunannya, dan False jika tidak.

Hasil cetak dari kode ini adalah False True. Mari kita bahas hasil ini:

isinstance(x, Z) mengembalikan False karena objek x adalah instance dari kelas X, bukan Z 
atau turunannya.

isinstance(z, X) mengembalikan True karena objek z adalah instance dari kelas Z, dan Z adalah turunan dari Y, 
yang pada gilirannya adalah turunan dari X. Sebagai hasilnya, objek z juga bisa dianggap sebagai instance dari kelas X.
'''

# 36. The following code prints:
# x = "\"
# print(len(x))
# answer: the code will cause an error


# 37. The followinf code prints:
x = """
"""
# print(len(x))
# answer: 1

'''
breakdown

newline juga merupakan karekter sehingga tiap newline dihitung satu karakter
'''

# 38. If the class constructor is declared as below,
# which one of the assignments is valid?


# class Class:
#     def __init__(self):
#         pass


# Class()
# Class(None)  # error
# Class(1)  #
# Answer: Class()


# 39. What will be the output of the following code?
# class A:
#     A = 1

#     def __init__(self, v=2):
#         self.v = v + A.A
#         A.A += 1

#     def set(self, v):
#         self.v += v
#         A.A += 1
#         return


# a = A()
# a.set(2)
# print(a.v)
# answer: 5

'''
breakdown

Anda mendefinisikan kelas A. Dalam kelas ini, Anda memiliki dua atribut: A (atribut kelas) dan v (atribut objek). 
Atribut kelas A diinisialisasi dengan nilai 1.

Dalam metode kelas A yang disebut __init__, Anda mendefinisikan inisialisasi objek. Metode ini menerima parameter v 
(defaultnya adalah 2). Saat objek dibuat, nilai atribut objek v dihitung dengan menambahkan nilai v yang diteruskan 
sebagai argumen dengan nilai dari atribut kelas A. Selain itu, nilai atribut kelas A ditingkatkan sebesar 1 setiap 
kali objek baru dari kelas A dibuat.

Anda juga memiliki metode set yang menerima parameter v. Metode ini digunakan untuk menambahkan nilai v yang 
diteruskan sebagai argumen ke dalam atribut objek v, kemudian meningkatkan nilai atribut kelas A sebesar 1.

Anda membuat objek a dari kelas A tanpa menyebutkan nilai v. Ini berarti nilai v objek a akan diinisialisasi 
dengan 2 (default) ditambah dengan nilai dari atribut kelas A, yang pada awalnya adalah 1. Jadi, a.v akan menjadi 3, 
dan nilai A.A akan ditingkatkan menjadi 2.

Anda memanggil metode set(2) pada objek a. Ini akan menambahkan 2 ke dalam atribut objek v, 
sehingga nilai a.v menjadi 5. Selain itu, nilai atribut kelas A akan ditingkatkan menjadi 3.

Terakhir, Anda mencetak nilai a.v, yang adalah 5, sehingga output yang dihasilkan adalah 5.
'''


# 40. What will be the output of the following code?
class A:
    A = 1

    def __init__(self):
        self.a = 0


print(hasattr(A, 'A'))
# answer: True


'''
breakdown

Anda mendefinisikan kelas A. Di dalam kelas ini, Anda memiliki dua atribut:

A adalah atribut kelas yang memiliki nilai 1.
self.a adalah atribut objek yang akan diinisialisasi menjadi 0 saat objek dari kelas A dibuat. Namun, 
dalam kode yang Anda berikan, Anda tidak membuat objek, sehingga self.a tidak akan diinisialisasi.
Anda menggunakan fungsi hasattr(A, 'A') untuk memeriksa apakah kelas A memiliki atribut dengan nama 'A'. 
Fungsi hasattr(objek, atribut) digunakan untuk memeriksa apakah objek (dalam hal ini kelas A) memiliki 
atribut dengan nama tertentu ('A' dalam hal ini).

Hasil dari kode ini adalah True. Hal ini karena kelas A memiliki atribut kelas A yang telah Anda definisikan. 
Fungsi hasattr(A, 'A') mengembalikan True karena atribut 'A' ada dalam kelas A.

other text:
class A: - Ini adalah definisi kelas A. Kelas ini memiliki atribut kelas bernama A (dalam hal ini, namanya sama dengan nama 
kelas itu sendiri) dan memiliki konstruktor __init__ yang menginisialisasi atribut instance a dengan nilai 0.
A = 1 - Ini adalah atribut kelas dengan nama A yang memiliki nilai 1. Perlu dicatat bahwa atribut kelas dengan nama 
yang sama dengan nama kelas sendiri adalah hal yang sah dalam Python.
def __init__(self): - Ini adalah definisi konstruktor kelas. Konstruktor ini akan dijalankan ketika Anda membuat 
objek dari kelas A.
self.a = 0 - Ini adalah pernyataan dalam konstruktor yang menginisialisasi atribut instance a dengan nilai 0.
Selanjutnya, kode tersebut menggunakan fungsi hasattr() untuk memeriksa apakah kelas A memiliki atribut 
dengan nama 'A'. Fungsi hasattr() mengambil dua argumen: objek dan nama atribut yang ingin diperiksa.
Dalam kasus ini, kita memeriksa apakah kelas A memiliki atribut dengan nama 'A'. Hasilnya adalah True, 
karena kita telah mendefinisikan atribut kelas 'A' dengan nilai 1 di dalam kelas A itu sendiri.
'''

# 41. What will be the result of executing the following code?
# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass
# print(issubclass(C,A) and issubclass(C,B))
# answer: True


'''
breakdown
Anda mendefinisikan tiga kelas:

A: Kelas pertama A tidak memiliki isi (pass).
B: Kelas kedua B juga tidak memiliki isi (pass).
C: Kelas ketiga C didefinisikan sebagai turunan dari A dan B dengan menulis class C(A, B). 
Ini menunjukkan bahwa C mewarisi sifat dan metode dari kedua kelas A dan B.
Kemudian, Anda menggunakan fungsi issubclass(C, A) dan issubclass(C, B) untuk memeriksa 
apakah kelas C adalah subkelas dari A dan B masing-masing.

Hasil dari kedua pemanggilan issubclass di atas adalah True. Ini karena kelas C memang 
mewarisi sifat dan metode dari kelas A dan B, sehingga dapat dianggap sebagai subkelas dari keduanya.

issubclass():

issubclass(class, superclass) adalah fungsi yang digunakan untuk memeriksa apakah sebuah kelas adalah subkelas dari 
kelas tertentu (superclass).
Fungsi ini mengembalikan True jika kelas pertama (parameter pertama) adalah subkelas dari kelas kedua (parameter kedua), 
dan False jika tidak.
Contoh penggunaan: issubclass(ChildClass, ParentClass).

isinstance():
isinstance(obj, class) adalah fungsi yang digunakan untuk memeriksa apakah sebuah objek adalah instance (contoh/salinan) 
dari suatu kelas tertentu.
Fungsi ini mengembalikan True jika objek (parameter pertama) adalah instance dari kelas tertentu (parameter kedua), 
dan False jika tidak.
Contoh penggunaan: isinstance(obj, MyClass).
Perbedaan utama antara keduanya adalah bahwa issubclass() memeriksa hubungan antara kelas (kelas anak dan kelas induk), 
sedangkan isinstance() memeriksa hubungan antara objek dan kelas. Dengan kata lain:

issubclass() digunakan untuk memeriksa apakah sebuah kelas adalah subkelas dari kelas lain.
isinstance() digunakan untuk memeriksa apakah sebuah objek adalah instance dari suatu kelas.

'''


# 42. The sys.stdout stream is normally associated with
# answer: the screen


# 43. What will be the effect of running the following code?
# class A:
#     def __init__(self, v):
#         self._a = v + 1


# a = A(0)
# print(a._a)
# answer: 1

'''

class A: - Ini adalah definisi kelas A.
def __init__(self, v): - Ini adalah konstruktor kelas A. Konstruktor ini menerima satu parameter v ketika objek dari kelas A dibuat.
self._a = v + 1 - Dalam konstruktor, kita menginisialisasi atribut instance _a dengan nilai v + 1. Perlu diperhatikan 
bahwa atribut ini memiliki awalan garis bawah _, yang menunjukkan bahwa ini adalah konvensi untuk atribut "terlindungi" 
dalam Python. Atribut terlindungi ini dapat diakses dari luar kelas, tetapi biasanya dianggap sebagai bagian dari implementasi 
internal kelas dan tidak seharusnya diakses secara langsung.
Selanjutnya, kita membuat sebuah objek a dari kelas A dengan menggunakan konstruktor A(0). Saat membuat objek ini, 0 
akan menjadi nilai v yang dikirimkan ke konstruktor. Oleh karena itu, saat objek a dibuat, atribut _a akan diinisialisasi 
dengan 0 + 1, yaitu 1.
Kemudian, kita mencoba mencetak nilai atribut _a dari objek a dengan pernyataan print(a._a). Meskipun atribut ini memiliki 
awalan garis bawah, Python masih memungkinkan kita untuk mengaksesnya. Output dari kode tersebut adalah 1, sesuai dengan 
hasil yang ditampilkan dalam komentar.

'''

# 44. What will be the result of executing the following code?


# class A:
#     def __init__(self):
#         pass

#     def f(self):
#         return 1

#     def g():
#         return self.f()


# a = A()
# print(a.g())
# answer: it will raise an exception
'''

class A: - Ini adalah definisi kelas A. Kelas ini memiliki tiga metode: __init__, f, dan g.
def __init__(self): - Ini adalah konstruktor kelas A. Namun, dalam implementasinya, konstruktor ini tidak melakukan apa-apa 
selain pernyataan pass. Itu berarti objek dari kelas A akan dibuat tanpa inisialisasi yang nyata.
def f(self): - Ini adalah metode f dalam kelas A yang mengembalikan nilai 1. Metode ini memiliki parameter self, yang 
adalah konvensi dalam Python untuk merujuk pada objek instance yang sedang dioperasikan.
def g(): - Ini adalah metode g dalam kelas A. Namun, perhatikan bahwa metode g ini tidak memiliki parameter self, yang 
seharusnya ada dalam setiap metode kelas yang merujuk pada objek instance. Karena itu, metode g ini akan mengalami masalah.
Selanjutnya, kita membuat sebuah objek a dari kelas A dengan a = A(). Objek ini dibuat tanpa kesalahan.
Namun, ketika kita mencoba memanggil metode g melalui objek a dengan a.g(), akan terjadi kesalahan. Hal ini terjadi 
karena metode g tidak memiliki parameter self, sehingga ia tidak dapat merujuk pada objek instance a atau mengakses metode 
lain dalam kelas. Oleh karena itu, pemanggilan a.g() akan menghasilkan kesalahan yang disebut "TypeError" dengan pesan bahwa 
metode g membutuhkan 0 argument, tetapi 1 diberikan.

'''


# 45. What will be the result of executing the following code?
# class A:
#     def a(self):
#         print("a")


# class B:
#     def a(self):
#         print("b")


# class C(A, B):
#     def c(self):
#         self.a()


# a = C()  # type: ignore
# a.c()  # a
# answer: it will print a


# 46. The Exception class contains a property named args, and it iis a:
# answer: tuple


# 47. What will be the result of executing the following code?
def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s


for x in I(3):
    print(x, end='')
# answer: it will print ******

'''
breakdown
Anda mendefinisikan sebuah fungsi bernama I(n) yang menerima satu parameter, n. Fungsi ini akan digunakan sebagai generator.

Di dalam fungsi I(n), Anda mendeklarasikan variabel string kosong s.

Anda menggunakan loop for yang akan berjalan sebanyak n iterasi, di mana n adalah parameter yang diterima oleh fungsi.

Pada setiap iterasi, Anda menambahkan satu karakter * ke variabel string s menggunakan operator +=. 
Ini berarti pada setiap iterasi, satu bintang akan ditambahkan ke akhir string s.

Kemudian, Anda menggunakan pernyataan yield s untuk menghasilkan (yield) nilai dari string s pada setiap 
iterasi. Fungsi ini akan menghentikan eksekusi dan mengembalikan nilai s kepada pemanggil, tetapi tetap 
menjaga keadaan (state) dari fungsi, sehingga Anda dapat melanjutkan eksekusinya di iterasi berikutnya.

Di luar fungsi I(n), Anda menggunakan loop for untuk mengiterasi melalui generator yang dihasilkan oleh I(3).

Setiap nilai yang dihasilkan oleh generator (yaitu, string s dengan jumlah bintang yang bertambah pada 
setiap iterasi) dicetak menggunakan pernyataan print(x, end=''), di mana x adalah nilai yang dihasilkan oleh generator.

Hasil dari kode ini adalah ******. Hal ini terjadi karena generator I(3) akan menghasilkan nilai *, **, dan *** pada 
setiap iterasi, dan nilai-nilai tersebut akan dicetak secara berurutan karena pernyataan print menggunakan end='' untuk 
tidak menambahkan baris baru setelah setiap nilai dicetak.
'''


# 48. What will be the result of executing the following code?
def a(x):
    def b():
        return x + x
    return b


x = a('x')
y = a('')
print(x()+y())
# answer: it will print xx


'''
breakdown

Fungsi a(x) didefinisikan dengan satu parameter, x. Fungsi ini memiliki fungsi dalamnya sendiri, 
yaitu b(), yang tidak memiliki parameter.

Fungsi dalam, yaitu b(), mengembalikan hasil penjumlahan dari variabel x dengan dirinya sendiri, yaitu x + x.

Fungsi a(x) mengembalikan fungsi dalam b().

Kemudian, kita memanggil fungsi a('x') dan menyimpan hasilnya di dalam variabel x. Ini berarti x 
sekarang adalah referensi ke fungsi dalam a('x').

Selanjutnya, kita memanggil fungsi a('') dan menyimpan hasilnya di dalam variabel y. Ini berarti y 
sekarang adalah referensi ke fungsi dalam a('').

Pada baris terakhir, kita memanggil x() dan y() dan menjumlahkan hasilnya.

Ketika kita memanggil x(), itu sebenarnya akan menjalankan fungsi dalam a('x'), yang mengembalikan 
hasil x + x, di mana x adalah string 'x'. Jadi, hasil pertama adalah 'xx'.

Kemudian, ketika kita memanggil y(), itu akan menjalankan fungsi dalam a(''), yang juga mengembalikan 
hasil x + x, di mana x adalah string kosong (''). Jadi, hasil kedua adalah ''.

Kemudian, kita menggabungkan hasilnya dengan x() + y(), yang akan menghasilkan 'xx' + '', yang masih 
sama dengan 'xx'.

Jadi, hasil akhir dari x() + y() adalah 'xx'. Itulah mengapa jawabannya adalah 'xx'.
'''


# 49. If s is a stream opened in read mode, the following line will assign q as a:
# q = s.readlines()
# answer: list

'''

s adalah stream (misalnya, file) yang sudah dibuka dalam mode baca (read mode).

readlines() adalah metode yang dapat digunakan pada objek stream (file) untuk membaca semua baris dari stream 
tersebut dan mengembalikannya sebagai daftar (list) dalam Python.

Dengan demikian, baris kode di atas akan membaca semua baris dari stream s dan menyimpannya dalam variabel q sebagai
daftar. Setiap elemen dalam daftar q akan menjadi satu baris dari stream tersebut. Oleh karena itu, q akan menjadi daftar 
yang berisi semua baris dari stream s, dan setiap elemennya akan berisi satu baris dari stream.

'''


# 50. If you want to write a byte array's content to a stream, you'd use:
# answer: thw write() method


'''

Dalam Python, jika Anda ingin menulis konten dari sebuah byte array (atau objek bytes) ke dalam sebuah stream, 
Anda dapat menggunakan metode write(). Metode write() digunakan untuk menulis data ke dalam objek stream, seperti 
file atau objek socket

'''
