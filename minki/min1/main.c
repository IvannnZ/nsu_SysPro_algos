/*
 Сложность алгоритма можно оценить как 0(log2(n)), где n это делимое, пояснения в коде
 Если делитель равен 0, то 0(1)
*/



#include "stdio.h"

struct quotient_remainder {
    unsigned long quotient;
    unsigned long remainder;
};

int len_of_num_in_bin_sys(unsigned long num) {
    int len = 1;
    while (num > 1) {
        num = num >> 1;
        len++;
    }
    return len;
}


int take_a_bit(unsigned long *num, int bit_pos) {// 0(1)
    bit_pos--;
    int answ = ((*num & (unsigned long) ((unsigned long) 1 << bit_pos)) == ((unsigned long) 1 << bit_pos));
    *num -= ((unsigned long) 1 << bit_pos) * answ;
    return answ;
}

struct quotient_remainder division_column(unsigned long divisible, unsigned long divisor) {
    //кусок кода (1) начало
    struct quotient_remainder answer;
    answer.quotient = 0;
    if (divisor == 0) {
        answer.quotient = -1;
        answer.remainder = 0;
        return answer;//или можно развалиться
    }

    int len_divisible = len_of_num_in_bin_sys(divisible);
    unsigned long pivot = 0;
    // кусок кода (1) конец
    //он выполняется всегда, независимо от входных данных, кроме как делитель = 0

    //кусок кода (2) конец
    for (int i = len_divisible; i > 0; i--) {
        pivot = pivot << 1;
        pivot += take_a_bit(&divisible, i);
        answer.quotient = answer.quotient << 1;
        answer.quotient += (pivot >= divisor);
        if (pivot >= divisor) {
            pivot -= divisor;
        }
    }
    //кусок кода (2) конец
    /*
     выполнется за log2(делимое), так как len_divisible примерно равняется log2(делимое), так как равняется длине в двоичной системе счисления
     а всё что внутри выполняется за 0(1)
    */
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
    auto_test();
    return 0;
}

void auto_test() {
    unsigned long divisible = 10;
    unsigned long divisor = 5;
    struct quotient_remainder answer;
    answer = division_column(divisible, divisor);
    if ((answer.quotient * divisor) + answer.remainder == divisible) {
        printf("%lu / %lu is correct\n", divisible, divisor);
    } else {
        printf("%lu / %lu isn`t correct\n", divisible, divisor);
    }
    divisible = 10;
    divisor = 549;
    answer = division_column(divisible, divisor);
    if ((answer.quotient * divisor) + answer.remainder == divisible) {
        printf("%lu / %lu is correct\n", divisible, divisor);
    } else {
        printf("%lu / %lu isn`t correct\n", divisible, divisor);
    }

    divisible = 1188640;
    divisor = 54829;
    answer = division_column(divisible, divisor);
    if ((answer.quotient * divisor) + answer.remainder == divisible) {
        printf("%lu / %lu is correct\n", divisible, divisor);
    } else {
        printf("%lu / %lu isn`t correct\n", divisible, divisor);
    }

    divisible = 123456;
    divisor = 123;
    answer = division_column(divisible, divisor);
    if ((answer.quotient * divisor) + answer.remainder == divisible) {
        printf("%lu / %lu is correct\n", divisible, divisor);
    } else {
        printf("%lu / %lu isn`t correct\n", divisible, divisor);
    }
    divisible = 42;
    divisor = 42;
    answer = division_column(divisible, divisor);
    if ((answer.quotient * divisor) + answer.remainder == divisible) {
        printf("%lu / %lu is correct\n", divisible, divisor);
    } else {
        printf("%lu / %lu isn`t correct\n", divisible, divisor);
    }
}

