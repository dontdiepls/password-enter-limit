password = "a123456"
login_limit = 3
while login_limit > 0:
    user_login = input("请输入密码: ").lower()
    if user_login == password:
        print("登录成功")
        break
    else:
        login_limit -= 1
        print(f"密码错误，你还有{login_limit}机会")
