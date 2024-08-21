def main():
    int_var = 5
    # Simula un puntero que almacena la "dirección" de int_var
    int_ptr = int_var
    
    # Imprime el valor de la variable
    print(f"Value of int_var: {int_var}")
    
    # Simula obtener la dirección de int_var
    # En Python, esto no tiene sentido real, pero se puede mostrar el valor
    print(f"Simulated address of int_var: {id(int_var)}")
    
    # El puntero int_ptr contiene el valor de int_var (simulación)
    print(f"Value at 'pointer': {int_ptr}")
    
    # Simula la dirección de int_ptr (la "dirección" donde se guarda int_ptr)
    # En Python, simplemente mostramos el ID de int_ptr
    print(f"Simulated address of int_ptr: {id(int_ptr)}")
    
    # El valor al que apunta 'int_ptr' (simulación de desreferenciación)
    print(f"Value pointed to by 'pointer': {int_ptr}")

if __name__ == "__main__":
    main()
