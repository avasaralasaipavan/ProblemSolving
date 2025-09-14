def generatePermutations(nums,idx,result,hMap):

    if idx == len(nums):
        if str(nums) not in hMap:
            result.append(nums[:])
            hMap[str(nums)]=nums
        return
    for i in range(idx,len(nums)):
        nums[i],nums[idx] = nums[idx],nums[i]
        generatePermutations(nums,idx+1,result,hMap)
        nums[i],nums[idx] = nums[idx],nums[i]

result = []
hMap = {}  #added changes
generatePermutations([1,1,2],0,result,hMap)
print(result)