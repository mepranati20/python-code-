 # Given a sequence numbers print the median of the sequence. 
# Note: your solution should work if the sequence is a list or tuple.


def find_median(numbers):
    nums = sorted(numbers)      
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


