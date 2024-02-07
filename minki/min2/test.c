#include "stdio.h"

struct halves_of_num {
    int first_half;
    int second_half;
};


int len_of_num(int num) {
    //первая степень двойки которая больше чем длина числа
    unsigned long long pivot = 1;
    unsigned long len= 1;
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

void print_bin(int a) {
    int len_a = len_of_num(a);
    for (int i = 0; i < len_a; i++) {
        printf("%d", a & 1);
        a = a >> 1;
    }
    printf("\n");
}
//void rec(){
//    int a = 5;
//    int b = a<<a;
//    rec();
//}

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
    int num;
    scanf("%d", &num);
    printf("%d\n", len_of_num(num));
    printf("%d, %d\n", num_separator(num, len_of_num(num)).first_half, num_separator(num, len_of_num(num)).second_half);
//    rec();
    int max_len = len_of_num(num);
    struct halves_of_num half = num_separator(num, max_len);
    int len_for_third_step =
            max_len >> (1 - (((half.first_half + half.second_half) & (1<<max_len)) == (1<<max_len) ||
                             ((half.first_half + half.second_half) & (1<<max_len)) == (1<<max_len)));
    printf("num:%d, len:%d third_len:%d ,bin:", num, max_len, len_for_third_step);
    print_bin(num);
    return 0;
}