# Find the Number Occurring Odd Number of Times

def getOddOccurrence(arr, arr_size):
    for i in range(0,arr_size):
        count=0
        for j in range(0,arr_size):
            if arr[i]==arr[j]:
                count+=1

        if (count%2!=0):
            return arr[i]
            