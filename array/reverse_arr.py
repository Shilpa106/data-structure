# def reverseList(A,start,end):
#     while start<end:
#         A[start],A[end]=A[end],A[start]
#         start+=1
#         end-=1

# A=[1,2,3,4,5,6]
# print(A)
# reverseList(A,0,5)
# print("Reversed list is")
# print(A)


# recursive way
# def reverseList(A,start,end):
#     if start>=end:
#         return 
#     A[start],A[end]=A[end],A[start]

#     reverseList(A,start+1, end-1)

# A=[1,2,3,4,5,6]
# print(A)
# reverseList(A,0,5)
# print("Reversed list is")
# print(A)

# using python list slicing
def reverseList(A):
    print(A[::-1])

A=[1,2,3,4,5,6]
print(A)
print("Reversed list is")
reverseList(A)
