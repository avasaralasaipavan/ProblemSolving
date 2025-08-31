def Power(n,x):

    if x==0:
        return 1

    temp = x%2
    half = Power(n,x//2)
    if temp == 0:
        return  half*half 
    else: 
        return half*half*n
    
n=2
x=10

if x<0:
    x = -1*x
    data = 1/Power(n,x)
    print(data)

print(Power(n,x))
     

