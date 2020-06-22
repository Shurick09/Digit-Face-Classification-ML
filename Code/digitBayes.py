import random
import pprint
import math
import statistics
import time


def driver(trainArray, trainLabelArray, testArray, testLabelArray):

    arrayOfSuccess = [[0 for a in range(5)] for b in range(10)]
    #for j in range(5):
    for i in range(10):
        digitsToLookAt = random.sample(range(5000),int((((i * 10) + 10) / 100) * 5000))
        successRate = trainTest(trainArray, trainLabelArray, testArray, testLabelArray,digitsToLookAt)
        #arrayOfSuccess[i][j] = successRate
        print(successRate)
    #statTesting(arrayOfSuccess)
    """
    time_start = time.time()
    successRate = trainTest(trainArray, trainLabelArray, testArray, testLabelArray, range(5000))
    print(successRate)
    time_end = time.time()
    print("Time per training picture: " + str((time_end - time_start) / 5000))
    """
def trainTest(trainArray, trainLabelArray, testArray, testLabelArray, digitsToLookAt):
    addedUpFeats, freqOfDigits = featuresAddedUp(trainArray, trainLabelArray, digitsToLookAt)
    chancesItIsDigit = [1 for a in range(10)]
    totCorrect = 0
    tot = 0
    for testing in range(1000):
        for i in range(28):
            for j in range(28):
                curFeat = testArray[testing][i][j]
                for pickDigit in range(10):
                    if curFeat == 0:
                        chancesItIsDigit[pickDigit] = chancesItIsDigit[pickDigit] * ((1 - addedUpFeats[pickDigit][i][j]))
                    elif curFeat == 1:
                        chancesItIsDigit[pickDigit] = chancesItIsDigit[pickDigit] * ((addedUpFeats[pickDigit][i][j]))
        for y in range(10):
            chancesItIsDigit[y] = (chancesItIsDigit[y]) * ((freqOfDigits[y] / sum(freqOfDigits)))
        #chancesItIsDigit = [float(f)/sum(chancesItIsDigit) for f in chancesItIsDigit]
        maxProb = max(chancesItIsDigit)
        digitPrediction = chancesItIsDigit.index(maxProb)
        #print(digitPrediction)
        if(digitPrediction == testLabelArray[testing]):
            totCorrect+=1
            tot+=1
        else:
            tot+=1
        chancesItIsDigit = [1 for a in range(10)]
    return totCorrect / tot



def featuresAddedUp(trainArray, trainLabelArray, digitsToLookAt):
    freqOfDigits = [0 for m in range(10)]
    addedUpFeats = [[[1 for k in range(28)] for j in range(28)] for i in range(10)]
    for lookAtDigs in digitsToLookAt:
        freqOfDigits[trainLabelArray[lookAtDigs]] = freqOfDigits[trainLabelArray[lookAtDigs]] + 1
        for a in range(28):
            for b in range(28):
                addedUpFeats[trainLabelArray[lookAtDigs]][a][b] = addedUpFeats[trainLabelArray[lookAtDigs]][a][b] + trainArray[lookAtDigs][a][b]
    #pprint.pprint(addedUpFeats[4])
    for v in range(10):
        if freqOfDigits[v] == 0:
            freqOfDigits[v] = 1
        for l in range(28):
            for u in range(28):
                addedUpFeats[v][l][u] = addedUpFeats[v][l][u] / freqOfDigits[v]

    return addedUpFeats, freqOfDigits

def statTesting(arrayOfSuccess):
    for i in range(10):
        print(str((i + 1) * 10) + "% of training data: Mean = " + str(statistics.mean(arrayOfSuccess[i])) + " Standard Deviation = " + str(statistics.stdev(arrayOfSuccess[i])))

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)
