#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    char str = "Pudim";
    
    printf_s("Nova string: %c\n", &str);

    return 0;
}