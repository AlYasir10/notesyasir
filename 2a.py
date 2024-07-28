print("Yasir   - 34")

def vowels(ch):
    if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print(ch, "is vowel..!!!")
    else:
        print(ch, "is not a vowel..!!!")
    vowels(ch)
    

ch = input("Enter a character: ")
vowels(ch)
