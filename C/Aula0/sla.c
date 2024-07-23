#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int x = 0;
    while (x <= 100)
    {
        if (x % 2 == 0)
        {
            printf("O número %i é PAR!\n", x);
        }
        else
        {
            printf("O número %i é IMPAR!\n", x);
        }
        x++;      
    }
    
    return 0;
}