#Loops Homework 1

# Try to find out if the number you received from the user is perfect.
#A perfect number is a whole number, an integer greater than zero;
# and when you add up all of the factors less than that number, you get that number.

a = int(input("Enter a number :"))
b = list(range(1,a))
c= list()
d= 0
for i in b:
    if a%i == 0:
        c.append(i)
for i in c:
    d += i5
if d == a :
    print("It is a perfect number!!!")
else:
    print("It is not a perfect number!!!")

# I have done without going back to notes but i think there will be short way. :)