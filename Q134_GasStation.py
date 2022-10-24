class Solution:
    def canCompleteCircuit_1(self, gas: List[int], cost: List[int]) -> int:  # O(N^2), time limit exceeded
        def check(gas, index, tank):
            for _ in range(len(gas) - 1):
                if index == len(gas) - 1:
                    next_station = 0
                else:
                    next_station = 1 + index
                tank = tank + gas[next_station] - cost[index]
                if tank < cost[next_station]:
                    return -1
                index = next_station
            if index == len(gas) - 1:
                return 0
            else:
                return index + 1

        start = []
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                start.append(i)
        if not start:
            return -1
        else:
            for index in start:
                tank = gas[index]
                if check(gas, index, tank) != -1:
                    return check(gas, index, tank)
            return -1

    def canCompleteCircuit_2(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1  # !!! it is not beneficial to check at indices (i+1,i+2,...,j-1) because if we start at indices (i+1,i+2,...j-1) it will result in less amount of gas in our car at station j which will definitely be a failure.
        return -1 if (total_surplus < 0) else start