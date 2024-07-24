# program to generate fibonacci series
print("Yasir   - 34")
a = int(input("Enter a number: "))
x = 0
y = 1
for n in range(0,a):
    if (n<=1):
        c = n
    else:
        c=x+y
        x=y
        y=c
        print(c)