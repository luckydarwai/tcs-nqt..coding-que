T = int(input('Enter the size '))
arr = []
k=[]
for i in range(T):
    arr.append(int(input()))
print(arr)
if arr.count(0)==0 or arr.count(1)==0:
    print(None)
else:
   for i in range(0,T):
       if arr[i]==0:
           for j in range(i,T):
               x=[]
               if arr[j]==1:
                   x.append(i)
                   x.append(j)
                   k.append(x)
   print(k)