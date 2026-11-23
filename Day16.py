#with syntax

with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)


with open ("demo.txt" , "w") as f :
     f.write("new data")

    #  import os 
    #  os.remove ("file namei ")


    # qs1 
# create a file and write the text 

with open ("practice.txt" , "w") as f :
     f.write("Hi all\nwe r learning File I/O\n")
     f.write ("using Java. \nI like programming in Java.")


     #qs 2
     # WAF that will replace java wod python

     with open ("practice.txt" , "w") as f :
        data = f.read()

new_data = data.replace("Java" , "Python")
print (new_data)

with open ("practice.txt" , "w") as f :
        f.wrie(new_data)