
# # Generator-Function
# from ast import keyword
# from pyrfc3339 import generate


# # normal function,but whenever it needs to generate a value, it does so with the yield keyword rather than return
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3

# # to check above generator function
# for value in simpleGeneratorFun():
#     print(value)


# # ***********************************
# # Generator-object:

# # generator functions return a generator object.generator objects are used either by calling the  __next__() method on the generator object or using the generator object in a "for in" loop

# def simleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3

# # x is a generator object
# x=simleGeneratorFun()
# # iterating over the generator object using  __next__()
# print(x)
# print(x. __next__())
# print(x. __next__())
# print(x. __next__())

# # ****************************

# A simple generator for fibbonacci number

def fib(limit):
    # Initiallize first two fibonacci numbers
    a,b=0,1

    # one by one yield next fibonacci numbers
    while a<limit:
        yield a
        a,b=b, a+b

# create a generator object
x=fib(5)

# 
# iterating over the generator object using next 
print(x. __next__())
print(x. __next__())
print(x. __next__())
print(x. __next__())
print(x. __next__())
# iterating over the generator object using for in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)



