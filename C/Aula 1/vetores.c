#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int numero[10];
    int i, posicao, indice, novovalor;

    for (i = 0; i < 10; i++)
    {
        posicao = i + 1;
        numero[i] = i + 1;
        printf_s("Indice %d, Valor %d\n",posicao, numero[i]);
    }

    printf_s("Escolha o indice: ");
    scanf("%d", &indice);
    indice--;

    printf_s("Digite o novo valor para o indice: ");
    scanf("%d", &novovalor);

    numero[indice] = novovalor;

    for (i = 0; i < 10; i++)
    {
        posicao = i + 1;
        printf_s("Indice %d, Valor %d\n",posicao, numero[i]);
    }

    
    
    return 0;
}
