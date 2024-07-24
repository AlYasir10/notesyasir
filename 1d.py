# program to reverse the number, create a function
print("Yasir   - 34")
def revnum(num):
    
    sum = 0
    while num!=0:
        rem=num%10
        sum=sum*10+rem
        num=num//10
        
    print("Reverse number is: ", sum)

num = int(input("Enter a number: \n"))
revnum(num)
