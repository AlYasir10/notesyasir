print("Yasir   - 34")
def palin(num):
    sum=0
    temp=num
    while temp!=0:
        rem = temp%10
        sum=sum*10+rem
        temp=temp//10

    if num==sum:
        print("the number is palindrome")
    else:
        print("the number is not palindrome")

num = int(input("Enter a number: " ))
palin(num)