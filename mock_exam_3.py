import math
import test3

# 1. Choose the correct output of the following code: -


class A:
    num = 0

    def __str__(self):
        A.num = A.num + 1
        return str(A.num)


class B(A):
    def __init__(self):
        super().__init__()


obj = A()
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
class List1(test3.List):
    def __init__(self):
        super().__init__()
        print("One: ", self._l)
        print("Two: ", test3.List._name)


List1()
# answer:
# One: [1,1.0,3,2.0,5,3.0,7,4.0,9,5.0]
# Two: List


# 12. Choose the correct output of the following code: -
