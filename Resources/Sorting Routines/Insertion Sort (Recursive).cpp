/*
 * This version of insertion sort uses recursion to repeatedly sort smaller subarrays until
 * reaching an array of 1 element, which is the base case since no sorting is required. Then,
 * the last element is inserted in its correct position in the sorted array, just like the normal
 * insertion sort.
 *
 * The algorithm again runs in O(n²) time, which is not ideal. Similar to its non-recursive
 * counterpart, it is a stable algorithm.
 */

using namespace std;

/**
 * @param arr[]
 *     A pointer to an unsorted array of integers
 * @param len
 *     The length of the array passed in
 */
void insertionSortRecursive(int arr[], int len) {
    if (len == 1)
        return;
    
    // Sort first (n - 1) elements
    insertionSortRecursive(arr, len - 1);
    
    int key = arr[len - 1], j = len - 2;
    
    while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j--;
    }
    
    arr[j + 1] = key;
}
