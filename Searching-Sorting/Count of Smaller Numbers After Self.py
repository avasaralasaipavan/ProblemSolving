''' 
315. Count of Smaller Numbers After Self
Hard
Topics
premium lock icon
Companies
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

'''


def Merge(left,right,dit):
    

    i=j=0
    m,n = len(left),len(right)
    sorted_array = []

    while i<m and j<n:

        if left[i]< right[j]:
            sorted_array.append(left[i])
            i+=1

        else:
            sorted_array.append(right[j])
            dit[left[i]]= dit[left[i]]+1
            j+=1
        
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    print(dit,left,right)
    return sorted_array


def MergeSort(arr,dit):
    
    if len(arr)<=1:
        return arr 
    
    mid = len(arr)//2

    left =  arr[:mid]
    right = arr[mid:]

    left = MergeSort(left,dit)
    right = MergeSort(right,dit)

    return Merge(left,right,dit)  


arr = [5,2,6,1]
dit = {}


for i in arr:
    dit[i] = 0

data = MergeSort(arr,dit)
print(data)