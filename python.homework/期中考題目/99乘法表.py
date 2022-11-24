#input
n=int(input('請輸入一整數:'))
while n%2==0 :
    n=int(input('請輸入一整數:'))

#set

print('  ',end='')
for i in range(1,n+1):
    print( f'{i:4d}',end='' )
for x in range(1,n+1):
    print( '\n'+ f'{x:2d}',end='' )
    for y in range(1,n+1):
        if x-1==y//2 or (((n+1)/2)-x)==y//2:
            print('    ',end='')
        else:
            print(f'{x*y:4d}',end='')
