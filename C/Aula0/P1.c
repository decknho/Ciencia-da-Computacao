#include <stdio.h>

int main() {
    printf("Olá, mundo!");
    int x, y, res;
    printf("Digite um numero: ");
    scanf_s("%i", &x);

    printf("Digite outro numero: ");
    scanf_s("%i", &y);

    res = x + y;

    printf("O resultado da soma de %i com %i é %i", x, y, res);
    if (x % 2 == 0) 
    {
        printf("A variavel 'X' é PAR")
    }
    else 
    {
        printf("A variavel 'X' IMPAR")
    }
    
    return 0;
}