#In each while loop, get a number from the user and add the numbers that the user enters to a variable named "total".
#  When the user presses the "q" key, end the loop and press the "total variable" on the screen

#start time = 22:24
total=0
while True:
    a= (input("Enter a number :"))
    if a == "q":
        print("Total :",total)
        break
    else:
        total += int(a)

#end time = 22:27

