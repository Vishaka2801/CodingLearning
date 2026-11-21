f = open ( "demo.txt" , "r" )



line1 = f.readline()
print (line1)

line2 = f.readline()
print (line2)




f.write("\nAnd with that innovator founder visa too")

f.close()

f = open ( "demo.txt" , "r+" )
f.write("abc")
print(f.read())


#with syntax 



