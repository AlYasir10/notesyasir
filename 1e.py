print("Yasir   - 34")
def arm(num):
    sum=0
    temp=num
    while temp>0:
        digit = temp%10
        sum += digit**3
        temp = temp//10

    if num==sum:
        print("The number is armstrong")
    else:
        print("The number is not armstrong")

num = int(input("Enter a number: "))
arm(num)