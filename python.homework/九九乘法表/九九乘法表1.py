#九九乘法表
#先輸出左上角的空白

print(' ',end='')
for i in range(1,10):
    print(f'{i:3d}',end='') #上面的y，把輸出設成3位數，讓下面可對齊
for x in range(1,10):
    print('\n'+str(x),end='') #x軸
    for y in range(1,10):
        print(f'{ x*y:3d}',end='') #乘積