# implementing map 
#  return double of n


# def addition(n):
#     return n+n

# # we double all numbers using map()
# numbers=(1,2,3,4)
# result=map(addition, numbers)
# print(result)
# print(list(result))

# o/p:[2, 4, 6, 8]

# # double all numbers using map and lambda 

# numbers=(1,2,3,4)
# result=map(lambda x:x+x, numbers)
# print(list(result))

# # Add two lists using map and lambda

# numbers1=[1,2,3]
# numbers2=[4,5,6]

# result=map(lambda x, y:x+y, numbers1, numbers2)
# print(list(result))

# # list of strings
# l=['sat','bat','cat','mat']

# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)


# ChainMap

# from collections import ChainMap
# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5,'f':6}

# # Definig the chainmap
# c=ChainMap(d1,d2,d3)
# print(c)

# # access operations

# import collections

# # initializing dictionaries
# dict1={'a':1,'b':2}
# dict2={'b':3,'c':4}

# # initializing ChainMap
# chain=collections.ChainMap(dict1, dict2)

# print("all the chainMap contents are:")
# print(chain.maps)

# # printing keys using keys()
# print("all keys of ChainMap are : ")
# print(list(chain.keys()))

# # printing value using keys()
# print("All values of ChainMap are: ")
# print(list(chain.values()))


# manipulating operations
import collections

# initializing dictionaries
dic1={'a':1,'b':2}
dic2={'b':3,'c':4}
dic3={'f':5}

# initializing ChainMap
chain=collections.ChainMap(dic1, dic2)

# printing chainMap  using map
print("All the ChainMap contents are  :")
print(chain.maps)

# using new_child() to add new dictionary
chain1=chain.new_child(dic3)

# printing chainMap using map
print("Displaying new ChainMap : ")
print(chain1.maps)

# displaying value associated with b before reversing
print("value associated with b before reversing is: ", end="")
print(chain1['b'])

# reversing the ChainMap
chain1.maps=reversed(chain1.maps)
# displaying value associated with b after reversing
print("Value associated with b after reversing is :", end="")
print(chain1['b'])
