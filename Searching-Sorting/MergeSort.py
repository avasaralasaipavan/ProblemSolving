#merge sort algorithm

def Merge(left,right):
    

    i=j=0
    m,n = len(left),len(right)
    sorted_array = []

    while i<m and j<n:

        if left[i]< right[j]:
            sorted_array.append(left[i])
            i+=1

        else:
            sorted_array.append(right[j])
            j+=1
        
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


def MergeSort(arr):
    
    if len(arr)<=1:
        return arr 
    
    mid = len(arr)//2

    left =  arr[:mid]
    right = arr[mid:]

    left = MergeSort(left)
    right = MergeSort(right)

    return Merge(left,right)  


print(MergeSort([5,4,3,2,1]))
