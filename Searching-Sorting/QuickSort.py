
def QuickSort(arr):
    

    if len(arr)<=1:
        return arr 
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x<pivot]
    right = [x for x in arr[:-1] if x>=pivot]

    return QuickSort(left) + [pivot] + QuickSort(right)


print(QuickSort([5,4,3,21,2,1]))
