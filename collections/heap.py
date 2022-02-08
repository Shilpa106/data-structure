

# # import heapq
# # #
# # # initializing list
# # li=[5,7,9,1,3]

# # # using heapify to convert list into heap
# # heapq.heapify(li)

# # # printing created heap
# # print("the created heap is:", end="")
# # print(list(li))

# # # using heappush() to push elements into heap 
# # # pushes 4
# # heapq.heappush(li,4)

# # # printing modified heap
# # print("The modified heap after push is:", end="")

# # print(list(li))

# # # using heappop() to pop smallest element
# # print("The popped and smallest element is: ", end="")
# # print(heapq.heappop(li))

# # # # ****************************

# # # heappushpop(), heapreplace()

# # import heapq
# # # initializing list 1
# # li1=[5,7,9,4,3]

# # # initializing list2
# # li2=[5,7,9,4,3]

# # # using heapify() to convert list into heap
# # heapq.heapify(li1)
# # heapq.heapify(li2)

# # # using heappushpop() to push and pop items simultaneously pops 2
# # print("The popped item using heappushpop() is: ", end="")
# # print(heapq.heappushpop(li1, 2))

# # # using heapreplace() to push and pop items simultaneously pops 3
# # print("The popped item using heapreplace() is :", end="")
# # print(heapq.heapreplace(li2, 2))


# # # **********************


# # # working of nlargest(), nsmallest()
# # import heapq

# # # initializing list
# # li1=[6,7,9,4,3,5,8,10,1]

# # # using heapify() to convert list into heap
# # heapq.heapify(li1)
# # print("The 3 largest numbers in list are",end="")
# # print(heapq.nlargest(3,li1))


# # print(heapq.nsmallest(3,li1))

# # # ***************************

# #  UserDict

# from collections import UserDict

# d={'a':1,'b':2,'c':3}
# print("ddddddddddddddddddd",d)

# # creating an UserDict
# userD=UserDict(d)
# print(userD.data)


# # creating an empty UserDict
# userD=UserDict()
# print(userD.data)

# # *****************
# # Customized dictionary

# from collections import UserDict

# # create a dictionary where deletion is not allowed
# class MyDict(UserDict):
#     # function to stop deletion from dictionary
#     def __del__(self):
#         raise RuntimeError("Deletion not allowed")
#     # function to stop pop from dictionary
#     def pop(self, s=None):
#         raise RuntimeError("Deletion not allowed")
#     # 
#     # to stop popitem from dictionary
#     def popitem(self, s=None):
#         raise RuntimeError("Deletion not allowed")

# d=MyDict({'a':1,'b':2,'c':3})
# print("Original dictionary")
# print(d)
# d.pop(1)

# # *************************

# # UserList

# from collections import UserList
# L=[1,2,3,4]
# # creating a UserList
# userL=UserList(L)
# print(userL.data)

# # creating empty userlist
# userL = UserList()
# print(userL.data)


# # ***************

# from collections import UserList

# # 
# # creating a List where deletion is not allowed
# class MyList(UserList):
#     # function to stop deletion from list
#     def remove(self, s=None):
#         raise RuntimeError("Deletion not allowed")

#     # function to stop pop from list
#     def pop(self,s=None):
#         raise RuntimeError("Deletion not allowed")

# # Driver code
# L=MyList([1,2,3,4])
# print("original list")

# # inserting to list
# L.append(5)
# print("After insertion")
# print(L)

# # Deleting from list
# L.remove()


# # *******************************

# UserString
# # M1
# from collections import UserString
# d=12344

# # Creating an UserDict
# userS=UserString(d)
# print(userS.data)

# # creating an empty UserDict
# userS=UserString("")
# print(userS.data)

# # *****************************

# # M2
# from collections import UserString

# # creating a mutable string
# class Mystring(UserString):
#     # function to append to string
#     def append(self, s):
#         self.data+=s

#     # function to remove from string
#     def remove(self,s):
#         self.data= self.data.replace(s,"")

# # Driver's code
# s1=Mystring("Geeks")
# print("original string:", s1.data)

# # appending to string
# s1.append("s")
# print("string after appending:",s1.data)

# # Removing from string
# s1.remove("e")
# print("String after Removing", s1.data)

# # **********************************************
