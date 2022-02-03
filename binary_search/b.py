def search(arr, search_element):
    left=0
    length = len(arr)
    position = -1
    right = length -1 

    # run loop from 0 to right
    for left in range(0, right,1):

        # if search element is found with left variable
        if (arr[left]==search_element):
            position = left
            print("Element found in array at", position +1 , "position with ", left+1, "Attempt")
            break

        # if search element is found with right variable
        if (arr[right] ==search_element):
            position = right
            print("Element found in array at", position+1,"position with", length - right, "Attempt")
            break
        left+=1
        right-=1

    if(position == -1):
        print()