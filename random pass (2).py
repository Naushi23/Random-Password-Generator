import random
import string

# Function to generate a random password
def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if character_pool == "":
        return "Error: No character set selected."
    
    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Main function
def main():
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate and display password
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

# Run the generator
main()