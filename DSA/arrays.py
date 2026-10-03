# finding the length of an array but not using the len() function
def get_length(arr):
    count = 0
    for i in arr:
        count += 1
    return count

# finding the second largest element in the array
def second_largest(arr):
    if len(arr) < 2:
        return None # no need to do anything if array has not enough elements
    else:
        return sorted(list(set(arr)), reverse=False)[-2] # using set to remove duplicates, sorting array in ascending order and then returning 2nd last elenetn
    




'''''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
Got from Leetcode obv
'''''
# we're using the 2 pointer approach
def sortedSquares(nums):
    left, right = 0, len(nums)-1  # initialising the 2 pointes, both at each extremities
    result = [0]*len(nums) # initialising the result array with 0s, which is of the same lenght 
    write_index = len(nums)-1 # intialising the write index, which is the index whrer we will write the largest square value
    while left <= right: # keep in mind to use <= because we want to include the case when left == right, which happened to me ＞︿＜
        a,b = (nums[left]**2), (nums[right]**2)
        if a > b:
            result[write_index] = a # adding largest square value
            left += 1 # since left side won, it is moving , have to make sure not to move both pointers at the same time
        else:
            result[write_index] = b
            right -= 1
        write_index -= 1 # write_index is moving downwards so that we can have a non-decreasing order of the result array
    return result
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))

# waaaay easier method, without using 2 pointers(saw on leetcode by some dude)
def sortedSquares(nums):
    a = [n**2 for n in nums] # squaring each element in the array and then putting it in a new awway
    a.sort() # sorting the new array
    return a
""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 """
def containsDuplicate(nums):
    return len(nums) != len(set(nums)) #if the length of the array is not equal to the length of the set of the array then it obv means it contains duplicates
# in leetcode, I also added if function, but this is faster and more efficient


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
def productExceptSelf(nums):
    answer = [1] * len(nums) #initialising the answet array with 1s and same lenght as nums array
    prefix, suffix = 1,1 #initialising the 2 variables as 1, this will be useful to calculate the prefix and suffix profuct instead of using them as arrays and then multiplying, we're going to go through the nums array twice(left to right and righr to left) and then multiplying the prefix and suffix product to get the final answer

    for i in range(len(nums)):
        answer[i] *= prefix # multiplying the prefix product to the answer array
        prefix *= nums[i] # updating the prefix

    for i in range(len(nums)
                   -1, # this means start from the last index of the array
                   -1, # stop before the first index of the array, which is 0, so we use -1
                   -1 # move backwards by 1
                   ): # range has 3 parameters, start, stop and step 
        answer[i] *= suffix # multiplying the suffix product to the answer array
        suffix *= nums[i] # updating the suffix
    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums)) # [24,12,8,6]