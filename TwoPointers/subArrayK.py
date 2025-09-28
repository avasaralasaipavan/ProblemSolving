from collections import defaultdict


def atMostKDistinct(nums, k):
    count = defaultdict(int)
    start = 0
    result = 0

    for end in range(len(nums)):
       
        if count[nums[end]] == 0:
            k -= 1
        count[nums[end]] += 1

        
        while k < 0:
            count[nums[start]] -= 1
            if count[nums[start]] == 0:
                k += 1
            start += 1

       
        result += end - start + 1

    return result  


def subarraysWithKDistinct(nums, k):
    return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)

print(subarraysWithKDistinct([1,2,1,2,3],2))