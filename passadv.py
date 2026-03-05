import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

try:
    length = int(input("Enter the length of the password (max: 12): "))
    if length >12:
        raise ValueError("Length must be 12 or less: ")
    else:
        password =generate_password(length)
        print("Password Generated:",password)
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")



