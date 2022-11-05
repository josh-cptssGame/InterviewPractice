"""Day 2-  Nov 4 2022"""





"""Day 1"""
"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.


Constraints:
* 1 <= prices.length <= 10^5
* 0 <= prices[i] <= 10^4


[9, 5, 10, 2, 9]
[5, 9, 1, 2]


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must
buy before you sell.


Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


bestSoFar = None
loop
"""

def maxProfit(prices):
    bestSoFar = 0
    small = 0

    # for i in range(len(prices)): # Equivalent to: for i range(0, len(prices))
    #     for j in range(i + 1, len(prices)):

    # [5, 12, 2, 4]

    # minPriceSoFar = 
    # maxDiff = 


    # [5, 12, 2, 4, 5, 14]

    minPriceSoFar = None
    maxDiff = 0
    for i in range(len(prices)):
        price = prices[i]

        if i == 0:
            minPriceSoFar = price
        elif price < minPriceSoFar:
            minPriceSoFar = price
        else:
            curDiff = price - minPriceSoFar
            if curDiff > maxDiff:
                maxDiff = curDiff

    return maxDiff

    for price in range(len(prices)):
        small = prices[price]
        for sell in range(price + 1, len(prices)):
            temp = prices[sell] - small
            if (temp > bestSoFar):
                bestSoFar = temp
            
    return bestSoFar


maxProfit([7,1,5,3,6,4]) # 5
maxProfit([7,6,4,3,1]) # 0




"""
stk = []
stk.append('a')
stk.pop()

list: l = []
l.append("foo")

map: m = {}
m["a"] = 1 # { "a": 1 }
print(m["a"]) # Prints 1

for i in range(len(inputString)):
    print(i)
"""

def isValidParenString(inputString):
    s = [] #I want this as a stack
    for i in range(len(inputString)): #(i = 0; i < len(inputSting); i++)
        if inputString[i] == "(":
            s.push("(")
        elif inputString[i] == ")":
            if s:
                s.pop()
            else:
                return False
    if s:
        return False
    else:
        return True



def isValidMultiBracketString(inputString):
    s = [] #I want this as a stack
    # for c in inputString:
    for i in range(len(inputString)): #(i = 0; i < len(inputSting); i++)
        c = inputString[i]

        if c == "(" or c =="[" or c == '{':
            s.push(c)
        elif c == ")" or c == "]" or c == '}':
            nextC = s.peek() 

            if s:
                if nextC == "(" and c == ")":
                    s.pop()
                elif nextC == "[" and c == "]":
                    s.pop()
                elif nextC == "{" and c == "}":
                    s.pop()
                else:
                    return False
            else:
                return False
    if s:
        return False
    else:
        return True





# Valid chars: (, ), [, ], {, }

isValidMultiBracketString("([])") # true
isValidMultiBracketString("([)]") # false
"""

TOP
...
[
(
BOT
"""



isValidParenString("()") # should return true
isValidParenString("((") # should return false
isValidParenString("((()()))") # should return true
isValidParenString(")()(") # should return false
isValidParenString("(()") # should return false
isValidParenString("((((((((((()))))))))))")




"""
Data Structures:
* Stack LIFO
* Set


s = (())

TOP
(
(
BOT_

"""

