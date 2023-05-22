import math
print("""**************
      
ADVANCED CALCULATOR

1 ADDITION
2 SUBTRACTION
3 MULTIPLICATION
4 DIVISION
5 EXPONENTIATION
6 SQUARE ROOT
7 LOGARITHM
8 SINE
9 COSINE
10 TANGENT
11 FACTORIAL

Press 'q' to exit.

*************""")

while True:
    choice = input("Please select an operation: ")
    if choice == "q":
        print("Exiting the program...")
        break
    else:
        choice = float(choice)

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))
        if choice == 1:
            result = num1 + num2
            print(num1, "+", num2, "=", result)
            continue
        elif choice == 2:
            result = num1 - num2
            print(num1, "-", num2, "=", result)
            continue
        elif choice == 3:
            result = num1 * num2
            print(num1, "*", num2, "=", result)
            continue
        elif choice == 4:
            result = num1 / num2
            print(num1, "/", num2, "=", result)
            continue

    elif choice == 5:
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))
        result = math.pow(num1, num2)
        print("Result:", result)

    elif choice == 6:
        num1 = float(input("Please enter a number: "))
        result = math.sqrt(num1)
        print("Result:", result)

    elif choice == 7:
        num1 = float(input("Please enter the number to take the logarithm of: "))
        base = float(input("Please enter the logarithm base: "))
        result = math.log(num1, base)
        print("Result:", result)

    elif choice in [8, 9, 10]:
        degree = float(input("Please enter the degree: "))
        radian = math.radians(degree)
        
        if choice == 8:
            result = math.sin(radian)
            print("Result:", result)
        elif choice == 9:
            result = math.cos(radian)
            print("Result:", result)
        elif choice == 10:
            result = math.tan(radian)
            print("Result:", result)
        
    if choice == 11:
        num1 = int(input("Please enter a number: "))
        result = math.factorial(num1)
        print("Result:", result)
