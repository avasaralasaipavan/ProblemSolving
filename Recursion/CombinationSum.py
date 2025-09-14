target = 7
def generateCombination(arr,start,current,remaining):
    if sum(current) == target:
        print(current)
        return
    if remaining == 0:
        print(current)
        return
    
    if remaining<0:
        return
    for i in range(start,len(arr)):
        #print(current)
        current.append(arr[i])
        generateCombination(arr,i,current,remaining-arr[i])
        #print("The current before pop,",current)
        current.pop()
        #print("The current after pop,",current)

arr = [2,3,6,7]
target = 7
generateCombination(arr,0,[],7)
