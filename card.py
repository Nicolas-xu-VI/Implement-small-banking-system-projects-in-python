#银行卡类  包括信息：卡号 金额 密码
class Card():
    def __init__(self,cardid,money,password):
        self.cardid = cardid
        self.money = money
        self.password = password
        #是否锁定
        self.islock = False