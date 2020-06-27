prices = [7, 6, 4, 3, 1]


def besttime(prices):
    if len(prices) == 0:
        return 0
    else:
        maxprofit = []
        minprice = prices[0]
        for i in range(1, len(prices)):
            if(prices[i] < minprice):
                minprice = prices[i]
            if(prices[i-1] < prices[i]):
                maxprofit.append(prices[i]-minprice)
        if len(maxprofit) == 0:
            return 0
        else:
            return max(maxprofit)


mp = besttime(prices)
print(mp)
