
print(' ',end='')

for i in range(1,10):
    print( f'{i:3d}' ,end='')
for x in range(1,10):
    print('\n'+str(x),end='')
    for y in range(1,10):
        if 2<=x<=7 and 3<=y<=7:
            print(f'{x*y:3d}',end='')
        else:
            print('   ',end='')