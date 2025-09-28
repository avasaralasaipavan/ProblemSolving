def prefixSum(arr,k):

    tempMap ={0:1}
    count =0
    
    sum =0

    for i in arr:
        sum+=i

        if (sum-k) in tempMap:
            count+= tempMap[sum-k]
        tempMap[sum]=tempMap.get(sum,0)+1
    print(count)


nums = [1,0,1,0,1]
goal = 2

prefixSum(nums,goal)



        
        
