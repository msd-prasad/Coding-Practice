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
