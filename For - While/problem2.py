#Try to find out if a number you get from the user is an "Armstrong" number.
#For example; If a number is digits and the sum of the 4th power of each of the number is equal to that number, then this number is called
#the "Armstrong" number.
a=0
number= input("Enter a number :")
digit= (len(number))
for i in number:
    a += int(i)**digit
if a == int(number):
    print("It is a Armstrong number.")
else:
    print("It is not a Armstrong number.")
