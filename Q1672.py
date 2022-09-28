# Richest customer wealth

class Solution:
    def maximumWealth_1(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):  # DO NOT write len(...) withour range
            wealth_of_ith_customer = sum(accounts[i])
            if wealth_of_ith_customer > max_wealth:
                max_wealth = wealth_of_ith_customer
        return max_wealth

    # Using max()
    def maximumWealth_2(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            wealth_of_ith_customer = sum(accounts[i])
            max_wealth = max(wealth_of_ith_customer, max_wealth)  # Replace the if statement
        return max_wealth

    # Using map()
    # map(function, iterable)
    # function:	Required. The function to execute for each item
    # iterable:	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.
    def maximumWealth_3(self, accounts):
        return max(map(sum, accounts))
