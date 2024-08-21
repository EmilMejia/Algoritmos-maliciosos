import struct

# Función para mostrar el tamaño y el rango de los enteros
def show_sizes():
    print(f"'int' data type is \t\t {struct.calcsize('i')} bytes")
    print(f"'unsigned int' data type is \t {struct.calcsize('I')} bytes")
    print(f"'short int' data type is \t {struct.calcsize('h')} bytes")
    print(f"'long int' data type is \t {struct.calcsize('l')} bytes")
    print(f"'long long int' data type is {struct.calcsize('q')} bytes")
    print(f"'float' data type is \t {struct.calcsize('f')} bytes")
    print(f"'char' data type is \t\t {struct.calcsize('c')} bytes")

# Función para mostrar cómo funciona el complemento a dos
def show_twos_complement():
    # 8-bit signed integer representation of 73
    value = 73
    signed_value = struct.pack('b', value)
    unsigned_value = struct.unpack('B', signed_value)[0]
    print(f"Original value (73): {value}")
    print(f"Signed value: {signed_value}")
    print(f"Unsigned interpretation: {unsigned_value}")

    # Flip bits and add 1 (two's complement)
    flipped = ~unsigned_value & 0xFF
    twos_complement = (flipped + 1) & 0xFF
    print(f"Flipped bits: {flipped}")
    print(f"Two's complement: {twos_complement}")

    # Add original value and its two's complement
    result = unsigned_value + twos_complement
    print(f"Sum of original and two's complement: {result}")

if __name__ == "__main__":
    show_sizes()
    print("\nTwo's Complement Example:")
    show_twos_complement()
