x = ("apple", "banana", "cherry")
#print tuple x
#print type tuple x
y = list(x)
#print tuple y
#print type tuple y
y[1] = "kiwi"
#print tuple y
x = tuple(y)
#print type tuple x
print(x)