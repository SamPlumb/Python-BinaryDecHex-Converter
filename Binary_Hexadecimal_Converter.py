# Binary / Hexadecimal / Decimal Converter

# Functions -

# Format binary string
def binary_format(input):
    space = " "
    binary = ""

    # Reverse binary string
    input = input[::-1]

    # Add 0 to string to make output padded correctly
    padding = len(input) / 4
    padding = padding - int(padding)

    if padding == 0.25:
        input = input + "000"
    elif padding == 0.5:
        input = input + "00"
    elif padding == 0.75:
        input = input + "0"

    # Add spaces to string every 4 characters
    for x in range(0, len(input), 4):
        binary += input[x:x + 4] + space

    # Remove extra space
    binary = binary[:-1]
    # Reverse binary string to correct way
    binary = binary[::-1]

    return binary


# Validate Binary Input
def validate_binary(input):

    input = user_input.replace(" ", "")

    valid = True

    for num in input:

        if num != "0" and num != "1":

            valid = False

            break

    return valid


# Validate Hexadecimal Input
def validate_hexadecimal(input):

    valid_chars = "0123456789abcdefABCDEF"

    valid = True

    for char in input:

        if char not in valid_chars:

            valid = False

            break

    return valid


# Binary to Decimal
def binary_dec(input):

    input = user_input.replace(" ", "")

    dec = 0

    for num in input:
        dec = dec*2 + int(num)

    return dec


# Hexadecimal to Decimal
def hex_dec(input):

    dec = int(input, 16)

    return dec


# Decimal to Binary
def dec_binary(input):

    binary = bin(int(input))

    return binary[2:]


# Decimal to Hexadecimal
def dec_hex(input):

    hexadecimal = hex(int(input))

    return hexadecimal[2:]


# Menus -

# Main Help Menu
def main_help():

    print("Type 'convert' to convert between Binary, Hexadecimal, Decimal")

    # print("Type 'calculate' to perform any calculations with Binary, Hexadecimal or Decimal values")

    print("Type 'quit' to exit")


# Convert Help Menu
def convert_help():

    print("Binary to Decimal = btd")

    print("Binary to Hexadecimal = bth")

    print("Decimal to Binary = dtb")

    print("Decimal to Hexadecimal = dth")

    print("Hexadecimal to Binary = htb")

    print("Hexadecimal to Decimal = htd")

    print("Type 'quit' to exit")


# Main Program Loop -

# Initialise Variables
running = True
main_menu = True
convert = False

while running:

    # Main Menu
    if main_menu:

        print("Binary / Hexadecimal / Decimal Converter")

        main_help()

        main_menu = False

    user_input = input("What Operation Would You Like To Perform?").lower()

    if user_input == "quit":

        exit()

    elif user_input == "help":

        main_help()

    elif user_input == "convert":

        convert = True

    # Converter
    while convert:

        user_input = input("What would you like to convert?").lower()

        if user_input == "quit":

            exit()

        elif user_input == "help":

            convert_help()

        # Binary To Decimal
        elif user_input == "btd":

            while convert:

                user_input = input(
                    "Enter Binary value to convert to Decimal:")

                if user_input.lower() == "quit":

                    exit()

                elif user_input.lower() == "help":

                    convert_help()

                # Perform Conversion
                elif validate_binary(user_input):

                    print(
                        f"'{user_input}' as a decimal value is: {binary_dec(user_input)}")

                    convert = False

                else:

                    print(f"'{user_input}' is not a valid input. Try Again")

        # Binary To Hexadecimal
        elif user_input == "bth":

            while convert:

                user_input = input(
                    "Enter Binary value to convert to Hexadecimal:")

                if user_input.lower() == "quit":

                    exit()

                elif user_input.lower() == "help":

                    convert_help()

                # Perform Conversion
                if validate_binary(user_input):

                    print(
                        f"'{user_input}' as a Hexadecimal value is: {dec_hex(binary_dec(user_input))}")

                    convert = False

                else:

                    print(f"'{user_input}' is not a valid input. Try Again")

        # Decimal to Binary -
        elif user_input == "dtb":

            while convert:

                print("Enter Decimal value to convert to Binary:")

                user_input = input()

                if user_input.lower() == "quit":

                    exit()

                elif user_input.lower() == "help":

                    convert_help()

                # Perform Conversion
                elif user_input.isdigit():

                    print(
                        f"{user_input} as a binary value is: {binary_format(dec_binary(user_input))}")

                    convert = False

                else:
                    print(f"'{user_input}' is not a valid input. Try Again")

        # Decimal to Hexadecimal -
        elif user_input.lower() == "dth":

            while convert:

                print("Enter Decimal value to convert to Hexadecimal:")

                user_input = input()

                if user_input.lower() == "quit":

                    exit()

                elif user_input.lower() == "help":

                    convert_help()

                # Perform Conversion
                elif user_input.isdigit():

                    print(
                        f"{user_input} as a hexadecimal value is: {(dec_hex(user_input))}")

                    convert = False

                else:
                    print(f"'{user_input}' is not a valid input. Try Again")

        # Hexadecimal to Binary -
        elif user_input.lower() == "htb":

            while convert:

                print("Enter Hexadecimal value to convert to Binary:")

                user_input = input()

                if user_input.lower() == "quit":

                    exit()

                elif user_input.lower() == "help":

                    convert_help()

                # Perform Conversion
                elif validate_hexadecimal(user_input):

                    print(
                        f"{user_input} as a binary value is {binary_format(dec_binary(hex_dec(user_input)))}")

                    convert = False

                else:

                    print(f"'{user_input}' is not a valid input. Try Again")

        # Hexadecimal to Decimal -
        elif user_input.lower() == "htd":

            while convert:

                print("Enter Hexadecimal value to convert to Decimal:")

                user_input = input()

                if user_input.lower() == "quit":

                    exit()

                elif user_input.lower() == "help":

                    convert_help()

                # Perform Conversion
                elif validate_hexadecimal(user_input):

                    print(
                        f"{user_input} as a binary value is: {(hex_dec(user_input))}")

                    convert = False

                else:

                    print(f"'{user_input}' is not a valid input. Try Again")

        # Invalid Input -
        else:
            print(f"'{user_input}' is not a valid input. Try Again")

            print("Type 'help' to display instructions")

    else:

        print(f"'{user_input}' is not a valid input. Try Again")

        print("Type 'help' to display instructions")
