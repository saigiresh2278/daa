nums = [2, 3, 2]
if len(nums) == 0:
    print(0)
elif len(nums) == 1:
    print(nums[0])
else:
    def rob_linear(houses):
        prev1, prev2 = 0, 0
        for money in houses:
            temp = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = temp
        return prev1
    max_money = max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
    print(max_money)
