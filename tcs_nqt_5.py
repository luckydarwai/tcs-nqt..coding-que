N = int(input('Enter the Number of Entering and leaving person '))
E = []
L = []
list = []
Add = 0
print('Enter the no. of Entering people by at a time :')
for i in range(N):
    E.append(input())
print('Enter the no. of leaving people by at a time :')
for i in range(N):
    L.append(input())

for i in range(N):
   
    Add=Add+int(E[i])-int(L[i])
    list.append(Add)
print(list)
list.sort()
print(list[-1])
    