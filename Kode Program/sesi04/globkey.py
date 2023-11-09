# global variables
x = "awesome"

def myfunc():
	global x
	# global variables
	x = "fantastic"
	
print ("Python is " + x)
myfunc()
print ("Python is " + x)
