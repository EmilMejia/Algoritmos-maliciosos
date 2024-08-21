#dis.dis(hello_world): Esto desensambla la función hello_world y muestra el bytecode de Python, que es una representación más cercana al código de máquina que el intérprete de Python entiende y ejecuta.
import dis

# Definimos una función simple
def hello_world():
    for _ in range(10):
        print("Hello, world!")

# Usamos el módulo 'dis' para mostrar el bytecode
dis.dis(hello_world)