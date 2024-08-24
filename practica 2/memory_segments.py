global_var = None  # Representa una variable global no inicializada
global_initialized_var = 5  # Representa una variable global inicializada

def function():
    stack_var = None  # Variable local, simulando una variable en el stack
    print(f"the function's stack_var is at address {id(stack_var):#010x}")

def main():
    stack_var = None  # Otra variable local, también en el stack
    static_initialized_var = 5  # Simulando una variable estática inicializada
    static_var = None  # Simulando una variable estática no inicializada
    heap_var_ptr = [None]  # Simulando una variable en el heap usando una lista
    
    # Variables globales y estáticas
    print(f"global_initialized_var is at address {id(global_initialized_var):#010x}")
    print(f"static_initialized_var is at address {id(static_initialized_var):#010x}\n")
    
    print(f"static_var is at address {id(static_var):#010x}")
    print(f"global_var is at address {id(global_var):#010x}\n")
    
    # Variable en el heap (simulada)
    print(f"heap_var is at address {id(heap_var_ptr):#010x}\n")
    
    # Variables en el stack
    print(f"stack_var is at address {id(stack_var):#010x}")
    function()

if __name__ == "__main__":
    main()
