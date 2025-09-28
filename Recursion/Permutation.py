def method1(p,up):

    if not up:
        print(p)
        return 
    
    ch = up[0]
    for i in range(len(p)+1):
        new_processed = p[:i]+ch+ p[i:]
        method1(new_processed,up[1:])


def method2(arr,idx): # cannot go for swap as string is immutable
    if idx == len(arr):
        print(arr)
        return
    
    for i in range(idx,len(arr)):
        arr[i],arr[idx] = arr[idx],arr[i]
        method2(arr,idx+1)
        arr[i],arr[idx] = arr[idx],arr[i]

method2(['a','b','c'],0)