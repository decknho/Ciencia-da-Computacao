#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    char nome;
    printf_s("Nome completo:\n");
    scanf("%s", &nome);
    printf_s("Seu nome é %s, certo?\n", &nome);

    return 0;
}