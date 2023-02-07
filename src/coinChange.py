class MinCoinChange:
    def __init__(self, coins, availability):
        self.coins = coins
        self.availability = availability
        self.n = len(coins)
        self.coin_calc = None
        
    def solve(self, total):
        self.coin_calc = [float('inf')] * (total + 1)
        self.coin_calc[0] = 0

        for i in range(1, total + 1):
            for j in range(self.n):
                if (self.coins[j] <= i and self.availability[j] > 0):
                    if (self.coin_calc[i] > self.coin_calc[i - self.coins[j]] + 1):
                        self.coin_calc[i] = self.coin_calc[i - self.coins[j]] + 1

        if self.coin_calc[total] == float('inf'):
            return -1, []

        combination = []
        i = total
        break_flag = 0
        while (i > 0):
            break_flag += 1
            
            for j in range(self.n - 1, -1, -1):
                if (i >= self.coins[j] and self.availability[j] > 0 and self.coin_calc[i - self.coins[j]] == self.coin_calc[i] - 1):
                    combination.append(self.coins[j])
                    self.availability[j] -= 1
                    i -= self.coins[j]
                    break
            if i > 0 and sum(self.availability) == 0:
                return -1, []
                
        return self.coin_calc[total], combination

# coins = coins = [10, 25, 50, 100, 200, 500]
# availability =  [2, 0, 2, 0, 3, 0]
# total = 1000
# solver = MinCoinChange(coins, availability)
# result = solver.solve(total)
# print("Minimum coins required is", result[0])
# print("Combination is", result[1])
