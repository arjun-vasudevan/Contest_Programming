/*
 * Insertion sort is a simple sorting algorithm that builds the final sorted array one
 * element at a time. It proceeds by taking one input element at a time, and growing a
 * sorted output list. At each step of its iteration, it finds the location the element
 * belongs to in the sorted list and places it there, repeating until no elements remain.
 *
 * It has average and worst case time complexity of O(n²) and best case time complexity
 * of O(n), which is not suitable for large data sets. However, it is an adaptive algorithm,
 * meaning it is efficient for data sets that are already substantially sorted; the time
 * complexity is O(nk) when each element in the input is at most k places away from its sorted
 * position. It is a stable algorithm, as well as an online algorithm, meaning it can process
 * in the order the input is fed into it, without needing the entire input from the start.
 */

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
    for (int i = 1; i < len; i++) {
        int key = arr[i], j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = key;
    }
    
    return arr;
}
