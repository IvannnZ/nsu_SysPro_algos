#include "stdio.h"
#include "malloc.h"

#define max(X, Y) (((X) > (Y)) ? (X) : (Y))

void swap(int *a, int *b) {
    int c = *a;
    *a = *b;
    *b = c;
}
void rigt_half_sort(int *arr, size_t len_arr);
void left_half_sort(int *arr, size_t len_arr);

void rigt_half_sort(int *arr, size_t len_arr) {//this func make left half sorted example:[1,4,7,8,6,3,5,2]
    if (len_arr <= 2) {
        return;
    }
}

void left_half_sort(int *arr, size_t len_arr) {//this func make left half sorted example:[1,4,7,8,6,3,5,2]
    if (len_arr <= 2) {
        return;
    }

    if (len_arr<=5){
        if (arr[0] > arr[1]) {
            swap(&arr[0], &arr[1]);
        }
        return;
    }
    size_t midle = len_arr>>1;
    rigt_half_sort(arr+midle, midle);
    rigt_half_sort(arr+midle, midle);

}


void merge_sort(int *arr, int len_arr) {
    if (len_arr == 1) {
        return;
    }
    if (len_arr == 2) {
        if (arr[0] > arr[1]) {
            swap(&arr[0], &arr[1]);
        }
        return;
    }
    int midle = len_arr >> 1;
    while (midle > 1) {

    }
}


int main() {
    int len_arr;
    int *arr;
    printf("Enter len arr:");
    scanf("%d", &len_arr);
    arr = (int *) malloc(len_arr * sizeof(int));
    for (int i = 0; i < len_arr; i++) {
        scanf("%d", arr + i);
    }
    merge_sort(arr, len_arr);
    for (int i = 0; i < len_arr; i++) {
        printf("%d ", arr[i]);
    }
}