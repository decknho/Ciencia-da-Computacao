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
        printf_s("%i = %d\n",posicao, numero[i]);
    }
    
    
    return 0;
}
