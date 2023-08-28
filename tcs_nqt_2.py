N  = int(input(' Enter the Number : '))

if N >= 1 and N <= 100:
    res = 0
    binary = []
    while N != 0:
      res = N % 2
      binary.append(res)
      N = N // 2
    binary.reverse()
    print(binary)
    for i in range(len(binary)):
          if binary[i]==0:
                binary[i]=1
                continue
          else:
                binary[i]=0
    print(binary)
    val =0
    for i in range(len(binary)):
          digit = binary.pop()
          if digit == 1  :
                val += pow(2,i)
    print('Decimal number is ',val)
    
    


    
    



    
    
          
    
else :
    print('Wrong input ')
