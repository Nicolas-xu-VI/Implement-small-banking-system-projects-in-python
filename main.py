from bank.view import View
from bank.operation import Operation
def main():
    #先进行登录
    v = View()
    if not v.login():
        print("登录失败")
        return
    print("登录成功")
    #登录成功后进入到系统初始页面
    v.welcome()
    #出来操作界面
    print("请选取对应的操作")
    v.opration()

    #创建操作对象
    op = Operation()

    while True:
        num = input("请输入对应操作的数字：\n")
        if num == "1":
            #开户
            op.kaihu()
        elif num == "2":
            #查询
            op.search_money()
        elif num == "3":
            #存钱
            op.save_money()
        elif num == "4":
            #取钱
            op.get_money()
        elif num == "5":
            #转账
            op.trans_money()
        elif num == "6":
            #改密
            op.change_password()
        elif num == "7":
            # 挂失
            op.lock_card()
        elif num == "8":
            #解锁
            op.unlock_card()
        elif num == "0":
            #销户
            op.delete_user()
        elif num == "9":
            op.exitbank()
            break #退出

if __name__ == '__main__':
    main()