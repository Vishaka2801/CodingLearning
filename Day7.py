# x = (input("enter a number "))
# y = (input("enter another number "))
# if(x.isnumeric() & y.isnumeric()): #String Method
if((x := (input("enter a number ")).isnumeric()) & (y := (input("enter another number ")).isnumeric())):
    tmp1 = int(x) #Type
    tmp2 = int(y)

    if tmp1 > tmp2:
        print("high")
    elif tmp1 < tmp2:
        print("low")
    elif tmp1 == tmp2:
        print("equals")

else:
    print ("invalid task. Please enter a number" )


'''Boolean Code Challenge'''

# Print the result of 10 > 9
print(10 > 9)

# Print the result of 10 == 9
print(10 == 9 )
# Print the result of bool("Hello")
print (bool("Hello"))
# Print the result of bool(0)
print (bool(0))


'''Python Operators Code Challenge'''
'''Practice operators'''
x = 1222
y = 2

#1 2 3 4 5 6 7 8 9
#1 0 1 0 1 0 1 0 1

if(x%2 == 0):
	print("Number is EVEN")
else:
	print("Number is ODD")


x = 3
x= x+3



'''Assignment Operators
What are these???????

&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)

'''



