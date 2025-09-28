def SlidingWindows(arr,total,k):
    n = len(arr)
    window_size =  n-k
    start = 0
    end = window_size
    minimum = 9999999
    while end<=n:        
        window = arr[start:end]
        minimum = min(minimum,sum(window))
        start+=1
        end+=1

    print(minimum,"->",total-minimum)



     


arr  =  [1,2,3,4,5,6,1]
k= 3

SlidingWindows(arr,sum(arr),k)