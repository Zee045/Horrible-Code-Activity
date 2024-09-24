print("Simple Calculator program")
def add(a, b):
  return a + b #Add two values 

def subtract(a, b):
  return a -b #subtract two values

def multiply(a, b):
  return a * b #multiple two values

def main():
  Print("Select operation:")
  print("1- Add")
  print("2- Subtract")
  print("3- Multiply")
  choice = input("Enter choice of 1/2/3:")
  if choice in ['1','2','3']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
      print(f"The adding result is: {add(num1, num2)}")
    elif choice == '2':
      print(f"The subtraction result is: {subtract(num1, num2)}")
    elif choice == '3':
      print(f"The multiplication result is: {multiply(num1, num2)}")
  else:
    print("Invalid input")
if __name__ =="__main__":
  main()
        


