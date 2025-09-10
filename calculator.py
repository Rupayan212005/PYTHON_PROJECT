num1=int(input("Enter first number:"))
num2=int(input("Enter secound number"))


print("\nEnter 1 for addition")
print("\nEnter 2 for subtraction")
print("\nEnter 3 for divistion")
print("\nEnter 4 for multiplication")

Choice=int(input("\nEnter choice"))



if(Choice==1):
    Result=num1+num2
    print("your sum is:  ",Result)

elif(Choice==2):
    Result=num1-num2
    print("your subtraction is  ",Result)

elif(Choice==3):
    Result=num1/num2
    print("your division is  ",Result)

elif(Choice==4):
    Result=num1*num2
    print("your multiplication is  ",Result)

else:
    print("wrong choice")

