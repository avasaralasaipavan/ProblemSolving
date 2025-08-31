def rev(arr,i,j):

    if i>=j:
        return arr 
    
    arr[i],arr[j] =  arr[j],arr[i]
    return rev(arr,i+1,j-1)

arr = ["h","e","l","l","o"]
i=0
j= len(arr)-1

print(rev(arr,i,j))