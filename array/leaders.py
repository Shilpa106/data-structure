from array import array




# # Python function to print leaders in array


# def printLeaders(arr,size):
#     for i in range(0,size):
#         for j in range(i+1,size):
#             if arr[i]<=arr[j]:
#                 break
#         if j==size-1:#if loop didn't break
#             print(arr[i])

# # Driver function
# arr=[16,17,4,3,5,2]
# printLeaders(arr,len(arr))


def printLeaders(arr, size):
    max_from_right=arr[size-1]
    print(max_from_right)
    for i in range(size-2,-1,-1):
        if max_from_right<arr[i]:
            print(arr[i])
            max_from_right = arr[i]

# Driver Function
arr=[16,17,4,3,5,2]
printLeaders(arr, len(arr))

