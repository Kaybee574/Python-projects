#Purpose:A program that adds numbers of different bases
#Date:29/03/2024
#Author:g24m5008

def change_to_base_10(num, base):
    """A function that converts a number from a given base to base 10."""
    #Intialize a result and a multiplier
    result = 0
    multiplier = 1
    while num > 0:
        dgt = num % 10  # Extract the last digit of num
        # Check if the digit is within the base
        if dgt >= base:
            return "Number is not in base " + str(base)
        result += dgt * multiplier  # Add the digit to the result in base 10
        multiplier *= base  # Update the multiplier
        num //= 10  # Remove the last digit of num
    return result

def change_from_base_10(num, base):
    """A function that converts a number from base 10 to a given base."""
    #Intialize a result and a multiplier
    result = 0
    multiplier = 1
    while num > 0:
        dgt = num % base  # Get the remainder of num divided by base
        result += dgt * multiplier  # Add the digit to the result in the given base
        multiplier *= 10  # Update the multiplier
        num //= base  # Remove the last digit of num
    return result

def main():
    """A main function that gets the input from the user, convert the numbers to base 10, add them, and convert the result to the specified base."""
    # Get the two numbers ,two bases and result base from the user
    num1 = int(input("Please enter the first number: "))
    base1 = int(input("Please enter the base of the first number: "))
    num2 = int(input("Please enter the second number: "))
    base2 = int(input("Please enter the base of the second number: "))
    result_base = int(input("Please enter the base for the result: "))
    # Convert the numbers to base 10
    num1_in_base_10 = change_to_base_10(num1, base1)
    num2_in_base_10 = change_to_base_10(num2, base2)
    # Add the numbers
    result_in_base_10 = num1_in_base_10 + num2_in_base_10
    # Convert the result to the specified base
    result = change_from_base_10(result_in_base_10, result_base)
    print("Result:", result, "(base ", result_base,")")

# Call the main function
if __name__ == "__main__":
    main()
