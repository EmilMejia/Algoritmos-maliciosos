import random

def main():
    print(f"RAND_MAX is {2**31 - 1}")  # Simulating RAND_MAX from C
    random.seed()  # Initialize the random number generator with the current time
    print("random values from 0 to RAND_MAX")
    for _ in range(8):
        print(random.randint(0, 2**31 - 1))  # Print random values from 0 to RAND_MAX

    print("random values from 1 to 20")
    for _ in range(8):
        print(random.randint(1, 20))  # Print random values from 1 to 20

if __name__ == "__main__":
    main()
