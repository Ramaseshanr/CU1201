import string
if __name__ == '__main__':
    password = input("Enter a password: ")
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if all([length, has_upper, has_lower, has_digit, has_special]):
        print("Strong password!")
    else:
        print("Weak password! Ensure it has 8+ characters, uppercase, lowercase, numbers, and special symbols.")
