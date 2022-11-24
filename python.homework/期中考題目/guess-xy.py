
#split(str=分隔符,num+1))
xg,yg=(input('請輸入座標位置:')).split(",")

#產生隨機座標
import random
x=random.randint(1,10)
y=random.randint(1,10)

#距離差
r= ( ((float(xg)-x)**2) + ((float(yg)-y)**2) )**0.5

#答題迴圈
while r!=0:
    print("距離還差:",r,)
    xg,yg=(input('請輸入座標位置:')).split(",")
    r= ( ((float(xg)-x)**2) + ((float(yg)-y)**2) )**0.5
print('恭喜過關')
