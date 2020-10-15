li=[]
n=int(input("enter the no of elements"))
for i in range(n):
    x=int(input())
    li.append(x)
print(li)
lsub=[]
ls=[]
count=0
for i in range(len(li)):
    if i+1<=len(li)-1:
        lsub.append(abs(li[i+1]-li[i]))
for k in range(len(lsub)-1):
    if k+1<=len(lsub)-1:
        z=abs(lsub[k+1]-lsub[k])
        if z==1:
            count+=1
            ls.append(z)
            continue

        
    


                  
        
print(count)
b=len(li)-2
print(b)
if count==b:
    print("True")
else:
    print("False")
