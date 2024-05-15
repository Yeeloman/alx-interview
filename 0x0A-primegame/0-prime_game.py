#!/usr/bin/python3


def isWinner(x, num):
    mariaTurn = True
    benWins = 0
    mariaWins = 0

    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def makeArr(num):
        return list(range(1, num + 1))

    def removeMult(arr, n):
        arr[:] = [x for x in arr if x % n != 0]

    # how many rounds are there
    for i in range(x):
        thisRoundArr = makeArr(num[i])
        # loops for each round's array
        for thisNum in thisRoundArr:
            if mariaTurn:
                if isPrime(thisNum):
                    # thisRoundArr.remove(thisNum)
                    removeMult(thisRoundArr, thisNum)
                    mariaTurn = False
                else:
                    continue
            else:
                if isPrime(thisNum):
                    # thisRoundArr.remove(thisNum)
                    removeMult(thisRoundArr, thisNum)
                    mariaTurn = True
                else:
                    continue
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
