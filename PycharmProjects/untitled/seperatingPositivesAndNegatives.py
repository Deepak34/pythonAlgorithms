__author__ = 'Deepak'
import collections

def GCD(firstNumber, secondNumber):
    primeList = [2,3,5,7,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]
    divisorList = []

    for number in [firstNumber,secondNumber]:
        for prime in primeList:
            if number < prime:
                break
            else:
                if number % prime == 0:
                    divisorList.append(prime)

    divisorCount =  [item for item, count in collections.Counter(divisorList).items() if count > 1]
    finalGCD = 1
    for divisor in divisorCount:
        finalGCD = finalGCD * divisor
    return finalGCD



def LCM(firstNumber,secondNumber):

    return int((firstNumber*secondNumber)/GCD(firstNumber,secondNumber))



def LCMOfNumberList(numberList):
    currentLCM = LCM(numberList[0],numberList[1])
    del numberList[0]
    del numberList[0]

    while len (numberList) != 0:

        currentLCM = LCM(currentLCM,numberList[0])
        del numberList[0]

    return currentLCM