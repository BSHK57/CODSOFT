def calculator():
    print("\n\n1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION\n\n")
    num1=float(input("ENTER 1st Number:"))
    num2=float(input("ENTER 2nd Number:"))
    operation=int(input("Choose the operation Choice:"))
    if operation==1:
        result=num1+num2
        print("Performing Addition!....")
    elif operation==2:
        result=num1-num2
        print("performing Subtraction!....")
    elif operation==3:
        result=num1*num2
        print("performing Multiplication!....")
    elif operation==4:
        if num2!=0:
            result=num1/num2
            print("performing Division!....")
        else:
            print("Operation Not Performed")
            result="Undefined (cannot divide by zero)"
    else:
        print("Invalid Choice")
    if operation in [1,2,3,4]:
        print(f"\nResult : {result}")
def main():
    print("....WELCOME To Simple Calculator....")
    while True:
        print("\n\n1. TO USE CALCULATOR")
        print("2. TO EXIT")
        choice=int(input("Enter Choice:"))
        if choice==2:
            print("Thank you \nProgram Exited")
            break
        elif choice==1:
            calculator()
        else:
            print("Invalid Choice \nTry Again")
if __name__=="__main__":
    main()
