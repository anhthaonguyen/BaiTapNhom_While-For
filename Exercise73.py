x=str(input())
y=len(x)
z=len(x)//2
Sn=''
print(x,' is',sep='',end=' ')
for i in range(0,y):
    if x[i] != ' ':
        Sn==x[i]
for j in range(z):
    if x[i] != x[-i-1]:
        print('not',sep='',end=' ')
        break
print('a palindrome')