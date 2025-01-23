def encrypt_string(input_string):
    # Step 1: Reverse the string
    reversed_string = input_string[::-1]
    
    # Step 2: Replace vowels with their ASCII value
    vowels = 'aeiouAEIOU'
    encrypted_string = ''
    for char in reversed_string:
        if char in vowels:
            encrypted_string += str(ord(char))
        else:
            encrypted_string += char
    
    # Step 3: Append the length of the original string at the end
    encrypted_string += str(len(input_string))
    
    return encrypted_string

# Example usage
if __name__ == "__main__":
    sample_string = "hello"
    encrypted = encrypt_string(sample_string)
    print(f"Encrypted string: {encrypted}")