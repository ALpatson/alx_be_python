"""nstructions:

Prompt for User Input:

Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
Make sure you use num1 and num2 for first and second numbers
Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.
Perform the Calculation Using Match Case:

Implement a Match Case statement that executes the chosen operation based on the user’s input.
For addition (+), subtract (-), multiply (*), and divide (/).
Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.
Output the Result:

Display the result of the operation in a user-friendly message, e.g., The result is [result]."""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, / ): ")

match operator:
    case "+" :
        result = first_number + second_number
        print(f"The result is {result}")
        
    case "*" :
        result = first_number * second_number
        print(f"The result is {result}")
        
    case "-" :
        result = first_number - second_number
        print(f"The result is {result}")
        
    case "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"The result is {result}")
    case _:
        print("Invalid operator selected.")
        