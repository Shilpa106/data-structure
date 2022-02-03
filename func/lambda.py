

# # string='GeeksforGeeks'

# # # lambda returns a function object

# # # print(lambda string : string)
# # # print(lambda x : print(x)(x))



# # difference bw def and lambda

# def cube(y):
#     return y*y*y

# g=lambda x:x*x*x
# print(g(7))
# print(cube(5))


# lambda function

# def power(n):
#     return lambda a:a**n

# base=power(2)
# print("Now power is set to 2")
# print("8 power of 2=",base(8))
# base=power(5)
# print("now power is set to 5")
# print("8 powerof 5=", base(8))


# # ****************
# a=[100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
# filtered = filter(lambda x:x%2 == 0 ,a)
# print(list(filtered))
# mapped = map(lambda x:x%2==0, a)
# print(list(mapped))

# # **********************8

