def partition(arr):
    
    i=0
    j =len(arr)-1
    
    iflag = False
    jflag = False
    
    while i<j:
        if arr[i]%2 ==0:
            i+=1
            iflag = True
        else:
            iflag =  False
            
        if arr[j]%2 !=0:
            j-=1
            jflag = True
        else:
            jflag = False
        
        if iflag==False and jflag==False:
            arr[i],arr[j] = arr[j],arr[i]
    #print(i,j)  
    return arr,i,j+1


def merge(left,right):
    
    sorted_array=[]
    m,n = len(left),len(right)
    
    
    i=j=0
    
    
    while i<m and j<n:
        if left[i]<right[j]:
            sorted_array.append(left[i])
            i+=1
            
        else:
            sorted_array.append(right[j])
            j+=1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array
    
def merge_sort(arr,mid = None):
    
    if len(arr)<=1:
        return arr
    if mid ==None:
        mid = len(arr)//2    
        
    left =  merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    
    
    return merge(left,right)

#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr):
		# code here
		
		
		arr,i,j =  partition(arr)
		
		data = merge_sort(arr[0:i])
		data1 = merge_sort(arr[j:])
		
		return data+data1
		

s= Solution()
print(s.segregateEvenOdd([12, 34, 45, 9, 8, 90, 3])	)

		
		
		