#!/usr/bin/python3
"""why should i live a meaning less life"""


def isWinner(x, num):
    """no winner is this life only L takers"""
    mariaTurn = True
    benWins = 0
    mariaWins = 0

    if not num:
        return None

    def isPrime(n):
        "obtimous brime"
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def removeMultiples(arr, n):
        """ banished from the heavens"""
        arr[:] = [x for x in arr if x % n != 0]

    # how many rounds are there
    for n in num:
        mariaTurn = True
        round_array = list(range(1, n + 1))

        while round_array:
            prime_found = False
            for num in round_array:
                if isPrime(num):
                    prime_found = True
                    round_array = removeMultiples(round_array, num)
                    mariaTurn = not mariaTurn
                    break  # Move to the next round after finding a prime
            if not prime_found:
                break  # No prime found, the other player wins this round

        if mariaTurn:
            mariaWins += 1
        else:
            benWins += 1

    if benWins == mariaWins:
        return None
    elif benWins > mariaWins:
        return "Ben"
    else:
        return "Maria"
    #
    # for i in range(x):
    #     thisRoundArr = makeArr(num[i])
    #     # loops for each round's array
    #     for thisNum in thisRoundArr:
    #         if mariaTurn:
    #             if isPrime(thisNum):
    #                 # thisRoundArr.remove(thisNum)
    #                 removeMult(thisRoundArr, thisNum)
    #                 mariaTurn = False
    #             else:
    #                 continue
    #         else:
    #             if isPrime(thisNum):
    #                 # thisRoundArr.remove(thisNum)
    #                 removeMult(thisRoundArr, thisNum)
    #                 mariaTurn = True
    #             else:
    #                 continue
    #     if mariaTurn:
    #         mariaWins += 1
    #     else:
    #         benWins += 1
    #
    #     if benWins == mariaWins:
    #         return None
    #     elif benWins > mariaWins:
    #         return "Ben"
    #     else:
    #         return "Maria"
