								###Contains Duplicate###

#Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it #should return false if every element is distinct.

                
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) != len(set(nums))):
            return True
        else:
            return False

nums = [1,2,3,3,4,5]
ans = Solution().containsDuplicate(nums)
print ans

#Solution2:

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        if not nums:
            return None
        for i in nums:
            dict[i] = dict.get(i,0) + 1
        for key,val in dict.items():
            if val >=2:
               return True
            else:
                return False					

#Solution3:

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False
