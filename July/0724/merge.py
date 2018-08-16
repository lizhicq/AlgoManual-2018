class Solution:
    #param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
       C = A + B
       C.sort()
       return C