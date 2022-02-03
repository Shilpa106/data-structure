# Input: arr[] = {0, -1, 2, -3, 1}
#         sum = -2
# Output: -3, 1
#          Valid pair exists.
         
# If we calculate the sum of the output,
# 1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}
#        sum = 0
# Output:
#         No valid pair exists.


# Function to find and print pair
# def chkPair(A,size,x):

#     for i in range(0,size-1):#(0,4)
#         print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",i)
#         for j in range(i+1,size):#(i+1,5)
#             print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",j)
#             if (A[i]+A[j] == x):
#                 print("Pair with a given sum",x," is (" , A[i] , ", ", A[j] , ")")
#                 return True
#                 # return 1

#     return False
#     # return 0

# # if __name__ == "__main__":

# A=[0, -1, 2,-3,1]
# x=-2
# size=len(A)

# if(chkPair(A,size,x)):
#     print("Valid pair exists")
# else:
#     print("no valid pair exists for ", x)

#M2 ********************************************************************

def hasArrayTwoCandidates(A, arr_size,sum):
    # sort the array
    quickSort(A,0,arr_size-1)
    l=0
    r=arr_size-1

    # traverse the array for the two elements
    while l<r:
        if(A[l]+A[r]==sum):
            return 1
        elif (A[l]+A[r]<sum):
            l+=1
        else:
            r-=1

    return 0

    # Implementation of Quick Sort
def quickSort(A,si,ei):
    if si<ei:
        pi=partition(A, si,ei)
        quickSort(A,si,pi-1)
        quickSort(A,pi+1,ei)

def partition(A, si, ei):
    x=A[ei]
    i=(si-1)
    for j in range(si, ei):
        if A[j]<=x:
            i+=1

            # this operation is used to swap two variables in python
            A[i], A[j]=A[j],A[i]

        A[i+1],A[ei]=A[ei],A[i+1]
    return i+1

# Driver program
A=[1,4,45,6,10,-8]
n=16
if(hasArrayTwoCandidates(A,len(A),n)):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")

