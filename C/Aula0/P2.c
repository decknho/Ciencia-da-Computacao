#include <stdio.h>

int main() {
    int x, y;
    char op;
    
    printf("Você deseja?\n
    '+' - SOMAR\n
    '-' - SUBTRAIR\n
    '*' - MULTIPLICAR\n
    '/' - DIVIDIR\n");
    scanf_s("%c", &op);

    printf("Digite um numero:\n");
    scanf_s("%i", &x);

    printf("Digite outro numero:\n");
    scanf_s("%i", &y);

    switch (op)
    {
    case '+':
        printf("%i + %i = %i\n", x, y, x + y)
        break;
    case '-':
        printf("%i - %i = %i\n", x, y, x - y)
        break;
    case '*':
        printf("%i * %i = %i\n", x, y, x * y)
        break;
    case '/':
        printf("%i / %i = %i\n", x, y, x / y)
        break;
    
    default:
    printf("Opção invalida!")
        break;
    }
}