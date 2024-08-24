import os

def main():
    print(f"real uid: {os.getuid()}")
    print(f"effective uid: {os.geteuid()}")

if __name__ == "__main__":
    main()
