
# Python code to demonstrate
# call by value


string = "Geeks"


def test(string):
	del string[0]
	print("Inside Function:", string)
	
# Driver's code
test(string)
print("Outside Function:", string)
