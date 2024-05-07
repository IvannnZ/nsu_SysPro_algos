#include <stdlib.h>
#include "stdio.h"
#include "math.h"
//компилятору нужно добавить флаг -lm

#define big_simple_num 1306717

void is_null(void *ptr) {
    if (ptr == NULL) {
        exit(52);//да здравствует Санкт Питербург, и это город наш
    }
}

struct blum_filter {
    size_t size;
    size_t number_hash;
    unsigned int *arr_hash_seed;
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

unsigned int hash(unsigned int value, unsigned int seed) {
    return (unsigned int) ((value * seed) % big_simple_num);
}

struct blum_filter create_blum_filter(size_t number_request, float error_probability) {
    struct blum_filter bf;
    size_t bit_for_elem = (size_t) (-log2f(error_probability) / log(2));
    bf.size = bit_for_elem * number_request;
    bf.data = (unsigned int *) malloc(
            sizeof(unsigned int) * (size_t) ceilf(ceilf((float) bf.size / 8) / (float) sizeof(unsigned int)));
    is_null(bf.data);
    bf.number_hash = (size_t) (log(2) * (float) bit_for_elem);
    bf.arr_hash_seed = (unsigned int *) malloc(sizeof(unsigned int) * bf.number_hash);
    is_null(bf.arr_hash_seed);
    for (int i = 0; i < bf.number_hash; i++) {
        bf.arr_hash_seed[i] = rand();
    }
    return bf;
}

void add_to_blum_filter(struct blum_filter bf, unsigned int value) {
    for (int i = 0; i < bf.number_hash; i++) {
        set_bit(bf.data, hash(value, bf.arr_hash_seed[i]) % bf.size);
    }
}

int check_to_blum_filter(struct blum_filter bf, unsigned int value) {
    for (int i = 0; i < bf.number_hash; i++) {
        if (get_bit(bf.data, hash(value, bf.arr_hash_seed[i]) % bf.size) == 0) {
            return 0;
        }
    }
    return 1;
}


int main(int argc, char *argv[]) {
    if (argc != 3) {
        return 42;
    }
    printf("ABOBA\n");//thisout this this code didn`t work
    FILE *input = fopen(argv[1], "r");
    is_null(input);
    size_t number_request;
    float error_probability;
    fscanf(input, "%zd %f", &number_request, &error_probability);
    struct blum_filter bf = create_blum_filter(number_request, error_probability);
    unsigned int ip_adr;
    while (fscanf(input, "%d", &ip_adr) != EOF) {
        add_to_blum_filter(bf, ip_adr);
    }
    for (unsigned int i = 0; i < number_request; i++) {
        printf("%d in bitset: %d\n", i * 2, check_to_blum_filter(bf, i * 2));
    }
}