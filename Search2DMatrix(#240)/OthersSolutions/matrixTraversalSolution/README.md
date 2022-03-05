Approach: Search Space Reduction

Intuition

Because the rows and columns of the matrix are sorted (from left-to-right and top-to-bottom, respectively), we can prune \mathcal{O}(m)O(m) or \mathcal{O}(n)O(n) elements when looking at any particular value.

Algorithm

First, we initialize a (row, col)(row,col) pointer to the bottom-left of the matrix.[1] Then, until we find target and return true (or the pointer points to a (row, col)(row,col) that lies outside of the dimensions of the matrix), we do the following: if the currently-pointed-to value is larger than target we can move one row "up". Otherwise, if the currently-pointed-to value is smaller than target, we can move one column "right". It is not too tricky to see why doing this will never prune the correct answer; because the rows are sorted from left-to-right, we know that every value to the right of the current value is larger. Therefore, if the current value is already larger than target, we know that every value to its right will also be too large. A very similar argument can be made for the columns, so this manner of search will always find target in the matrix (if it is present).

Check out some sample runs of the algorithm in the animation below:

