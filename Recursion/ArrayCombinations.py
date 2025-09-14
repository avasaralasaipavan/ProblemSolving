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

print(Logic2([1,2,3,4],0,[]))
        

