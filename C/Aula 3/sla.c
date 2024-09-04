#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int sla;
    printf("Digite uma string? \n");
    scanf_s("%i", &sla);
    printf("Nova string: %i", sla);

    return 0;
}