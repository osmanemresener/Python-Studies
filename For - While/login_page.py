print("""******************
Login Page Program
******************
""")
sys_account = "Emre"
sys_password = "12345"
login_attempt = 3

while True:
        account = input("Account :")
        password = input("Password :")
        if (account != sys_account and password == sys_password):
            print("Account name is wrong....")
            login_attempt -= 1
        elif (account == sys_account and password != sys_password):
            print("Password is wrong.....")
            login_attempt -= 1
        elif (account != sys_account and password != sys_password):
            print("Account Name and Password is wrong.....")
            login_attempt -= 1
        else:
            print("Login successfull...")
            break
        if (login_attempt == 0):
            print("Login attempt is 0 ")
            break
