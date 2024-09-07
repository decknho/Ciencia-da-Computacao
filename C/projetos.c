#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    float num1, num2, resultado;
    int operador;
    char simbolo_operador;

    printf("Digite dois numeros\n1° Numero: ");
    scanf("%f", &num1);
    printf("2° numero: ");
    scanf("%f", &num2);

    printf("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\nVocê deseja? ");
    scanf("%i", &operador);

    printf("O resultado de: ");
    switch (operador) {
        case 1:
            resultado = num1 + num2;
            printf("%.2f + %.2f = %.2f", num1, num2, resultado);
            break;
        case 2:
            resultado = num1 - num2;
            printf("%.2f - %.2f = %.2f", num1, num2, resultado);
            break;
        case 3:
            resultado = num1 * num2;
            printf("%.2f * %.2f = %.2f", num1, num2, resultado);
            break;
        case 4:
            resultado = num1 / num2;
            printf("%.2f / %.2f = %.2f", num1, num2, resultado);
            break;
        default:
            break;
    }

    return 0;
}