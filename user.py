#用户类  包括：姓名  身份证号 卡 手机号
class User():
    def __init__(self,name,userid,card,phone):
        self.name = name
        self.userid = userid
        self.card = card
        self.phone = phone
    def __str__(self):
        return self.name
    __repr__ = __str__