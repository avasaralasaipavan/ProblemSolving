from typeguard import typechecked

def valid_condition(arr:list[int],n:int,k:int):
    return sum(arr) == n and len(arr) == k
      

@typechecked
def generateCombination(arr,start:int,curr:list[int],n:int,k:int):

    if valid_condition(curr,n,k):
        print(curr)
        arr.append(curr[:])
        return
    
    for i in range(start,n+1):
        curr.append(i)
        generateCombination(arr,i+1,curr,n,k)
        curr.pop()

k = 3
n = 7
arr = []
generateCombination(arr,1,[],n,k)
print(arr)