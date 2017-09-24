/*
 * Selection sort is a rudimentary sorting algorithm that maintains a sorted and unsorted
 * subarray. The process repeatedly takes the minimum element of the unsorted portion and
 * places it at the end of the sorted portion. It is a not a stable algorithm, meaning it
 * does not maintain the relative order of elements with equal values.
 *
 * It has a O(n²) average/best case/worse case time complexity due to the 2 nested loops,
 * which is inefficient on large lists.
 */

#include <algorithm> // swap
using namespace std;

/**
 * @param arr[]
 *     A pointer to an unsorted array of integers
 * @param len
 *     The length of the array passed in
 * @return
 *     Returns the sorted array of integers
 */
int* insertionSort(int arr[], int len) {
    for (int i = 0; i < len - 1; i++) {
        int minInd = i;
        
        for (int j = i + 1; j < len; j++)
            if (arr[j] < arr[minInd])
                minInd = j;
        
        swap(arr[i], arr[minInd]);
    }
    
    return arr;
}
