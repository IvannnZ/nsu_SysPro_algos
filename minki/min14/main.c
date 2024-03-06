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
    printf("enter num (without 0. -1), to add at end, or -1 to remove last element, or 0 to end\n");
    struct vector arr = init_vector(0);

    int scan;
    scanf("%d", &scan);
    while (scan != 0) {
        if (scan == -1) {
            arr = pop(arr);
        } else {
            arr = add(arr, scan);
        }
        print_vector(arr);
        scanf("%d", &scan);
    }
    delite(arr);
}