class View():
    admin = "admin"
    password = "123456"
    #登录操作
    def login(self):
        a = input("请输入登录名：")
        b = input("请输入密码：")
        if a == View.admin and b == View.password:
            return True
        else:
            return False
    #系统欢迎界面
    def welcome(self):
        print("*************************************")
        print("**                                ***")
        print("***     欢迎进入小帅银行           ***")
        print("***                               ***")
        print("*************************************")

    #操作界面
    def opration(self):
        print("*************************************")
        print("**      开户(1)     查询(2)        ***")
        print("***     存钱(3)     取钱(4)        ***")
        print("***     转账(5)     改密(6)        ***")
        print("***     挂失(7)     解锁(8)        ***")
        print("***     退出(9)     销户(0)        ***")
        print("*************************************")

