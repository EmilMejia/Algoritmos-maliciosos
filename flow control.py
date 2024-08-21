import ctypes
import struct

# Simulando un registro de CPU (por ejemplo, EIP)
# Usaremos un valor ficticio para el ejemplo
eip = ctypes.c_uint32(0x08048384)

# Muestra de bytes en memoria (equivalente a las instrucciones en ensamblador)
# Simulamos que estos bytes son lo que EIP estaría apuntando
memory = bytearray([0xc7, 0x45, 0xfc, 0x00, 0x00, 0x00, 0x00, 0x83])

# Función para mostrar la memoria en diferentes formatos
def show_memory_formats(mem):
    print("Bytes en memoria:", mem.hex())
    print("Formato Octal:", oct(int.from_bytes(mem, 'little')))
    print("Formato Hexadecimal:", hex(int.from_bytes(mem, 'little')))
    print("Formato Decimal sin signo:", int.from_bytes(mem, 'little'))
    print("Formato Binario:", bin(int.from_bytes(mem, 'little')))

# Mostrar la memoria a la que apunta EIP en diferentes formatos
print("Dirección apuntada por EIP:", hex(eip.value))
show_memory_formats(memory[:4])

# Cambiar el tamaño de la unidad (byte, halfword, word, etc.)
# Usamos struct para interpretar los bytes
print("\nInterpretación como diferentes tamaños:")
print("Byte:", [b for b in memory[:4]])
print("Halfword (2 bytes):", [struct.unpack('<H', memory[i:i+2])[0] for i in range(0, 4, 2)])
print("Word (4 bytes):", struct.unpack('<I', memory[:4])[0])

# Little-endian vs Big-endian
print("\nInterpretación Little-endian vs Big-endian:")
print("Little-endian:", int.from_bytes(memory[:4], 'little'))
print("Big-endian:", int.from_bytes(memory[:4], 'big'))

# Simulando el siguiente paso de la ejecución en ensamblador
# Por ejemplo, moviendo un valor a una posición en memoria
# Simulamos ejecutar la instrucción `mov DWORD PTR [ebp-4],0x0`
print("\nSimulando la ejecución de una instrucción ensamblador:")
memory_to_modify = bytearray([0xc0, 0x83, 0x04, 0x08])
print("Memoria antes de la operación:", memory_to_modify.hex())
memory_to_modify[:4] = (0).to_bytes(4, byteorder='little')
print("Memoria después de la operación:", memory_to_modify.hex())

# Ejecución de la siguiente instrucción (como en `nexti`)
# En Python no hay "punteros" como en C, pero podemos simular la ejecución de una instrucción
print("\nEjecución simulada de la instrucción y cambio en EIP:")
eip.value += 4  # Avanzamos EIP al siguiente conjunto de bytes en memoria
print("Nuevo valor de EIP:", hex(eip.value))
