class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## for i,one in enumerate(nums)
        
        for i in  range(0,len(nums),1):
            ##print(nums[i])
            one = target - nums[i]
            ##for j in range(len(nums[i:])):
            for j in range(i+1,len(nums),1):
                ##print(j)
                if one - nums[j]==0:
                   return (i,j)
                ##if one- nums[j]:

if __name__ == '__main__':
    print (Solution().twoSum((2, 7, 11, 15), 9))
    print (Solution().twoSum((3, 2, 4), 6))