#include <stdio.h>
#include <stdlib.h>

void main() {
    int number;
    char caract;

    printf("Number of characters in the password : ");
    scanf("%d", &number);

    for (int i = 0; i < number; i++){
        caract = rand()%120;
        printf("%d", caract);
    }
    printf("\n");
}
