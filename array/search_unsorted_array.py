# Python program for searching,insert,delete in unsorted array
# # **********************************************


# def findElement(arr, n, key):
#     for i in range(n):
#         if (arr[i]==key):
#             print(arr[i])
#             print(key)

#             return i
#     return -1

# arr=[12,34,10,6,40]
# key=34
# n=len(arr)

# # search operation
# index=findElement(arr,n,key)
# print(index)
# if index!=-1:
#     print("element found at position:" +str(index+1))
# else:
#     print("hi")
#     print("element not found")

#2 # ***********************************************************


# def findElement(arr,n,key):
#     for i in range(n):
#         if arr[i]==key:
#             return i

#     return -1

# arr=[2,4,5,6,65]
# n=len(arr)
# key=6

# index=findElement(arr,n,key)
# if index!=-1:
#     print("Element found at position:" +str(index+1))
# else:
#     print('element not found')


# 3# ***********************************************************



# def findElement(arr,n,key):
#     for i in range(n):
#         if arr[i]==key:
#             return i
#     return -1

# arr=[3,5,2,1]
# n=len(arr)
# key=2

# index=findElement(arr,n,key)
# if index!=-1:
#     print("element found at positions:" +str(index+1))
# else:
#     print("element not found")

# ***************************************************************
# def findElement(arr,n,key):
#     for i in range(n):
#         if arr[i]==key:
#             return i
#     return -1

# arr=[2,8,5,29,9]
# n=len(arr)
# key=5

# index=findElement(arr,n,key)
# if index!=-1:
#     print("element found at position:" +str(index+1))
# else:
#     print("element not found")

# ******************************************************************
# def findElement(arr,n,key):
#     for i in range(n):
#         if arr[i]==key:
#             return i
#     return -1

# arr=[3,43,2,22]
# n=len(arr)
# key=2

# index=findElement(arr,n,key)
# if index!=-1:
#     print("element found at pos:" +str(index+1))
# else:
#     print("element not found")

# ***************************Insert at the end*********************

# def insert(arr,element):
#     arr.append(element)

# arr=[12,16,20,40,50,70]
# key=26

# print("before inserting")
# print(arr)

# print("after inserting")
# insert(arr,key)
# print(arr)

# ********************************88
# def insert(arr,element):
#     arr.append(element)

# arr=[6,44,33,22,23]
# key=3

# print("before insert")
# print(arr)

# print("after insert")
# insert(arr,key)
# print(arr)

# ***********************************

# Delete Operation
# arr=[4,5,6,7,87]
# key=5

# print("Array before deletion")
# print(arr)

# print("After deletion")
# arr.remove(key)
# print(arr)

# ***************************************

# arr=[4,3,33,22,454]
# key=454

# print("array before deletion")
# print(arr)

# print("array after deletion")
# arr.remove(key)
# print(arr)

# *********************************

# Time complexities: 
# Search: O(n) 
# Insert: O(1) 
# Delete: O(n)
# *******************************************

# Program for search , insert ,delete in sorted array
# binary search
# def binarySearch(arr,low,high,key):
#     mid=int((low+high)/2)

#     if(key==arr[mid]):
#         return mid
#     if(key>arr[mid]):
#         return binarySearch(arr,(mid+1),high,key)

#     if(key<arr[mid]):
#         return binarySearch(arr,low,(mid-1),key)
#     return 0

# arr=[3,4,5,6,16,7,77]
# n=len(arr)
# key=77
# print("Index:", int(binarySearch(arr, 0, n-1, key)))


# *************************************
# def binarySearch(arr,low,high,key):
#     mid=int((low+high)/2)
#     if arr[mid]==key:
#         return mid
#     if key>arr[mid]:
#         return binarySearch(arr,mid+1,high,key)
#     if key<arr[mid]:
#         return binarySearch(arr,0,mid-1,key)
#     return 0

# arr=[4,3,2,33,44,22,44]
# key=33
# n=len(arr)
# print("index:", binarySearch(arr,0,n-1,key))

# *******************************************

# Time Complexity of Search Operation: O(Log n)

# **********************************************************************

# insert in sorted array


# def insertSorted(arr,n,key,capacity):
#     # cant insert more elements if n is already more than or equal to capacity
#     if(n>=capacity):
#         return n
#     i=n-1
#     while i>=0 and arr[i]>key:
#         arr[i+1]=arr[i]
#         i-=1
    
#     arr[i+1]=key
#     return (n+1)
# arr=[12,16,20,40,50,70]

# for i in range(20):
#     arr.append(0)

# capacity=len(arr)
# n=6
# key=26

# print("Before Insertion:")
# for i in range(n):
#     print(arr[i])


# # Inserting key
# n=insertSorted(arr,n,key,capacity)

# print("After insertion:")
# for i in range(n):
#     print(arr[i])

# Deletion in sorted array
def deleteElement(arr,n,key):
    # Find pos of element to be deleted
    pos=binarySearch(arr,0,n-1,key)
    if (pos==-1):
        print("element not found")
        return n

    # Deleting element********************************
    for i in range(pos,n-1):
        arr[i]=arr[i+1]
    return n-1
    # ************************************************

# To search a ley to be deleted
def binarySearch(arr,low,high,key):
    if(high<low):
        return -1
    mid=(low+high)//2
    if key==arr[mid]:
        return mid
    if key>arr[mid]:
        return binarySearch(arr,mid+1,high,key)
    if key<arr[mid]:
        return binarySearch(arr,low,mid-1,key)

arr=[23,33,44,233,12,22]
n=len(arr)
key=33
print('Array before deletion')
for i in range(n):
    print(arr[i])

n=deleteElement(arr,n,key)
print("after deletion")
for i in range(n):
    print(arr[i])

# Time Complexity of Delete Operation: O(n) [In the worst case all elements may have to be moved]*****************************


