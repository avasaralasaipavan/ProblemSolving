def findPoint(arr):

    right_total =  sum(arr)

    left_count =  0
    n=len(arr)
    for i in range(n):

        rightCount = right_total - left_count - arr[i]

        if rightCount == left_count:
            return i
        
        else:
            left_count +=arr[i] 
        
    return -1


print(findPoint([1, 2, 0, 3]))
