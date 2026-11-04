'''
Day 5 and Day 6 session work


Strings

'''

#Escape Characters : - Octal value
txt = "\111\146\155\155\157"
print(txt)

#Escape Characters : - hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#Strings Methods 

#1) Capitalize

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#2) Casefold

txt = "Hello, And Welcome To My World!"

y = txt.casefold()

print(y)

#3) count

txt = "I love apples, apple are my favorite fruit"

z = txt.count("apple")

print(z)

#4) endswith

txt = "Hello, welcome to my world."

a = txt.endswith(".")

print(a)

#5) find

txt = "Hello, welcome to my world."

b = txt.find("welcome")

print(b)

#6) format

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#7) index

txt = "Hello, welcome to my world."

c = txt.index("welcome")

print(c)

#8) isalnum()	Returns True if all characters in the string are alphanumeric

txt = "Company12"

d = txt.isalnum()

print(d)

#9) isalpha()	Returns True if all characters in the string are in the alphabet

txt = "CompanyX"

d = txt.isalpha()

print(d)
#10) isascii()	Returns True if all characters in the string are ascii characters

txt = "Company123"

e = txt.isascii()

print(e)
#11) isdecimal()	Returns True if all characters in the string are decimals

txt = "1234"

x = txt.isdecimal()

print(x)
#12) isdigit()	Returns True if all characters in the string are digits

txt = "50800"
e = txt.isdigit()

print(e)
#13) isidentifier()	Returns True if the string is an identifier

txt = "Demo2e"

f = txt.isidentifier()

print(f)

#14) islower()	Returns True if all characters in the string are lower case

txt = "hello world!"

g = txt.islower()

print(g)
#15) isnumeric()	Returns True if all characters in the string are numeric

txt = "565543"

h = txt.isnumeric()

print(h)
#16) isspace()	Returns True if all characters in the string are whitespaces

txt = "   "

i = txt.isspace()

print(i)

#17) istitle()	Returns True if the string follows the rules of a title

txt = "Hello, And Welcome to My World!"

j = txt.istitle()

print(j)

#18) isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"

k = txt.isupper()

print(k)
#19) join()	Joins the elements of an iterable to the end of the string

myTuple = ("John", "Peter", "Vicky")

k = "#".join(myTuple)

print(k)
#20) lower()	Converts a string into lower case

txt = "Hello my FRIENDS"

m = txt.lower()

print(m)

#21) lstrip()	Returns a left trim version of the string

txt = "     banana     "

n = txt.lstrip()

print("of all fruits", n, "is my favorite")

#22) partition()	Returns a tuple where the string is parted into three parts

txt = "I could eat bananas all day"

o = txt.partition("bananas")

print(o)
#23) replace()	Returns a string where a specified value is replaced with a specified value

txt = "I like bananas"

p = txt.replace("bananas", "apples")

print(p)
#24) rfind()	Searches the string for a specified value and returns the last position of where it was found

txt = "Mi casa, su casa."

q = txt.rfind("casa")

print(q)
#25) rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."

r = txt.rindex("casa")

print(r)

#26) rpartition()	Returns a tuple where the string is parted into three parts

txt = "I could eat bananas all day, bananas are my favorite fruit"

s = txt.rpartition("bananas")

print(s)
#27) rsplit()	Splits the string at the specified separator, and returns a list

txt = "apple, banana, cherry"

t = txt.rsplit(", ")

print(t)
#28) rstrip()	Returns a right trim version of the string

txt = "     banana     "

u = txt.rstrip()

print("of all fruits", u, "is my favorite")
#29) split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"

v = txt.split()

print(v)
#30) splitlines()	Splits the string at line breaks and returns a list

txt = "Thank you for the music\nWelcome to the jungle"

w = txt.splitlines()

print(w)

#31) startswith()	Returns true if the string starts with the specified value

txt = "Hello, welcome to my world."

abc = txt.startswith("Hello")

print(abc)
#32) strip()	Returns a trimmed version of the string

txt = "     banana     "

adx = txt.strip()

print("of all fruits", adx, "is my favorite")
#33) swapcase()	Swaps cases, lower case becomes upper case and vice versa

txt = "Hello My Name Is PETER"

uvw = txt.swapcase()

print(uvw)
#34) upper()	Converts a string into upper case

txt = "Hello my friends"

ijk = txt.upper()

print(ijk)
#35) zfill()	Fills the string with a specified number of 0 values at the beginning

txt = "50"

mno = txt.zfill(10)

print(mno)




'''
Practice work

1) Find out all the octal values and hex values for A-Z and 0-9 and paste it here!
2) Code challenge for Strings

'''

# 1. Create the variable

# 2. Print characters from index 2 to 5

# 3. Print in upper case

# 4. Create the name variable

# 5. Print using an f-string

txt = "Vishaka"
print (txt[2:5])
print (txt.upper())

name = "Python"
print(f"I love {name}")

print("A  101  41")
print("B  102  42")
print("C  103  43")
print("D  104  44")
print("E  105  45")
print("F  106  46")
print("G  107  47")
print("H  110  48")
print("I  111  49")
print("J  112  4A")
print("K  113  4B")
print("L  114  4C")
print("M  115  4D")
print("N  116  4E")
print("O  117  4F")
print("P  120  50")
print("Q  121  51")
print("R  122  52")
print("S  123  53")
print("T  124  54")
print("U  125  55")
print("V  126  56")
print("W  127  57")
print("X  130  58")
print("Y  131  59")
print("Z  132  5A")






