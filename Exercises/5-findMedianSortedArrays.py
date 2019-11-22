# Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n =len(nums1)        
        
        if n%2 ==1:
            m = n/2
            med = nums1[m]
        else:
            m = n/2
            med = 0.5*(nums1[m-1]+nums1[m])
            
        return med
