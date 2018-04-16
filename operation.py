import random
import os
import pickle
from bank.user import User
from bank.card import Card
class Operation():
    #先加载用户
    def __init__(self):
        self.load_user()
        #将存储文件数据的字典输出
        print(self.user_dict)
    def load_user(self):
        if not os.path.exists("user.txt"):
            self.user_dict = {}
        else:
            with open("user.txt","rb") as fp:
                self.user_dict = pickle.load(fp)
    #1.开户操作
    def kaihu(self):
        #输入姓名
        name = input("请输入姓名：")
        #输入身份证号
        userid = input("请输入身份证号：")

        #输入手机号
        phone = input("请输入手机号：")
        # 输入密码  需要两次输入密码进行确认
        password = self.get_password(flag=True)
        #随机生成卡号  随机生成
        cardid = self.get_cardid()
        print("卡号为：%s" % cardid)
        #此时生成完整卡对象
        card = Card(cardid,10,password)
        #用户对象
        user = User(name,userid,card,phone)
        #将用户保存起来
        self.user_dict[cardid] = user

    #1.1连续两次输入密码 获取密码
    def get_password(self,flag):
        while True:
            if flag == True:
                a = input("请输入密码：")
            else:
                a = input("请输入新密码：")
            b = input("请再确认密码：")
            if a == b:
                print("操作成功，密码请牢记")
                return a
            else:
                print("两次输入不一致，请重新输入")
    #1.2随机生成卡号  默认是6位数
    def get_cardid(self):
        while True:
            cardid = random.randint(111111,999999)
            #判断是否已经存在
            if cardid not in self.user_dict:
                return cardid
    #9.退出操作
    def exitbank(self):
        #保存数据
        with open("user.txt","wb") as fp:
            pickle.dump(self.user_dict,fp)
        print("亲 感谢使用")
    #2.查询余额
    def search_money(self):
        card = self.get_card_info()
        if card:
            print("账户余额为：%d" % card.money)

    #2.1查询卡的信息
    def get_card_info(self):
        cardid = int(input("请输入卡号："))
        print(self.user_dict)
        #判断卡号是否存在
        if cardid not in self.user_dict:
            print("卡号有误，请重新输入")
            return
        #卡号输入正确时 根据卡号找到字典中的用户信息
        user = self.user_dict[cardid]
        card = user.card
        #判断用户是否被锁定
        if card.islock:
            print("卡已被锁定，请解锁再继续")
            return

        #用户输入密码  检测是否超过三次
        if not self.check_password(card):
            print("密码输入三次错误，卡已被锁，请解锁再继续")
            return
        return card     #返回的是银行卡对象

    #2.1.1检测用户密码输入的次数
    def check_password(self,card):
        count = 0
        while True:
            psw = input("请输入密码：")
            if card.password == psw :
                return True
            else:
                print("输入密码不正确 请重新输入：")
                count +=1
                if count == 3:
                    card.islock = True
                    return False
    #3.存钱操作
    def save_money(self):
        card = self.get_card_info()
        if not card:
            return
        while True:
            money = int(input("请输入存钱的金额："))
            if money < 0:
                print("输入金额不对，请重新操作")

            else:
                card.money += money
                print("账户余额为：%d" % (card.money))
                break
    #4.取钱
    def get_money(self):
        card = self.get_card_info()
        if not card:
            return
        while True:
            money = int(input("请输入取钱金额："))
            if money < 0:
                print("输入金额不对，请重新操作")

            else:
                card.money -= money
                print("账户余额为：%d" % (card.money))
                break
    #5.转账
    def trans_money(self):
        #输入获取自己的卡
        card = self.get_card_info()
        if not card:
            return
        #输入对方的银行卡号
        otherid = int(input("请输入对方的银行账号："))
        if otherid not in self.user_dict:
            print("对方卡号不存在")
            return
        money = int(input("请输入转账金额："))
        while True:
            if money < 0 or card.money < money:
                print("请输入正确的转账金额：")
            else:
                break
        #根据对方卡号找到用户  进而找到卡
        otheruser = self.user_dict(otherid)
        othercard = otherid.card
        card.money -= money
        othercard.money += money
        print("%d向%d转了%d钱" % (card.cardid,otherid,money))

    #6.修改密码
    def change_password(self):
        #输入卡号 原始密码 新密码 确认新密码  保存
        card = self.get_card_info()
        if not card:
            return
        password1 = self.get_password(flag=False)
        #只要将银行卡对象中的密码修改 用户对象中的密码就会修改
        card.password = password1
        print("修改密码成功")
    #7.挂失
    def lock_card(self):
        card = self.get_card_info()
        if not card:
            return
        card.islock = True
        print("挂失成功")

    #8.解锁
    def unlock_card(self):
        cardid = int(input("请输入卡号："))
        #print(self.user_dict)
        # 判断卡号是否存在
        if cardid not in self.user_dict:
            print("卡号有误，请重新输入")
            return
        #得到用户
        user = self.user_dict[cardid]
        # 检查用户的卡是否已经锁定

        if not user.card.islock:
            print("卡没有锁住 无需此操作")
            return

        # 输入密码
        if not self.check_password(user.card):
            print("密码输入错误 解卡失败")
            return

        userid = input("请输入身份证号：")
        if userid != user.userid:
            print("输入身份证号不正确")
            return
        #解卡
        user.card.islock = False
        print("解卡成功")
    #9.销户
    def delete_user(self):
        card = self.get_card_info()
        if not card:
            print("卡号输入不正确")
            return
        #获取用户
        user = self.user_dict[card.cardid]
        # 判断卡里面是否有余额
        if card.money > 0:
            print("提现......")
            card.money = 0
        while True:
            flag = int(input("确认要销户吗？是请按1，返回请按2"))
            if flag == 2:
                return
            elif flag == 1:
                #字典删除是按照key键删除 用pop()删除
                self.user_dict.pop(card.cardid)
                print("销户成功")
                break

