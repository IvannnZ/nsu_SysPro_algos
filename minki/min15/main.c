#include "stdio.h"
#include "malloc.h"

struct vector {
    int *data;
    size_t len;
    size_t calloc;
};

struct vector add(struct vector arr, int elem) {
    if (arr.calloc == arr.len) {
        arr.calloc *= 2;
        arr.data = (int *) realloc(arr.data, arr.calloc * sizeof(int));
    }
    arr.data[arr.len] = elem;
    arr.len++;
    return arr;
}

struct vector init_vector(size_t len) {
    if (len == 0) len = 1;
    struct vector arr;
    arr.data = (int*)malloc(sizeof(int) * len);
    arr.calloc = len;
    arr.len = 0;
    return arr;
}

struct vector pop(struct vector arr) {//it can't return pop element
    if (arr.len == 0) return arr;
    arr.len--;
    if (arr.len * 4 < arr.calloc) {
        arr.calloc /= 2;
        arr.data = (int *) realloc(arr.data, arr.calloc);
    }
    return arr;
}

void delite(struct vector arr) {
    free(arr.data);
}

void print_vector(struct vector arr) {
    for (size_t i = 0; i < arr.len; i++) {
        printf("%d ", arr.data[i]);
    }
    printf("\n");
}

int main() {
    struct vector arr = init_vector(0);
    printf("enter num or e mean end, d mean dell\n");
    int c;
    while ((c = getchar()) != 'e') {
        int num = 0;
        if (c == 'd') {
            arr = pop(arr);
            c = getchar();
        } else {
            int is_minus = 1;
            if (c == '-') {
                is_minus = -1;
            } else {
                num = c - '0';
            }
            while ((c = getchar()) != '\n') {
                num *= 10;
                num += (c - '0');
            }
            num*=is_minus;
            arr = add(arr, num);
        }
        print_vector(arr);
    }

    delite(arr);
}