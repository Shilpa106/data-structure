# # def fun():
# #     print("welcome")

# # # Driver code to call a func
# # fun()

# # check x is even or odd

# import code


# def evenOdd(x):
#     if(x%2==0):
#         print('even')
#     else:
#         print("odd")

# # Driver code
# evenOdd(7)
# evenOdd(6)


# # Default argument
# def myFun(x, y=50):
#     print("x: ",x)
#     print("y: ",y)

# myFun(10)

# # keyword argument

# def student(firstname, lastname):
#     print(firstname, lastname)

# # keyword arg
# student(firstname='Geeks',lastname='practice')
# student(lastname='pracd',firstname='dfdsf')

# variable length argument
# In python, we can pass a variable number of arguments to a function using special symbols. there are 2 special symbols.

# *args(Non-Keyword Argument)
# **kwargs(Keyword Argument)

# # *args() 
# def myFun(*argv):
#     for arg in argv:
#         print(arg)

# myFun('Hello','Welcome','to','GeeksforGeeks')

# # M2
# a=['hello','welcome','to']
# def myFun(a):
#     for arg in a:
#         print(arg)
# myFun(a)


# # **kwargs
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("kwargs is",kwargs)
#         print("kwargs items",kwargs.items())

#         print("%s == %s" % (key, value))

# myFun(first='Geeks', mid='for', last='Geeks')


# *****************
#    #M3 # 

# # using *args and **kwargs
# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:",arg3)

# # use "*args or **kwargs to pass arguments 
# args=("Geeks","for","Geeks")
# myFun(*args)

# kwargs={"arg1":"Geeks", "arg2":"for","arg3":"geeks"}
# myFun(**kwargs)

# ******************8

# # using *args and **kwargs in same line to call a function
# def myFun(*args, **kwargs):
#     print("args:",args)
#     print("kwargs:",kwargs)

# myFun('geeks','for','geeks', first="Geeks", mid="for",last="Geeks")


# *****************************************
# # Docstring
# # check x is even or odd
# def evenOdd(x):
#     """Function to check if the number is even or odd"""
#     if (x%2 == 0):
#         print("even")
#     else:
#         print("odd")

# # Driver code to call the function
# print(evenOdd.__doc__)


# # return statement
# def square_value(num):
#     """This function returns the square value of the entered number"""
#     return num**2
# print(square_value(2))
# print(square_value(-4))



# # M1
# # in python every variable name is a reference.when we pass a variable to a function, a new reference to the object is created.parameter passing in python is the same as reference passing in java
# # here x is a new reference to same list 
# def myFun(x):
#     x[0]=20

# # lst is modified after function call.
# lst=[10,11,12,13,14,15]
# myFun(lst)
# print(lst)

# # M2
# When we pass a reference and change the received reference to something else, the connection between the passed and received parameter is broken.
# def myFun(x):
#     # After below line link of x with previous objects gets broken. A new object is assigned to x
#     x=[20,30,40]

# # lst is not modified after function call
# lst=[10,11,12,13,14,15]
# myFun(lst)
# print(lst)

# # M3
# # reference link is broken  if we assign a new value (inside the function)
# def myFun(x):
#     # after below line link of x with previous object gets broken.A new object is assigned to x
#     x=20

# # list is not modified after function call
# x=10
# myFun(x)
# print(x)


# # Swapping
# def swap(x,y):
#     temp = x
#     x=y
#     y=temp

# # Driver code
# x=2
# y=3

# swap(x,y)
# print(x)
# print(y)


# # Anonymous functions: a function is without a name.lambda keyword is used to create anonymous functions.
# # cube of a number using lambda function
# def cube(x):return x*x*x
# cube_v2=lambda x:x*x*x
# print(cube(7))
# print(cube_v2(7))

# # nested function
# def f1():
#     s='I love GeeksforGeeks'

#     def f2():
#         print(s)
#     f2()
# f1()


# Working of yield
# # A generator function that yields 1 for the first time,2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3

# # driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)

# *****************************
# # generate square from 1 to 100 using yield and generator


# def nextSquare():
#     i=1
#     # An infinite loop to generate squares
#     while True:
#         yield i*i
#         i+=1 #next execution resumes from this point
#     # function
# for num in nextSquare():
#     if num>100:
#         break
#     print(num)

# # ***************************************