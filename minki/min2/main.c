#include "stdio.h"
#include <time.h>

#define max(X, Y) (((X) > (Y)) ? (X) : (Y))

struct halves_of_num {
    unsigned long first_half;
    unsigned long second_half;
};

int counter = 0;

int len_of_num(unsigned long num) {
    //первая степень двойки которая больше чем длина числа
    unsigned long long pivot = 1;
    int len = 1;
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
    if (max_len <= 3) {
        return a * b;
    }
    struct halves_of_num halfs_a = num_separator(a, max_len);
    struct halves_of_num halfs_b = num_separator(b, max_len);
    unsigned long first_step = _multiply(halfs_a.first_half, halfs_b.first_half, max_len >> 1);
    unsigned long second_step = _multiply(halfs_a.second_half, halfs_b.second_half, max_len >> 1);
    unsigned long third_step = _multiply(halfs_a.first_half + halfs_a.second_half,
                                         halfs_b.first_half + halfs_b.second_half, max_len >> 1);
    unsigned long fourth_step = third_step - second_step - first_step;
    return ((first_step << max_len) + second_step + (fourth_step << (max_len >> 1)));
}

unsigned long multiply(unsigned long a, unsigned long b) {
    counter = 0;
    return _multiply(a, b, max(len_of_num(a), len_of_num(b)));
}

unsigned long multiply_column(unsigned long a, unsigned long b) {
    unsigned long answer = 0;
    int c = 0;
    while (b != 0) {
        answer += (a * (b & 1)) << c;
        c++;
        b = b >> 1;
    }
    return answer;
}

void auto_test();

int main() {
//не работает на отрицательных(можно сделать, но не вижу смысла)
    unsigned long a, b;
    printf("Enter -1 for start auto test, or\nEnter first num:");
    scanf("%lu", &a);
    if (a == -1) {
        auto_test();
        return 0;
    }
    printf("Enter second num:");
    scanf("%lu", &b);
    printf("The answer is: %lu\n", multiply(a, b));

    return 0;
}


void auto_test() {
    unsigned long a = 1, b = 1;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }

    a = 50, b = 1;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }
    a = 20, b = 47;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }

    a = 121453, b = 5141849;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }


    a = 123456789, b = 123456789;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }

    a = 545, b = 0;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }
    int i = 1;
    while (i > 0) {
        if (multiply_column(i - 1, i - 1) == multiply(i - 1, i - 1)) {
            printf("%d * %d = %lu is correct\n", i - 1, i - 1, multiply(i - 1, i - 1));
        } else {
            printf("%d * %d = %lu isn`t correct\n", i - 1, i - 1,
                   multiply(i - 1, i - 1));// пишет это потому-что си перемножает в int
        }
        i *= 2;
    }
    a = (1 << (sizeof(int) * 8) - 1) - 1, b = 1;
    if (multiply_column(a, b) == multiply(a, b)) {
        printf("%lu * %lu is correct\n", a, b);
    } else {
        printf("%lu * %lu isn`t correct\n", a, b);
    }
    int num;
    printf("Enter number of operation for bench:");
    scanf("%d", &num);
    struct timespec spec;
    clock_gettime(CLOCK_REALTIME, &spec);
    unsigned long long time_start = spec.tv_nsec;
    for (int i = 0; i < num; i++) {
        a = multiply(i, i);
    }
    clock_gettime(CLOCK_REALTIME, &spec);
    printf("time need to fast alg:%llu nsec\n", spec.tv_nsec - time_start);

    clock_gettime(CLOCK_REALTIME, &spec);
    time_start = spec.tv_nsec;
    for (int i = 0; i < num; i++) {
        a = multiply_column(i, i);
    }
    clock_gettime(CLOCK_REALTIME, &spec);
    printf("time need to slow alg:%llu nsec\n", spec.tv_nsec - time_start);
}
