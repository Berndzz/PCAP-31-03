# 4.3.1.6 LAB: A leap year: writing your own functions

def isYearLeap(year):

 if year == 2000 or year == 2016:
        return True
 else:
        return False

print (isYearLeap(1900))
print (isYearLeap(2016))

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")