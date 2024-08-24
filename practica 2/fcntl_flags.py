import os

def display_flags(label, value):
    print(f"{label}\t: {value}\t:", end='')
    binary_print(value)
    print()

def binary_print(value):
    mask = 0xff000000  # Comenzar con una máscara para el byte más alto.
    shift = 256 * 256 * 256  # Comenzar con un desplazamiento para el byte más alto.
    
    for byte_iterator in range(4):
        byte = (value & mask) // shift  # Aislar cada byte.
        print(" ", end='')
        for bit_iterator in range(8):  # Imprimir los bits del byte.
            if byte & 0x80:  # Si el bit más alto en el byte no es 0,
                print("1", end='')  # imprimir un 1.
            else:
                print("0", end='')  # De lo contrario, imprimir un 0.
            byte *= 2  # Mover todos los bits a la izquierda en 1.
        mask //= 256  # Mover los bits en la máscara a la derecha en 8.
        shift //= 256  # Mover los bits en el desplazamiento a la derecha en 8.

def main():
    display_flags("O_RDONLY\t\t", os.O_RDONLY)
    display_flags("O_WRONLY\t\t", os.O_WRONLY)
    display_flags("O_RDWR\t\t\t", os.O_RDWR)
    print()
    display_flags("O_APPEND\t\t", os.O_APPEND)
    display_flags("O_TRUNC\t\t\t", os.O_TRUNC)
    display_flags("O_CREAT\t\t\t", os.O_CREAT)
    print()
    display_flags("O_WRONLY|O_APPEND|O_CREAT", os.O_WRONLY | os.O_APPEND | os.O_CREAT)

if __name__ == "__main__":
    main()
