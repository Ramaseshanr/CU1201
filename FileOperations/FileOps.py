if __name__ == '__main__':
    file = None
    try:
        with open('Example.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        if file:
            file.close()
            print("File closed.")

        else:
            x = 5
            print(x.as_integer_ratio())
            print(bin(x))
            print(x.bit_count())
            print(x.bit_length())
            print(x.numerator)
            print(x.from_bytes(bin(x)))
            print("File not opened.")
            x = 'hello'
            x.
        print("Execution completed.")
