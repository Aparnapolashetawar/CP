n=int(input())
cycles=1
while n!=1:
    
    if n%2==0:
        n=n/2
        cycles+=1
    else:
        n=(3*n)+1
        cycles+=1

        
print(cycles)
