import sys

def fatal(message):
    error_message = "[!!] Fatal Error " + message
    print(error_message, file=sys.stderr)
    sys.exit(-1)

def ec_malloc(size):
    try:
        return bytearray(size)
    except MemoryError:
        fatal("in ec_malloc() on memory allocation")
