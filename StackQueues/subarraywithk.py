from collections import deque  


def findMax(nums,k):
    sum =0
    windowSize = 9999999
    flag = False
    q = deque()
    for i,value in enumerate(nums):  
        sum += value
        if sum >= k:
            flag = True
            windowSize = min(windowSize,i+1)

        while len(q) and q[-1][1] > sum:
            q.popleft()


        
        q.append([i,sum])
        print(q)
    while sum>k:
        index, element = q.popleft()
        sum-= element
        q[-1][1] = sum
    print(windowSize,sum)
    print(q)

    if flag:
        return  min(windowSize, i - q[0][0]+1)
    return -1
  

nums = [2,-1,2]
k = 3
print(findMax(nums,k))


