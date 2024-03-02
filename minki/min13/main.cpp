#include <cassert>
#include <functional>
#include <iostream>
#include <chrono>
#include <vector>
#include <map>
#include <string>
#include <cmath>

using std::swap;

void print_array(long arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
void rand_arr(long arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % size;
    }
}
void scan_arr(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cin >> arr[i];
    }
}



/**
Partition using the minimum of the first and last element as pivot.
Returns: a pointer to the final position of the pivot.
*/
long* hoare_partition(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *pivot_pos;
    for (;;) {
        ++first;
        auto f = *first;
        while (f < pivot)
            f = *++first;
        auto l = *last;
        while (pivot < l)
            l = *--last;
        if (first >= last)
            break;
        *first = l;
        *last = f;
        --last;
    }
    --first;
    swap(*first, *pivot_pos);
    return first;
}


/**
Partition using the minimum of the first and last element as pivot.
Returns: a pointer to the final position of the pivot.
*/
long* lomuto_partition(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;
    // Prelude: position first (the write head) on the first element
    // larger than the pivot.
    do {
        ++first;
    } while (*first < pivot);
    assert(first <= last);
    // Main course.
    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        if (x < pivot) {
            *read = *first;
            *first = x;
            ++first;
        }
    }
    // Put the pivot where it belongs.
    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}


long* lomuto_partition_branchfree(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;
    do {
        ++first;
        assert(first <= last);
    } while (*first < pivot);
    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        auto smaller = -int(x < pivot);
        auto delta = smaller & (read - first);
        first[delta] = *first;
        read[-delta] = x;
        first -= smaller;
    }
    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}


void quick_sort(long* first, long* last) {
    if (first >= last) return;

    auto pivot_pos = lomuto_partition(first, last);
    quick_sort(first, pivot_pos - 1);
    quick_sort(pivot_pos + 1, last);
}

int main() {
    int size;
    std::cout << "Enter the size of the array: ";
    std::cin >> size;

    long * myArray = new long[size];
    rand_arr(myArray, size);

    quick_sort(myArray, myArray + size - 1);

    std::cout << "Sorted array: ";
    for (int i = 0; i < size; i++) {
        std::cout << myArray[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}



/*int main(){
    std::cout<<"enter -1 if you want start 'auto' bench, or len of arr\n";
    int n;
    std::cin>>n;
    int *arr = new int [n];
    if (n == -1){

    }else{}


}*/