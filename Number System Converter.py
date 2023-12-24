# This Python program allows users to convert a number from one number system to another.
# It defines a function, convert_number, that takes three parameters: 
# number (the number to be converted), from_base (the base of the input number), 
# and to_base (the base to which the number should be converted).
# The program uses built-in Python functions to convert the input number to base 10 
# and then converts it to the desired base by performing repeated division 
# and storing remainders until the quotient becomes zero.
# Users can input the number, its base, and the target base to get the converted number.
# To use the program, run the main() function, which prompts the user for inputs.
def convert_number(number, from_base, to_base):
    # Convert number to base 10
    base_10 = int(str(number), from_base)
    
    # Convert base 10 number to target base
    converted_number = ""
    while base_10 > 0:
        remainder = base_10 % to_base
        converted_number = str(remainder) + converted_number
        base_10 //= to_base
    
    return converted_number if converted_number else "0"

def main():
    try:
        number = input("Enter the number you want to convert: ")
        from_base = int(input("Enter the base of the number you entered: "))
        to_base = int(input("Enter the base to which you want to convert: "))

        result = convert_number(number, from_base, to_base)
        print(f"The converted number is: {result}")
    except ValueError as e:
        print("Error:", e)
        print("Please enter valid numbers for conversion bases.")

if __name__ == "__main__":
    main()
