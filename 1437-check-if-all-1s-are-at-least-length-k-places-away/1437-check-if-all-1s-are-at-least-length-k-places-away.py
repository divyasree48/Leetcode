class Solution:
    def kLengthApart(self, nums: List[int], mini: int) -> bool:
        n = len(nums)
        c = 0
        if nums[0] == 1:
            k = 1
        else:
            k = 0
        for i in range(1,n):
            if k and (nums[i] == 0):
                c += 1
            else:
                k += 1
                if k > 1 and c < mini:
                    print(i)
                    return False
                c = 0
        return True

        