str1 = input('Enter string as a input : ')
if ' ' in str1:
    print('Wrong input')
else:
    
    
    res =str1.replace("G","").replace("EF","").replace("56","")
    
    print(res)