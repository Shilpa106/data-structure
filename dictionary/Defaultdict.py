# Dict={1:'Geeks',2:'For',3:'Geeks'}
# print('Dictionary:')
# print(Dict)
# print(Dict[1])


# defaultdict never raises a key error

# syntax:defaultdict(default_factory)

# M2

# from collections import defaultdict
# # function to return a default values for keys that is not present

# def def_value():
#     return "Not Present"

# # defining the dict
# # d=defaultdict()    #key error
# d=defaultdict(def_value)
# d["a"]=1
# d["b"]=2

# print(d["a"])
# print(d["b"])
# print(d["c"])


# M3

# # default_factory arg of defaultdict
# from collections import defaultdict
# # defining the dict and passing lambda as default_factory arg

# d=defaultdict(lambda:"Not Present")
# d["a"]=1
# d["b"]=2

# print(d["a"])
# print(d["b"])
# print(d["c"])

# M4
# from collections import defaultdict

# # Defining the dict
# d=defaultdict(lambda:"Not Present")
# d["a"]=1
# d["b"]=2
# # provides the default value for the key
# print(d.__missing__('a'))
# print(d.__missing__('d'))

# M5
# Using list as a default factory
# from collections import defaultdict
# # Definig a dict
# d=defaultdict(list)
# for i in range(5):
#     d[i].append(i)

# print("Dictionary with values as list")
# print(d)


# using int as a default_factory
# M6
from collections import defaultdict

# Defining the dict
d=defaultdict(int)
L=[1,2,3,4,2,4,1,2]
# iterate through the list for keeping count
for i in L:
    # the default value is 0 so there is no need to enter the key first 
    d[i]+=1

print(d)



