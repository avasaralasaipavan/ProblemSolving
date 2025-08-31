
def WaveArray(arr):

    length = len(arr)-1
    i=0
    while i+1 <= length:
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

        i+=2

    return arr

        

print(WaveArray([2]))