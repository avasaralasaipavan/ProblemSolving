from collections import deque
def MaxiumElements(nums:list[int],k:int):

    result = []
    q = deque()


    for i in range(0,k):
        while q and  nums[q[-1]]<=nums[i]:
            q.pop()
        q.append(i)

    for i in range(k,len(nums)):
        result.append(nums[q[0]])

        while (len(q)>0 and q[0]<=i-k):
            q.popleft() 

        while len(q)>0 and nums[q[-1]]<=nums[i]:
            q.pop()
        
        q.append(i)

    result.append(nums[q[0]])

    return result 


nums = [1,4,2,3]
k = 2
print(MaxiumElements(nums,k))
