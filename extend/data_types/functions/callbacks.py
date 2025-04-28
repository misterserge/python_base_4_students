def print_number_info(number):
    """
    It checks if the number is even or odd and prints the result.
    Args:
        number (int): The number to check.
    Returns:
        None
    """
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")

def process_number(number, callback):
    callback(number)

def print_square_number(number):
    print(f"Square of {number} is {number ** 2}")

process_number(10, print_number_info)

enter_number = int(input("Enter a number: "))
process_number(enter_number, print_number_info)
process_number(enter_number, print_square_number)