import random
c=['黑桃','紅心','方塊','梅花']
p=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
poker=list(range(0,52))
print(poker)
for i in range(1000): #洗牌 
    p1=random.randint(0,51)
    p2=random.randint(0,51)
    t=poker[p1]       #(不斷將牌的位置兌換)
    poker[p1]=poker[p2]
    poker[p2]=t
print('洗牌過後:'+str(poker))

for i in range(1,5): #發牌給四名玩家
    print(f'User[{i:>02}]:',end='')
    for j in range(0,13): #一人12張
        num= poker.pop() #隨機delete list裡其中一個元素，並回傳刪除的元素值(牌不會重複)
        print( c[num%4] + p[num//4],end='  ') #隨機的牌
    print('')