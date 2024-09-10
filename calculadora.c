#include <stdio.h>

int main()
{

    int numero1, numero2, resultado;
    char operador;

    printf("Ingrese el primer numero: ");
    scanf("%d", &numero1);

    printf("Ingrese el operador: +, -, *, /");
    scanf(" %c", &operador);

    printf("Ingrese el segundo numero: ");
    scanf("%d", &numero2);

    // operaciones

    switch (operador)
    {
    case '+':
        resultado = numero1 + numero2;
        printf("El resultado de %d + %d es: %d\n", numero1, numero2, resultado);

        break;

    case '-':
        resultado = numero1 - numero2;
        printf("El resultado de %d + %d es: %d\n", numero1, numero2, resultado);
        break;

    case '*':
        resultado = numero1 * numero2;
        printf("El resultado de %d * %d es: %d\n", numero1, numero2, resultado);
        break;

    case '/':
        resultado = numero1 / numero2;
        printf("El resultado de %d / %d es: ", numero1, numero2, resultado);
        break;

     default:
        printf("Operador inválido.\n");
    }

    return 0;
}