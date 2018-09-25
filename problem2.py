#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

number= int(input("Enter a number :"))
list1=list(range(1,number+1))
a=1
for i in list1:
    a *= i
print(a)

(1,2,3,4,5)

1*2
2*3
3*4
4*5
