#include <stdlib.h>
#include "stdio.h"
#include ""

void is_null(void *ptr) {
    if (ptr == NULL) {
        exit(52);//да здравствует Санкт Питербург, и это город наш
    }
}




int main(int argc, char *argv[]) {
    if (argc != 3) {
        return 42;
    }
    printf("\n\n%s\n\n", argv[1]);
    FILE *input = fopen(argv[1], "r");
    is_null(input);
    int number_request;
    float error_probability;
    fscanf(input, "%d %f", &number_request, &error_probability);
    printf("%d %f", number_request, error_probability);
    int

}