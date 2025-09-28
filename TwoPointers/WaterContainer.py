def WaterContainer(arr):
    left = 0
    right = len(arr)-1

    maxArea = 0
    while left<right:

        length = min(arr[left],arr[right])
        width = right-left
        maxArea = max(maxArea,length*width)

        if arr[left]>arr[right]:
            right-=1
        else:
            left+=1

    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(WaterContainer(height))

