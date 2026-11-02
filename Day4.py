'''
Day 4 Session Work.

Setting the Data Type
In Python, the data type is set when you assign a value to a variable:
Example	Data Type
x = "Hello World"	str
x = 20	int
x = 20.5	float
x = 1j	complex
x = ["apple", "banana", "cherry"]	list
x = ("apple", "banana", "cherry")	tuple
x = range(6)	range
x = {"name" : "John", "age" : 36}	dict
x = {"apple", "banana", "cherry"}	set
x = frozenset({"apple", "banana", "cherry"})	frozenset
x = True	bool
x = b"Hello"	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview
x = None	NoneType

'''
#List
x = [0,1,2,3,4,5]
print("List: ",x)

#Range
x = range(6)
print("Range: ", x)

print(list(x))