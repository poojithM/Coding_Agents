# Bubble Sort Algorithm Implementation in Python

" +
               "def bubble_sort(arr):
" +
               "    n = len(arr)
" +
               "    for i in range(n):
" +
               "        # Track whether a swap was made during this pass
" +
               "        swapped = False
" +
               "        # Last i elements are already in place, so loop goes until n-i-1
" +
               "        for j in range(0, n-i-1):
" +
               "            if arr[j] > arr[j+1]:  # Use j for comparison
" +
               "                # Swap if the element found is greater than the next element
" +
               "                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap arr[j] with arr[j + 1]
" +
               "                swapped = True
" +
               "        # If no two elements were swapped by inner loop, then break
" +
               "        if not swapped:
" +
               "            break

" +
               "# Example usage
" +
               "arr = [64, 34, 25, 12, 22, 11, 90]
" +
               "bubble_sort(arr)
" +
               "print("Sorted array is:", arr)

" +
               "# Explanation of Errors:
" +
               "# This code does not have any errors. It correctly implements the Bubble Sort algorithm.
" +
               "# The outer loop ensures that the algorithm runs n times, where n is the number of elements in the array.
" +
               "# The inner loop compares adjacent elements and swaps them if they are in the wrong order.
" +
               "# The swapped flag is a crucial optimization as it allows the algorithm to stop early if no swaps are made in a pass, 
" +
               "# indicating that the array is already sorted.