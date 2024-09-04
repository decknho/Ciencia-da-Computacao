#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int x = 10;
    int *p_x = &x;
    printf_s("%i", &p_x);

    return 0;
}