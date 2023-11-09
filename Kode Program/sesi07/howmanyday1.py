# 4.3.1.7 LAB: How many days: writing and using your own functions

def isYearLeap(year):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):


    if isYearLeap(year):
        if month == 2:
            return 29
        elif month in [4,6,9,11]:
            return 30
        else:
            return 31
    else:
        if month == 2:
            return 28
        elif month in [4,6,9,11]:
            return 30
        else:
            return 31

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
