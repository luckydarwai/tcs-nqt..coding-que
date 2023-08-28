S = input('Enter the string : ')
if len(S) != 50:
  if ' ' not in S : 
    a=0 
    b=0 
    for i in S:
       
       if i=='#':
         a+=1
         continue
       elif i=='*':
         b+=1
         continue
    if a>b:
      print(b-a)
    elif a==b:
        print(0)
    else:
        print(b-a)
  else:
     print('Wrong input ')