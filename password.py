import random

def gpass():
  length=int(input("Enter a Length For a Password:"))
  charecters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*+"
  password=""
  for i in range(length):
    password+=random.choice(charecters)
  print("Generated Password is:",password)


while True:
  
 print("PRESS 1 FOR GENERATING PASSWORD")
 print("PRESS 2 FOR END")
 choice=int(input("Enter choice between 1 and 2:"))


 if choice==1:
  gpass()
 elif choice==2:
  print("EXIT")
  break
 else:
  print("INVALID OPTION")