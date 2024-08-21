# Definición de una cadena de caracteres en Python
str_a = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!', '\n', '\0']

# Concatenar la lista de caracteres en una sola cadena para imprimir
print("".join(str_a))

# Alternativa usando directamente una cadena en Python
str_b = "Hello, world!\n"
print(str_b)

# Manejando cadenas con operaciones de Python
# Las cadenas en Python son inmutables, pero puedes manipularlas de varias maneras
# Ejemplo de reemplazo de un carácter
str_c = list(str_b)  # Convertimos la cadena a una lista de caracteres para poder modificarla
str_c[6] = '-'
str_c = "".join(str_c)  # Volvemos a convertirla en cadena
print(str_c)

# Usando una función estándar de manipulación de cadenas en Python
# En lugar de strcpy(), en Python simplemente puedes asignar una nueva cadena
str_d = "Hello, Python!"
print(str_d)
