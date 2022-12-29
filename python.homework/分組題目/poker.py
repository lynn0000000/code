#發牌( 洗牌，發牌，show )
import random

class Poker:
    def __init__(self,person = 0,take=0,times=0 ):
        self.set(person ,take )
        #牌庫
        self.c=["黑桃","紅心","菱形","梅花"]
        self.p=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.p_lst = list(range(52)) #52張撲克牌
        self.wash(times)

    #設定(人數，洗牌次數，發幾張牌)
    def set(self,person=0 ,take=0 ):
        #perosn
        if person>0:
            self.person = person
        else:
            self.person = 2
        # #times
        # if times>0: 
        #     self.times = times
        #take
        if take > 52 // self.person and take > 0: 
            self.take = 52 //  self.person
        else:
            self.take = take

    #洗牌
    def wash(self,times=0):
        if times >0:
            self.times = times
        else:
            self.times = 200
        for i in range(self.times+1):
            p1 = random.randint(0,51)
            p2 = random.randint(0,51)

            t = self.p_lst[p1]
            self.p_lst[p1] = self.p_lst[p2]
            self.p_lst[p2] = t
    #發牌
    def give(self):
        t_lst=[] #所有玩家的牌
        for i in range(1,self.person +1):
            player_lst=[] #個別玩家的牌
            print( f"player[ {i} ]:" ,end="") 
            for j in range(self.take):
                num = self.p_lst.pop() #取出p_lst裡的任意元素
                player_lst.append(num)
                print( f"{self.c[num%4]}{self.p[num//4]:3s}",end="" )
            t_lst.append(player_lst)
            print("")
        print(t_lst)
#test    
a = Poker(4 ,2 ,1000 )
a.wash(1000)
a.give()


