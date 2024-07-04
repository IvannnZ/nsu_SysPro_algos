#include <stdlib.h>
#include "stdio.h"
#include <math.h>
//компилятору нужно добавить флаг -lm

#define big_simple_num 1306717

void is_null(void *ptr) {
    if (ptr == NULL) {
        exit(52);//да здравствует Санкт Питербург, и это город наш
    }
}

struct blum_filter {
    int size;
    int number_hash;
    float *arr_hash_seed;
    unsigned int *data;
};

unsigned int get_bit(const unsigned int *arr_ptr, unsigned int bit_num) {
    unsigned int place_in_arr = bit_num / sizeof(unsigned int);
    unsigned int place_in_num = bit_num % sizeof(unsigned int);
    return arr_ptr[place_in_arr] && (1 << place_in_num);
}

void set_bit(unsigned int *arr_ptr, unsigned int bit_num) {
    unsigned int place_in_arr = bit_num / sizeof(unsigned int);
    unsigned int place_in_num = bit_num % sizeof(unsigned int);
    arr_ptr[place_in_arr] = arr_ptr[place_in_arr] || (1 << place_in_num);
}

unsigned int hash(unsigned int value, float seed, int max_value) {
    int a;
    return (unsigned int) (modff(value * seed, &a) * max_value);
}

struct blum_filter create_blum_filter(int number_request, float error_probability) {
    struct blum_filter bf;
    int bit_for_elem = (int) (-log2((double) error_probability) / log((double) 2));
    bf.size = bit_for_elem * number_request;
    bf.data = (unsigned int *) malloc(((bf.size + sizeof(unsigned int)) / sizeof(unsigned int) + 7) / 8);
    is_null(bf.data);
    bf.number_hash = (int) -floor(log2(error_probability));
    bf.arr_hash_seed = (float *) malloc(sizeof(float) * bf.number_hash);
    is_null(bf.arr_hash_seed);
    for (int i = 0; i < bf.number_hash; i++) {
        bf.arr_hash_seed[i] = (float) rand() / (float) (RAND_MAX);
    }
    return bf;
}

void add_to_blum_filter(struct blum_filter bf, unsigned int value) {
    for (int i = 0; i < bf.number_hash; i++) {
        set_bit(bf.data, hash(value, bf.arr_hash_seed[i], bf.size));
    }
}

int check_to_blum_filter(struct blum_filter bf, unsigned int value) {
    for (int i = 0; i < bf.number_hash; i++) {
        if (get_bit(bf.data, hash(value, bf.arr_hash_seed[i], bf.size)) == 0) {
            return 0;
        }
    }
    return 1;
}


int main(int argc, char *argv[]) {
//    if (argc != 2) {
//        return 42;
//    }
//    FILE *input = fopen(argv[1], "r");
//
//    is_null(input);
//    int number_request;
//    float error_probability;
//    fscanf(input, "%d %f", &number_request, &error_probability);
//    struct blum_filter bf = create_blum_filter(number_request, error_probability);
//    unsigned int ip_adr;
//    while (fscanf(input, "%d", &ip_adr) != EOF) {
//        add_to_blum_filter(bf, ip_adr);
//    }
//    for (unsigned int i = 0; i < number_request; i++) {
//        printf("%d in bitset: %d\n", i * 2, check_to_blum_filter(bf, i * 2));
//    }
//    printf("enter number request, and error_probability\n");

    int number_request = 500;
    float error_probability = (float) 0.1;
    struct blum_filter bf = create_blum_filter(number_request, error_probability);

    for (unsigned int i = 0; i < number_request; i++) {
        add_to_blum_filter(bf, 1 + (i * 2));
    }

    for (unsigned int i = 0; i < number_request; i++) {
        if (check_to_blum_filter(bf, 1 + (i * 2)) == 0) {
            return 52;
        }
    }

    int count_incorrect_error = 0;
    for (unsigned int i = 0; i < number_request; i++) {
        if (check_to_blum_filter(bf, i * 2) == 1) {
            count_incorrect_error++;
        }
    }
//    printf("%f", (float )count_incorrect_error / (float )number_request);
    printf("number_incorrect_error:%d\npersent_errors:%f",
           count_incorrect_error, ((float) count_incorrect_error / (float) number_request));


}