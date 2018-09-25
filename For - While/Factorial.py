print("""
******************************
Calculating Factorial

Press "q" to quit.

******************************
""")

while True:
    number = input("Number:")
    if(number== "q"):
        print("Ending....")
        break
    else:
        number = int(number)
        factoriel =1
        for i in range(2,number+1):
            print("Factoriel:",factoriel,"i:",i)
            factoriel *=i
        print(factoriel)

