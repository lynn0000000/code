
#set
import random

c=["黑桃","紅心","菱形","梅花"]
p=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]

poker=list(range(0,52))
print(poker)
#洗牌1000次(交換位置)
for i in range(1000):
    p1=random.randint(0,51)#從0~51之間隨機抓一個數
    p2=random.randint(0,51)
    t=poker[p1]
    poker[p1]=poker[p2]
    poker[p2]=t
print("洗牌過後",poker)

#發牌
lst=[]
#player
for i in range(1,3):
    print( f'player[{i:^3d}]:' ,end="")
    
    #一人五張
    for j in range(1,6):
        #隨機刪除poker裡的一元素，並傳回至num
        num=poker.pop()
        lst.append(num)
        print( " ",c[num%4] + p[num//4],end="" )
    print("")

#比大小

#兩人各自的牌
lst1=[]
lst2=[]
times=0
for r in lst:
    times+=1
    if times<=5:
        lst1.append(r)
    else:
        lst2.append(r)
    
pp=[]#放抽過的牌

#五回合
for t in range(1,6):
    #隨機出一張牌
    #不能重複
    p1p = random.choice(lst1)
    p2p = random.choice(lst2)
    while p1p in pp:
        p1p = random.choice(lst1)
    while p2p in pp:
        p2p = random.choice(lst2)

    pp.append(p1p)
    pp.append(p2p)

    print(f'第{t:1d}回合==>player[1]:',end='')
    print( c[ p1p%4 ] + p[p1p//4] ,end='')

    print(f', player[2]:',end='')
    print( c[ p2p%4 ] + p[p2p//4],end=", " )

    #先比數值在比花色
    if p1p//4 > p2p//4:
        print('player [1]:獲勝')
    elif p1p//4 == p2p//4:
        if p1p%4 < p2p<4:
            print('player [1]:獲勝')
        else:
            print('player [2]:獲勝')
    else:
        print('player [2]:獲勝')

    print('')
    
