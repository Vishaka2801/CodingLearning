# #Suppose 3 variables a,b and task
# a = 69
# b = 65
# task = "plus"

# if task == "plus" :
#     print ("Addition: ",a + b)

# elif task == "minus" :
#     print ("Subtraction: ", a - b)

# elif task == "mul" :
#     print ("Multilpcayion: ", a * b)

# elif task == "divide" :
#     print ("Division: ",a / b ) 
                                                                                
# a = 69
# b = 65
# task = "minus"

# if task == "plus" :
#     print ("Addition: ",a + b)

# elif task == "minus" :
#     print ("Subtraction: ", a - b)

# elif task == "mul" :
#     print ("Multilpcayion: ", a * b)

# elif task == "divide" :
#     print ("Division: ",a / b ) 

# a = 69
# b = 65
# task = "mul"

# if task == "plus" :
#     print ("Addition: ",a + b)

# elif task == "minus" :
#     print ("Subtraction: ", a - b)

# elif task == "mul" :
#     print ("Multilpcayion: ", a * b)

# elif task == "divide" :
#     print ("Division: ",a / b ) 

# a = 69
# b = 65
# task = "divide"

# if task == "plus" :
#     print ("Addition: ",a + b)

# elif task == "minus" :
#     print ("Subtraction: ", a - b)

# elif task == "mul" :
#     print ("Multilpcayion: ", a * b)

# elif task == "divide" :
#     print ("Division: ",a / b )

# def calculator(a,b,task):

#     if task == "plus" :
#         print ("Addition: ",a + b)

#     elif task == "minus" :
#         print ("Subtraction: ", a - b)

#     elif task == "mul" :
#         print ("Multilpcayion: ", a * b)

#     elif task == "divide" :
#         print ("Division: ",a / b )

# calculator(2,3,"plus")
# calculator(2,3,"minus")
# calculator(2,3,"mul")
# calculator(2,3,"divide")



"""
Your task for Practice Session is to get the inputs (a, b, task) from user on terminal. 
If you are comfortable in functions then you can use above function.
Or else just use the normal code to get the desired output.
"""
a = float (input("Enter first number:"))
b = float (input("Enter second number :"))
task = input ("Enter task plus/minus/mul/divide :")

if task == "plus":
    print("Result:", a + b )

elif task == "minus": 
    print("Result:", a - b)

elif task == "mul":
    print ("Result:", a * b)

elif task == "divide":
    if b != 0:
        print ("Result:", a/b)

    else :
        print ("Cannot divide by 0")

else:
    print ("invalid task. Please enter plus, minus, mul, divide" )







