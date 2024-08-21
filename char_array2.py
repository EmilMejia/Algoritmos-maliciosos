# Función que simula la operación de strcpy en C
def strcpy(dest, src):
    for i in range(len(src)):
        if i < len(dest):
            dest[i] = src[i]
        else:
            break
    return dest

def main():
    # Crear una lista con espacio para 20 caracteres
    str_a = [''] * 20

    # Simulamos el primer punto de interrupción en la línea anterior a strcpy()
    print("Breakpoint 1: Antes de strcpy()")
    print("Estado inicial de str_a:", str_a)

    # Llamamos a nuestra función strcpy personalizada
    strcpy(str_a, "Hello, world!\n")

    # Simulamos el segundo punto de interrupción después de strcpy()
    print("\nBreakpoint 2: Después de strcpy()")
    print("Estado de str_a después de strcpy():", "".join(str_a))

    # Imprimimos la cadena final
    print("\nOutput final:")
    print("".join(str_a))

# Ejecutar la función principal
main()
