

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


# Customized dictionary

from collections import UserDict

# create a dictionary where deletion is not allowed
class MyDict(UserDict):
    # function to stop deletion from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    # function to stop pop from dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")
        