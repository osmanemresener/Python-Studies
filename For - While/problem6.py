#We did not learn the solution of the problem here. Try to make a list of numbers from 1 to 100 using only logic and list comprehension.

#Note: We cannot learn every detail in programming. For this, there are things we learn in some places through trial and error. In this problem, you will learn how to use list comprehension with conditional situations through trial and error.

#Tip: Try to think simple.

#start time 22:48
b=list()
a = list(range(1,51))
for i in a:
    b.append(i*2)
print(b)
c = [i*2 for i in a]
print(c)
#other way

list1 = [x for x in range(1,101) if x%2 == 0]
print(list1)

#finish time 22:49