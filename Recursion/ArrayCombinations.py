def ArrayCombinations(p,up):
    if len(up)==0:
        print(p)
        return
    
    for i in range(0,len(up)):
        p.append(up[i])
        ArrayCombinations(p,up[i+1:])
        p.pop()


def Logic2(arr,index,curr):
    #print(curr)
    if len(curr)==2:
        print(curr)
        return
    
    for i in range(index,len(arr)):
        curr.append(arr[i])
        Logic2(arr,i+1,curr)
        curr.pop()

    return ""

def subsets(arr,current,start,result):
    
    result.append(current[:])

    if current == len(arr):
        #print(current)
        return

    for i in range(start,len(arr)):
        current.append(arr[i])
        subsets(arr,current,i+1,result)
        current.pop()

result = []
subsets([1,2,2],[],0,result)
print(result)


        

