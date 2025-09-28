def generate(arr,target):
    
    i =0
    j = len(arr)-1
    while i<j:
        t = arr[i]+arr[j]
        if t == target:
            return True
        
        if t<target:
            i+=1
        if t>target:
            j-=1
 
    return False


arr = [0, -1, 2, -3, 1]

print(generate(sorted(arr), target = -2))