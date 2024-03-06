#include "malloc.h"
#include "stdio.h"
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

int take_ways(int *arr, int len_arr, int serching_elem) {
    if (len_arr <= serching_elem) {
        return -1;//some error code
    }
    if (len_arr == 0) {
        return -1;//some error code
    }
    if (len_arr == 1) {
        return arr[0];
    }
    if (len_arr == 2) {
        if (arr[0] > arr[1]) {
            swap(arr, arr + 1);
        }
        return arr[serching_elem];
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
    if (l >= serching_elem && r <= serching_elem) {
        return arr[l];
    } else {
        if (r < serching_elem) {
            return take_ways(arr + r, len_arr - r, serching_elem-r);
        } else {
            return take_ways(arr, l, serching_elem);
        }
    }
}

int main() {
//    printf("enter len array:");
//    int count_oil_pump;
//    scanf("%d", &count_oil_pump);
//    int *oil_pump = (int *) malloc(sizeof(int) * count_oil_pump);
//    scanArr(oil_pump, count_oil_pump);
//    printf("enter searching place of elem\n");
//    int search;
//    scanf("%d", &search);
//    printf("answer:%d", take_ways(oil_pump, count_oil_pump, search));
    printf("enter count of oil_pump:");
    int count_oil_pump;
    scanf("%d", &count_oil_pump);
    int *oil_pump = (int *) malloc(sizeof(int) * count_oil_pump);
    scanArr(oil_pump, count_oil_pump);
    printf("ideal_place:%d\n", take_ways(oil_pump, count_oil_pump, count_oil_pump>>1));
    return 0;
}