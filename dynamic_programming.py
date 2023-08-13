import numpy as np

class DP():
    def __init__(self) -> None:
        pass

    """ problem: 
        finding the summation of 1 to n. 

        Objective function: 
        f(num) is the function which returns summation from 1 to num 

        Recurrence relation: 
        f(num) = num + f(num-1)
    """
    def sum(self, num):
        if num < 1:
            raise ValueError('The input should be a positive integer!')
        buffer = [0]*(num + 1)
        for index in range(1, num+1):
            buffer[index] = buffer[index-1] + index
        
        return buffer[-1]
    

    """
    Problem:
    The Climbing Stairs problem is a classic dynamic programming problem
    that involves finding the number of distinct ways to climb a staircase
    of n steps, taking 1 or 2 steps at a time.

    Objective function:
    f(num_stairs) is the function which returns total number of ways.

    Base cases:
    f(1) = 1 -> 1
    f(2) = 2 -> 1+1, 2

    Recurrence relation:
    f(n) = f(n-1) + f(n-2)
    """

    def climb_stairs(self, num):
        if num < 1:
            raise ValueError('The input should be a positive integer!')
        buffer = [1]*num
        buffer[1] = 2
        for i in range(2, num):
            buffer[i] = buffer[i-1] + buffer[i-2]
        return buffer[-1]
    


    """
    Problem:
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint
    stopping you from robbing each of them is that adjacent houses have
    security systems connected and it will automatically contact the police
    if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police.

    Objective function:
    f(nums) is the function which returns max value of stolen money.

    Base cases:
    f(1) = nums[0]
    f(2) = max(nums[0], nums[1])

    Recurrence relation:
    f(n) = max(f(n-1), f(n-2) + nums[n])
    """
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        buffer = [0] * len(nums)
        buffer[0] = nums[0]
        buffer[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            buffer[i] = max(buffer[i-1], buffer[i-2] + nums[i])
        
        return buffer[-1]


    """
    Problem:
    The alternating sum of a 0-indexed array is defined as the sum of the elements
    at even indices minus the sum of the elements at odd indices.
    For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
    Given an array nums, return the maximum alternating sum of any subsequence of
    nums (after reindexing the elements of the subsequence).
    A subsequence of an array is a new array generated from the original array
    by deleting some elements (possibly none) without changing the remaining elements'
    relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4]
    (the underlined elements), while [2,4,2] is not.

    Dynamic programming logic:
    For each index, we can maintain two arrays: one for the maximum alternating sum
    ending at even indices and another for the maximum alternating sum ending at odd indices.
    even/odd_sum[i-1] is max sub-sequence sums of vecor nums[:i] with even/odd lengths.
    You will find out why we assume these two cases!
    For the last element (n-1), we first calculate even_sum:
    If the last element is not present in any even subsequence, the value is even_sum(n-2)
    If the last element is present in all even subsequence, the value is odd_sum(n-2)+nums[n-1]. This
    is because we have to create all odd subsequences from first n-1 indexes and add the last one to them!
    The final even_sum[n-1] is calculated by max(even_sum[n-2], odd_sum[n-1]+nums[n-1])
    Calculating odd_sum is similar:
`   max(odd_sum[n-2], even_sum[n-1]-nums[n-1])
    """
    def maxAlternatingSum(self, nums):
        n = len(nums)
        even_sum = [0] * n
        odd_sum = [0] * n
        
        even_sum[0] = nums[0]
        odd_sum[0] = 0
        
        for i in range(1, n):
            even_sum[i] = max(even_sum[i - 1], odd_sum[i - 1] + nums[i])
            odd_sum[i] = max(odd_sum[i - 1], even_sum[i - 1] - nums[i])
        
        return max(even_sum[-1], odd_sum[-1])
    

    """
    Given an integer array nums, return true if you can partition the
    array into two subsets such that the sum of the elements in both
    subsets is equal or false otherwise.
    """
    def canPartition(self, nums):

        total_sum = np.sum(nums)
        
        # If the total sum is odd, it is impossible
        # to divide into two equal-sum subsets!
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2

        buffer = [False] * (target_sum + 1)
        # buffer[i] is True when there is a subset in nums with summation of i.
        buffer[0] = True # Null set's sum is zero and is a subset of nums!
        
        for num in nums:
            # j: target_sum -> target_sum-1 -> ... -> num
            for j in range(target_sum, num - 1, -1):
                buffer[j] = buffer[j] or buffer[j - num]
        
        return buffer[-1]
    


    def findWaysToTarget(self, nums, target):
        n = len(nums)
        dp = [[0] * (2 * target + 1) for _ in range(n + 1)]
        dp[0][target] = 1

        # dp[i][j]
        # i: 1 -> 2 -> ... -> n
        for i in range(1, n + 1):
            # j: 1 -> 2 -> ... -> 2*target
            for j in range(2 * target + 1):
                if j + nums[i - 1] <= 2 * target:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]

        return dp[n][target]
    


    """
    Problem:
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    """
    def coinChange(self, coins, amount):
        # dp[i] := fewest # Of coins to make up i
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]
    


    """
    Problem:
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.
    Return the number of combinations that make up that amount. If that amount
    of money cannot be made up by any combination of the coins, return 0.
    You may assume that you have an infinite number of each kind of coin.
    """
    def change(self, amount, coins):
        dp = [1] + [0] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
    



if __name__ == "__main__":
    import os
    os.system("clear")

    dp = DP()

    num = 5
    sum = dp.sum(num=num)
    print('Summation from 1 to {} is: {}'.format(num, sum))

    num = 5
    ways = dp.climb_stairs(num=num)
    print('Number of possible way(s) to climb {} stairs is: {}'.format(num, ways))

    nums = [2, 7, 9, 3, 1]
    max_money = dp.rob(nums)
    print('The maximum stolen money is: {}'.format(max_money))


    nums = [6,2,1,2,4,5]
    print(dp.maxAlternatingSum(nums))

    nums1 = [1, 5, 11, 5]  # Output: True (1+5+5=11 and 11)
    nums2 = [3, 1]   # Output: False

    print(dp.canPartition(nums1))
    print(dp.canPartition(nums2))


    coins = [1, 2, 5]
    amount = 8
    min_num_coins = dp.coinChange(coins, amount)
    print('Fewest number of coins to reach {} is: {}'.format(amount, min_num_coins))
