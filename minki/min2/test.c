#include "stdio.h"

struct halves_of_num {
    int first_half;
    int second_half;
};


int len_of_num(int num) {
    //первая степень двойки которая больше чем длина числа
    int pivot = 1;
    int len = 1;
    while (num > pivot) {
        pivot = pivot + (pivot << len);
        len = len << 1;
    }
    return len;
}

struct halves_of_num num_separator(int a, int len) {
    struct halves_of_num answ;
    printf("a: %d, len: %d\n", a, len);
    answ.first_half = (a >> (len >> 1));
    printf("first_half: %d\n", answ.first_half);
    answ.second_half = a - (answ.first_half << (len >> 1));
    printf("second_half: %d\n", answ.second_half);
    return answ;
}


int main() {
    //printf("%lu", sizeof (int));
    /*
    int num = 9;
    int pivot = 1;
    int len = 1;
    while (num > pivot){
        pivot = pivot + (pivot << len);
        len = len << 1;
        printf("%d\n", pivot);
    }
    printf("%d", len);
    */
    int num = 9;
    printf("%d, %d\n", num_separator(num, len_of_num(num)).first_half, num_separator(num, len_of_num(num)).second_half);
    return 0;
}