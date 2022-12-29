from poker import Poker

class Rule(Poker):
    def __init__(self, person=0, times=0, take=0):
        super().__init__(person, times, take)

    def wash(self, times=0):
        return super().wash(times)
    
    #發牌
    def give(self):
        t_lst=[] #所有玩家的牌
        for i in range(1,self.person +1):
            player_lst=[] #個別玩家的牌
            print( f"player[ {i} ]:" ,end="") 
            for j in range(self.take):
                num = Poker.p_lst.pop() #取出p_lst裡的任意元素
                player_lst.append(num)
                print( f"{Poker.c[num%4]}{Poker.p[num//4]:3s}",end="" )
            t_lst.append(player_lst)
            print("")
        print(t_lst)
#test
# a = Poker(4,100,5)
# a.give()
b = Rule(2,3,4)