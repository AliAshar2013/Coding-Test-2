print("Welcome to the grand calculator!")
try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    function = str(input("Which function would you like to use? (add, subtract, multiply, divide) : "))
    if function == "add":
       def add(a, b):
          return num_1 + num_2
       print("Sum is ", add(num_1, num_2))
    elif function == "subtract":
        def subtract(a, b):
          return num_1 - num_2
        print("Subtracting the numbers gives us the number ", subtract(num_1, num_2))
    elif function == "multiply":
        def multiply(a, b):
          return num_1 * num_2
        print("Multiplication of both numbers is ", multiply(num_1, num_2))
    elif function == "divide":
        def divide(a, b):
          return num_1 / num_2
        print("Division of both numbers is ", divide(num_1, num_2))
    else:
        print("That is not one of the functions!")

except ZeroDivisionError:
     print("Dividing a number by zero is an error!")
except ValueError:
     print("That is not a number!")