Approach: Binary Search

Intuition

The fact that the matrix is sorted suggests that there must be some way to use binary search to speed up our algorithm.

Algorithm

First, we ensure that matrix is not null and not empty. Then, if we iterate over the matrix diagonals, we can maintain an invariant that the slice of the row and column beginning at the current (row, col)(row,col) pair is sorted. Therefore, we can always binary search these row and column slices for target. We proceed in a logical fashion, iterating over the diagonals, binary searching the rows and columns until we either run out of diagonals (meaning we can return False) or find target (meaning we can return True). The binarySearch function works just like normal binary search, but is made ugly by the need to search both rows and columns of a two-dimensional array.

The other solution is MUCH better