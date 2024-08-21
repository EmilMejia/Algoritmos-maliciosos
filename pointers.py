def main():
    str_a = "Hello, world!\n"  # A string variable (similar to a character array in C)
    pointer = str_a  # Set pointer to the string
    print(pointer)  # Print the string

    # Simulate pointer manipulation
    pointer2 = pointer[2:]  # Pointer2 starts 2 characters into the string
    print(pointer2)  # Print starting from the 2nd character

    # Simulate string copy into the new location
    pointer2 = "y you guys!\n"  # Replace content starting from position 2
    str_a = str_a[:2] + pointer2  # Concatenate the unchanged start with the new content

    print(str_a)  # Print the modified string

if __name__ == "__main__":
    main()
