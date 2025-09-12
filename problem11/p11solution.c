/*
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array 
        [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
        (blue section) the container can contain is 49.

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
*/

int maxArea(int* height, int heightSize){
    register unsigned i = 0;
    register unsigned j = heightSize - 1;
    register unsigned best = 0;
    register unsigned cur_h, candidate;

    while (i < j) {
        cur_h = height[i] < height[j] ? height[i] : height[j];
        candidate = cur_h * (j - i);
        while (i < j && height[i] <= cur_h) {
            ++i;
        }
        while (i < j && height[j] <= cur_h) {
            --j;
        }

        if (candidate > best) {
            best = candidate;
        }
    }

    return best;
}