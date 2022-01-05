#include <stdio.h>
#include <stdalign.h>

int main(void)
{
    printf("Alignment requirement for char is %zu.\n", alignof(char));
    printf("sizeof char is %zu.\n", sizeof(char));
    printf("Alignment requirement for int is %zu.\n", alignof(int));
    printf("Alignment requirement for float is %zu.\n", alignof(float));
    printf("Alignment requirement for double is %zu.\n", alignof(double));
    return 0;
}
