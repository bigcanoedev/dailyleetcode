"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order
"""
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Create an empty dictionary to store the value and index of each element
        hash_map = {}

        #iterate over the list collecting both index and value
        for i, num in enumerate(nums):
                
                #calculate the complement
                complement = target - num

                #if the complement is in the hash map
                if complement in hash_map:
                        
                        #if it is return the dictionary at the complement index as well as the current index
                        return [hash_map[complement], i]
                
                #the hash map at value is equal to the index
                hash_map[num] = i
        #no values
        return []

#test
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))