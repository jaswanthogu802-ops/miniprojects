def divide(x,y):
    if y==0:
        return"error:division by zero!"
    return x/y

def calculator():
    print("welcome to python calculator!")
while True:
    print("\nselect operation:")
    print("1.additon")
    print("2.subraction")
    print("3.multiply")
    print("4.divide")
    choice=input("enter your choice (1/2/3/4):")
    if choice=='5':
        print("good bye!")
        break
    if choice not in ['1','2','3','4']:
        print("invalid input.please try again.")
        continue
    try:
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
    except valueError:
        print("invalid number input please enter numeric values.")
        continue
    if choice=="1":
        print("result:",(num1+num2))
    elif choice=="2":
        print("result:",(num1-num2))
    elif choice=="3":
        print("result:",(num1*num2))
    elif choice=="4":
        print("result:",(num1/num2))
    else:
        print("invalid choice!")

