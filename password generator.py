import random

def generate_password(length):
    chars = ""
    complexity = input("Enter complexity level (1 for low, 2 for medium, 3 for high): ")
    
    if complexity == '1':
        chars += "abcdefghijklmnopqrstuvwxyz"
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars += "0123456789"
    elif complexity == '2':
        chars += "abcdefghijklmnopqrstuvwxyz"
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars += "0123456789"
        chars += "!@#$%^&*()-_+=[]{}|;:,.<>?/~"
    elif complexity == '3':
        chars += "abcdefghijklmnopqrstuvwxyz"
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars += "0123456789"
        chars += "!@#$%^&*()-_+=[]{}|;:,.<>?/~"
    else:
        print("Invalid complexity level. Defaulting to medium complexity.")
        chars += "abcdefghijklmnopqrstuvwxyz"
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars += "0123456789"
        chars += "!@#$%^&*()-_+=[]{}|;:,.<>?/~"
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
