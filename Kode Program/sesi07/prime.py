# 4.3.1.9 LAB: Prime numbers - how to find them

def is_prime(num):

    n = num - 1
    while num % n != 0:
        n -= 1
        if n == 1:
            return num 
            



for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()