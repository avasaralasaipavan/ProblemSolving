#approach use merge sort then count arr[i]>arr[j] then count++
count = 0
def merge(left,right):
    
    i=j=0

    m,n = len(left),len(right)
    sorted_array = []

    while i<m and j<n:
        if left[i]<right[j]:
            sorted_array.append(left[i])

            i=i+1

        else:
            sorted_array.append(right[j])
            j+=1

            global count 
            count = count + len(left)-i

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

class Sort():
    

    def merge_sort(self,arr):


        if len(arr)<=1:
            return arr
        
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        data =  merge(left,right)
        return data
    def ans(self,arr):

        output = self.merge_sort(arr)
        return count

S= Sort()

print(S.ans([2, 3, 4, 5, 6]))


