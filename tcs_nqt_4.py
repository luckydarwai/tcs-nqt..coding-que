N = int(input('Enter the size of '))
list1 =[]
for i in range(N):
    a = int(input())
    if a<=2 and a>=0:
        list1.append(a)
    else:
        print('Wrong input')
        break
print(list1)
list1.sort()
print(list1)
