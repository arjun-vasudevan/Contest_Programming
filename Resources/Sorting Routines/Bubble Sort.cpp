/*
 * Bubble sort is a naive sorting algorithm involving repeated iterations of an array, comparing
 * every adjacent pair of elements, and swappping them if they are in the wrong order.
 *
 * Bubble sort has an average and worst case time complexity of O(n²), and hence, not optimal
 * for large data sets.
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
int* bubbleSort(int arr[], int len) {
    bool flag = true;
    int n = len;
    
    for (int i = 0; i < len - 1 && flag; i++) {
        flag = false;
        int newn = 0;
        
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                flag = true;
                newn = j + 1;
            }
        }
        
        n = newn;
    }
    
    return arr;
}
