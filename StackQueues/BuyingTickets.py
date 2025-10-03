from collections import deque

def BuyingTickets(arr,k):

    q = deque()
    time = 0
    for i in range(len(arr)):

        q.append((arr[i],i))

    while q:

        count,index = q.popleft()

        time+=1
        count-=1

        if count==0 and index ==k:
            return time
        if count>0:
            q.append((count,index))
        print(q)
tickets = [5,1,1,1]
k = 0
print(BuyingTickets(tickets,k))