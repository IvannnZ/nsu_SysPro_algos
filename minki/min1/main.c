#include "stdio.h"

struct quotient_remainder {
    unsigned long quotient;
    unsigned long remainder;
};

int len_of_num(unsigned long num) {
    int len = 1;
    while (num > 1) {
        num = num >> 1;
        len++;
    }
    return len;
}


int take_a_bit(unsigned long *num, int bit_pos) {
    bit_pos--;
    int answ = ((*num & (unsigned long) ((unsigned long) 1 << bit_pos)) == ((unsigned long) 1 << bit_pos));
    *num -= ((unsigned long) 1 << bit_pos) * answ;
    return answ;
}

struct quotient_remainder division_column(unsigned long divisible, unsigned long divisor) {
    struct quotient_remainder answer;
    answer.quotient = 0;
    if (divisor == 0) {
        answer.quotient = -1;
        answer.remainder = 0;
        return answer;//или можно развалиться
    }

    int len_divisor = len_of_num(divisor);
    int len_divisible = len_of_num(divisible);
    unsigned long pivot = 0;
    for (int i = 0; i < len_divisor; i++) {
        pivot = pivot << 1;
        pivot += take_a_bit(&divisible, len_divisible - i);
    }
    for (int i = len_divisible - len_divisor; i >= 0; i--) {
        if (divisor <= pivot) {
            pivot -= divisor;
            answer.quotient = answer.quotient << 1;
            answer.quotient += 1;
        } else {
            answer.quotient = answer.quotient << 1;
        }
        pivot = pivot << 1;
        pivot += take_a_bit(&divisible, i);
    }
    answer.remainder = pivot;

    return answer;
}

void auto_test();

int main() {
    unsigned long divisible, divisor;
    printf("Enter divisible:");
    scanf("%lu", &divisible);
    printf("Enter divisor:");
    scanf("%lu", &divisor);
    printf("The answer is: quotient:%lu remainder:%lu\n", division_column(divisible, divisor).quotient,
           division_column(divisible, divisor).remainder);
    return 0;
}

//добавить автотесты