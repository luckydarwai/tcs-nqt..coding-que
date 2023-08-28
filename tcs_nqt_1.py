N = int(input('Enter the size of the array :'))
arr = list(map(int,input().split(' ')))

if len(arr)!= N:
    print('wrong input ')
else:
     a = []
     sum = 0
     for i in arr:
         if i not in a:
             a.append(i)
     
          
         else:
             
             i = i+1
             if i not in a:
              a.append(i) 
              continue
     for j in a:
        sum = sum + j
     print(a)
     print(sum)       


         
             
         
    