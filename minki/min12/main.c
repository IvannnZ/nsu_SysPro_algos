#include "stdio.h"
#include "malloc.h"
#include "stdlib.h"

void swap(int *a, int *b) {
    printf("swap:%d, %d\n", *a,*b);
    int c = *a;
    *a = *b;
    *b = c;
    printf("%d, %d\n", *a,*b);
}

void scanArr(int *a, size_t al) {
    for (size_t i = 0; i < al; i++) {
        scanf("%d", &(a[i]));
    }
}

void printArr(int *a, size_t al) {
    for (size_t i = 0; i < al; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}


void quick_sort(int *arr, size_t len_arr) {
    printf("start\n");
    printArr(arr, len_arr);
    if (len_arr == 1 || len_arr == 0) {
        return;
    }
    if (len_arr == 2) {
        if (arr[0] > arr[1]) {
            swap(&arr[0], &arr[1]);
        }
        return;
    }
    size_t rand_num = rand() % len_arr;
    swap(&arr[rand_num], &arr[0]);
    printf("rand:%zu, arr:", rand_num);
    printArr(arr,len_arr);
    int i = 1, j = 1;
    while (j < len_arr) {
        printArr(arr, len_arr);
        if (arr[j] < arr[0]) {
            swap(&arr[j], &arr[i]);
            i++;
        }
        j++;
    }
    swap(&arr[i-1], &arr[0]);
    printf("i:%d len_arr:%d\n", i, len_arr);
    quick_sort(arr + i, len_arr - i);
    quick_sort(arr, i-1);
    return;
}

int main() {
    printf("enter len array:");
    size_t len_arr;
    scanf("%zd", &len_arr);
    int *arr = (int *) malloc(sizeof(int) * len_arr);
    scanArr(arr, len_arr);

    quick_sort(arr, len_arr);

    printArr(arr, len_arr);

    return 0;
}