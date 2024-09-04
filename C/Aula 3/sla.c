#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    char str;
    scanf("%s", str);
    printf("Nova string: %s\n", str);

    return 0;
}