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
