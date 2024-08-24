import os
import sys
from hacking import fatal, ec_malloc

def usage(prog_name, filename):
    print(f"Usage: {prog_name} <data to add to {filename}>")
    sys.exit(0)

def main():
    if len(sys.argv) < 2:
        usage(sys.argv[0], "/var/notes")

    buffer = ec_malloc(100)
    datafile = ec_malloc(20)
    datafile = "/var/notes"
    buffer = sys.argv[1].encode('utf-8')

    print(f"[DEBUG] buffer @ {hex(id(buffer))}: '{buffer.decode('utf-8')}'")
    print(f"[DEBUG] datafile @ {hex(id(datafile))}: '{datafile}'")

    try:
        with open(datafile, "ab") as fd:
            userid = os.getuid()
            fd.write(userid.to_bytes(4, 'little'))  # Write user ID
            fd.write(b"\n")
            fd.write(buffer)  # Write note
            fd.write(b"\n")
            print("Note has been saved.")
    except OSError as e:
        fatal(f"in main() while handling the file: {e}")

if __name__ == "__main__":
    main()
