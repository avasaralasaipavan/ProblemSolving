def FlipZeros(arr, k):
    start = 0
    maxWindowSize = 0
    zeroCount = 0

    for end in range(len(arr)):
        if arr[end] == 0:
            zeroCount += 1

        while zeroCount > k:
            if arr[start] == 0:
                zeroCount -= 1
            start += 1

        maxWindowSize = max(maxWindowSize, end - start + 1)

    return maxWindowSize


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(FlipZeros(nums,k))