#設定題目
import random
nu=random.randint(0,100)
print(nu)

#判斷
for i in range(0,7):
    inp=int(input('輸入一個數字'))

    if nu>inp:
        print('太小了')
    
    elif nu<inp:
        print('太大了')
    
    else:
        print('猜對了')
        break
        
print('game over')




