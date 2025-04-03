def print_number_info(number):
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")

def process_number(number, callback):
    callback(number)

process_number(10, print_number_info)

enter_number = int(input("Enter a number: "))
process_number(enter_number, print_number_info)




    
    