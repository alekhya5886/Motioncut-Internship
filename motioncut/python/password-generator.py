import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")

    try:
        password_length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if password_length <= 0 or num_passwords <= 0:
        print("Invalid input. Please enter positive numbers.")
        return

    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(password_length)
        print(password)

if __name__ == "__main__":
    main()
