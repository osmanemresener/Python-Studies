#Try to print the multiplication table with numbers from 1 to 10.

a= list(range(1,11))
b= list(range(1,11))
print(a)
for i in a:
    print("**************")
    for j in b:
        print("{} times {} = {}".format(i,j,i*j))

# I have started at 22:14 and finished at 22:21