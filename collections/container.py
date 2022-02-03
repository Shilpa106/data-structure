

# from collections import Counter

# # with sequence of items
# print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# # with dictionary
# print(Counter({'A':3, 'B':5,'c':2}))

# # with keyword arguments
# print(Counter(A=3, B=5, C=2))


# **********************

# # update
# from collections import Counter
# coun=Counter()

# coun.update([1,2,3,1,2,1,1,2])
# print(coun)

# coun.update([1,2,4])
# print(coun)

# # ***************************


# from collections import Counter
# c1=Counter(A=4, B=3, C=10)
# c2=Counter(A=10,B=3,C=4)

# c1.subtract(c2)
# print(c1)

# # # ********************************

# from collections import Counter

# # create a list
# z=['blue','red','blue','yellow','blue','red']
# print(Counter(z))

# # # **************************



# from collections import OrderedDict
# print("this is a cid")
# d={}
# d['a']=1
# d['b']=2
# d['c']=3
# d['d']=4

# for key, value in d.items():
#     print(key, value)

# print("this is an ordered dict:\n")
# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['d']=4

# for key, value in od.items():
#     print("od",od)
#     print("od items",od.items())
#     print("ordered dict",key, value)

# # # ********************************
# key value change

# from collections import OrderedDict
# print("Before:\n")

# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['d']=4

# for key, value in od.items():
#     print(key, value)

# print("after ")
# od['c']=5
# for key, value in od.items():
#     print(key, value)

# # # ********************************8
# # Deletion and Re-Inserting:
# from ast import Or
# from collections import OrderedDict
# print("Before deleting")
# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['d']=4
# for key, value in od.items():
#     print(key, value)

# print("After deleting")
# od.pop('c')
# for key, value in od.items():
#     print(key, value)

# print("After re-inserting")
# od['c']=3
# for key, value in od.items():
#     print(key, value)


# # *****************************

