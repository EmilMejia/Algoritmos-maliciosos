import pdb

# Función de ejemplo
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Inicia el depurador
pdb.set_trace()

# Llamada a la función
factorial(5)
