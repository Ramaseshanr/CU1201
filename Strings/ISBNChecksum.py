def is_valid_isbn10(isbn):
    """
    Check if a given ISBN-10 is valid.

    :param isbn: A string representing the ISBN-10 number (can include dashes).
    :return: True if valid, False otherwise.
    """
    # Remove any dashes
    isbn = isbn.replace("-", "")
    
    # Check if it has exactly 10 characters
    if len(isbn) != 10:
        return False

    # Validate each character
    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (i + 1)

    # Check the last character, which can be a digit or 'X'
    if isbn[9] == 'X':
        total += 10 * 10
    elif isbn[9].isdigit():
        total += int(isbn[9]) * 10
    else:
        return False

    # Verify the checksum
    return total % 11 == 0

# Example usage
isbn = "0-306-40615-2"
isbn = '81-85015-96-1'
if is_valid_isbn10(isbn):
    print(f"{isbn} is a valid ISBN-10.")
else:
    print(f"{isbn} is not a valid ISBN-10.")