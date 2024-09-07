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

    printf("Você deseja?\n 1 - Somar\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir\n ");
    scanf("%i", &operador);

    switch (operador) {
        case  1:
            simbolo_operador = ("+");
            resultado = num1 + num2;
            break;
        case  2:
            simbolo_operador = ("-");
            resultado = num1 - num2;
            break;
        case  3:
            simbolo_operador = ("*");
            resultado = num1 * num2;
            break;
        case 4:
            simbolo_operador = ("/");
            resultado = num1 / num2;
            break;
        default:
            break;
    }

    printf("%f %c %f = %f",&num1, &simbolo_operador, &num2, &resultado);

    return 0;
}