num = [1, 3 , 1]

def has_33(nums):
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i].next() == 3:
            return True
        else:
            return False
