class Solution:
    def orArray(self, A):
        """
        Problem: OR Array
        
        Given an array A of size n, create a new array by taking bitwise OR of 
        consecutive elements.
        
        Approach: For each index i from 0 to n-2, compute A[i] | A[i+1]
        
        Time Complexity: O(n)
        Space Complexity: O(n) for the output array
        """
        return [A[i] | A[i + 1] for i in range(len(A) - 1)]
