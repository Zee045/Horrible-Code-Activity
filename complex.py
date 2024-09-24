Print("Complex calculator program")
def calculater():
  print("Select option: ")
  print("1- Add")
  print("2- subtract")
  print("3- multiple")
  print("4- divide")
  choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"The result is: {result}")
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"The result is: {result}")
    elif choice == '4':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = num1 / num2
    else:
        print("Invalid input")

calculator()
