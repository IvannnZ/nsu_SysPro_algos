#include "stdio.h"


#define max(X, Y) (((X) > (Y)) ? (X) : (Y))

struct halves_of_num {
    unsigned long first_half;
    unsigned long second_half;
};

int counter = 0;

int len_of_num(int num) {
    //первая степень двойки которая больше чем длина числа
    unsigned long long pivot = 1;
    unsigned long len = 1;
    while (num > pivot) {
        pivot = pivot + (pivot << len);
        len = len << 1;
    }
    return len;
}

struct halves_of_num num_separator(unsigned long a, unsigned long len) {
    struct halves_of_num answ;
    answ.first_half = (a >> (len >> 1));
    answ.second_half = a - (answ.first_half << (len >> 1));
    return answ;
}


unsigned long _multiply(unsigned long a, unsigned long b, int max_len) {
    //printf("a\n");
    if (max_len <= 3) {
        return a * b;
    }
    struct halves_of_num halfs_a = num_separator(a, max_len);
    struct halves_of_num halfs_b = num_separator(b, max_len);
    unsigned long first_step = _multiply(halfs_a.first_half, halfs_b.first_half, max_len >> 1);
    unsigned long second_step = _multiply(halfs_a.second_half, halfs_b.second_half, max_len >> 1);
    int len_for_third_step =
            max_len >> (1 - ((((halfs_a.first_half + halfs_a.second_half) & (1 << max_len)) == (1 << max_len)) ||
                             (((halfs_b.first_half + halfs_b.second_half) & (1 << max_len)) == (1 << max_len))));
    if (len_for_third_step != max(len_of_num(halfs_a.first_half + halfs_a.second_half), len_of_num(halfs_b.first_half + halfs_b.second_half))){
   //     printf("her`s BUG\n");
    }
    if (max_len == len_for_third_step) {
        counter++;
        if (counter == 100) {
            counter = 0;
            return 0;
        }
        printf("counter:%d len:%d, a:%lu, fa:%lu, sa:%lu, b:%lu, fb:%lu, sb:%lu\n", counter, max_len, a,
               halfs_a.first_half, halfs_a.second_half, b, halfs_b.first_half, halfs_b.second_half);
    }
    len_for_third_step = max_len>>1;
    /*
     что делает строка выше, она смотрит не перескочила ли длина суммы первой половины числа и второй половины числа в следующую 2^n пример
     сумма составных числа 11111111(число в двоичной системе счисления) равняется 1111 + 1111 = 11110, и его длина равняется 5, а если судить в
     2^n тогда длина равна 8, и мы должны его перемножать с учётом этого
     либо же число такой же длины 10000000, и его сумма равняется 1000 + 0000 = 1000, что уже не 8, а 4 и его можно перемножать с длиной 4
    */

    // я не придумал как укоротить это условие, а переменную вынес для того чтобы было проще читать, можно сразу занести по применению

    unsigned long third_step = _multiply(halfs_a.first_half + halfs_a.second_half,
                                         halfs_b.first_half + halfs_b.second_half,
                                         len_for_third_step);
    unsigned long fourth_step = third_step - second_step - first_step;
    return ((first_step << max_len) + second_step + (fourth_step << (max_len >> 1)));
}

unsigned long multiply(unsigned long a, unsigned long b) {
    counter = 0;
    //printf("%d c mlt\n", a * b);
    return _multiply(a, b, max(len_of_num(a), len_of_num(b)));
}

void auto_test();

int main() {
//не работает на отрицательных(можно сделать, но не вижу смысла)
    unsigned long a, b;
    printf("Enter -1 for start auto test, or\nEnter first num:");
    scanf("%ld", &a);
    if (a == -1) {
        auto_test();
        return 0;
    }
    printf("Enter second num:");
    scanf("%ld", &b);
    printf("The answer is: %d\n", multiply(a, b));

    return 0;
}


void auto_test() {
    unsigned long a = 1, b = 1;
    if (a * b == multiply(a, b)) {
        printf("%d * %d is correct\n", a, b);
    } else {
        printf("%d * %d isn`t correct\n", a, b);
    }

    a = 50, b = 1;
    if (a * b == multiply(a, b)) {
        printf("%d * %d is correct\n", a, b);
    } else {
        printf("%d * %d isn`t correct\n", a, b);
    }
    a = 20, b = 47;
    if (a * b == multiply(a, b)) {
        printf("%d * %d is correct\n", a, b);
    } else {
        printf("%d * %d isn`t correct\n", a, b);
    }

    a = 121453, b = 5141849;
    if (a * b == multiply(a, b)) {
        printf("%d * %d is correct\n", a, b);
    } else {
        printf("%d * %d isn`t correct\n", a, b);
    }

    a = 545, b = 0;
    if (a * b == multiply(a, b)) {
        printf("%d * %d is correct\n", a, b);
    } else {
        printf("%d * %d isn`t correct\n", a, b);
    }
    int i = 1;
    while (i > 0) {
        if ((i - 1) * (i - 1) == multiply(i - 1, i - 1)) {
            printf("%d * %d = %lu is correct\n", i - 1, i - 1, multiply(i - 1, i - 1));
        } else {
            printf("%d * %d = %lu isn`t correct\n", i - 1, i - 1,
                   multiply(i - 1, i - 1));// пишет это потому-что с перемножает в int
        }
        i *= 2;
    }
    /*
    a = (1 << (sizeof(int) * 8)-1)-1, b = 1;
    if (a * b == multiply(a, b)) {
        printf("%d * %d is correct\n", a, b);
    } else {
        printf("%d * %d isn`t correct\n", a, b);
    }*/
}
