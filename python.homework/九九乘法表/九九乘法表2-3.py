#三角形九九乘法表 ( x+y<=10才輸出 )
print(' ',end='')
for i in range(1,10):
    print(f'{i:3d}',end='')
for x in range(1,10):
    print('\n'+str(x),end='')
    for y in range(1,10):
        if x+y<=10:
            print(f'{x*y:3d}',end='')
        else:
            print('   ',end='')