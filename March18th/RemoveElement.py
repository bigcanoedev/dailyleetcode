"""
Given an integer array nums and an integer val, remove all occurrences of val
 in nums in-place. The order of the elements may be changed. Then return the 
 number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the 
elements which are not equal to val. The remaining elements of nums are not 
important as well as the size of nums. Return k.
"""

def remove_element(nums, val):
    #init pointer
    k = 0

    #loop through the array
    for i in range(len(nums)):

        #if the array at i is not equal to val
        if nums[i] != val:

            #then the array at k is equal to the array at i
            nums[k] = nums[i]

            #increment k
            k += 1

    #return k
    return k


nums = [3, 2, 2, 3]
val = 3
new_length = remove_element(nums, val)
print("New length:", new_length)
print("Modified array:", nums[:new_length])
