print("""
*****************************************

Welcome To ATM Machine

Operations;

1.Balance Inquiry

2.Deposit

3.Withdraw

If you want to quit program press :"q" ..
*****************************************

""")

balance = 1000

while True:
    operation = input("İşlemi seçiniz:")
    if (operation == "q"):
        print("Log-out successful!")
        break
    elif (operation == "1"):
        print("Your Balance is {} Euro".format(balance))
    elif (operation == "2"):
        amount= int(input("Enter amount :"))
        balance += amount
    elif (operation == "3"):
        amount = int(input("Enter amount :"))
        if (balance - amount) <0:
            print("Insufficient Balance")
            continue
        balance -= amount
    else:
        print("Invalid Operation!!")