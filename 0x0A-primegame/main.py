#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
isWinnertest = __import__('test').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinnertest(5, [2, 5, 1, 4, 3])))

