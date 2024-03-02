#include "stdio.h"
#include "malloc.h"
#include "stdlib.h"


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


void swap(int *a, int *b) {
    int c = *a;
    *a = *b;
    *b = c;
}

void quick_sort(int *arr, int len_arr) {
    if (len_arr == 1 || len_arr == 0) {
        return;
    }
    if (len_arr == 2) {
        if (arr[0] > arr[1]) {
            swap(arr, arr + 1);
        }
        return;
    }
    int rand_num = rand() % len_arr;
    int pivot = arr[rand_num];

    if (rand_num != 0) {
        swap(arr + rand_num, arr);
    }

    int l = 0, r = 0;
    for (int i = 1; i < len_arr; i++) {
        if (arr[i] < pivot) {
            int tmp = arr[i];
            arr[i] = arr[r + 1];
            arr[r + 1] = arr[l];
            arr[l] = tmp;
            r++;
            l++;
        } else {
            if (arr[i] == pivot) {
                swap(arr + (r + 1), arr + i);
                r++;
            }
        }
    }
    quick_sort(arr, l);
    quick_sort(arr + r, len_arr - r);
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