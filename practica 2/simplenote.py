import os
import sys

def usage(prog_name, filename):
    print(f"Usage: {prog_name} <data to add to {filename}>")
    sys.exit(0)

def fatal(message):
    error_message = "[!!] Fatal Error " + message
    print(error_message, file=sys.stderr)
    sys.exit(-1)

def ec_malloc(size):
    try:
        return bytearray(size)
    except MemoryError:
        fatal("in ec_malloc() on memory allocation")

def main():
    if len(sys.argv) < 2:
        usage(sys.argv[0], "/tmp/notes")

    buffer = ec_malloc(100)
    datafile = "/tmp/notes"

    # Copia el argumento en el buffer
    buffer[:len(sys.argv[1])] = sys.argv[1].encode()

    print(f"[DEBUG] buffer @ {id(buffer):#010x}: '{buffer.decode().rstrip()}'")
    print(f"[DEBUG] datafile @ {id(datafile):#010x}: '{datafile}'")

    # Añade un salto de línea al final
    buffer[len(sys.argv[1]):len(sys.argv[1]) + 1] = b"\n"

    try:
        # Abrir el archivo para escritura, creación y añadir al final
        with open(datafile, 'ab') as f:
            print(f"[DEBUG] file descriptor is {f.fileno()}")
            f.write(buffer[:len(sys.argv[1]) + 1])
            print("Note has been saved.")
    except OSError as e:
        fatal(f"in main() while handling the file: {e}")

if __name__ == "__main__":
    main()
