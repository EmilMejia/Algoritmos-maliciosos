def test_function(a, b, c, d):
    flag = 31337
    buffer = [''] * 10  # Similar to a character array in C
    buffer[0] = 'A'
    
    print("flag =", flag)
    print("buffer[0] =", buffer[0])
    print("buffer =", buffer)

def main():
    test_function(1, 2, 3, 4)

if __name__ == "__main__":
    main()
