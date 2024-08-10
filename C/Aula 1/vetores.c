#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int numero[10];
    int i, posicao, indice, novovalor;

    for (i = 0; i < 10; i++)
    {
        posicao = i + 1;
        numero[i] = i;
        printf_s("Indice: %i = Valor: %d\n",posicao, numero[i]);
    }

    printf_s("Digite o indice do valor: ");
    scanf("%d", indice);


    printf_s("Digite o indice do valor: ");
    scanf("%d", novovalor);

    numero[indice] = novovalor;
    
    
    return 0;
}
