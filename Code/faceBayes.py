import random
import pprint
import math
import time
import statistics


def driver(trainArray, trainLabelArray, testArray, testLabelArray):

    arrayOfSuccess = [[0 for a in range(5)] for b in range(10)]
    #for j in range(5):
    for i in range(10):
        digitsToLookAt = random.sample(range(451),int((((i * 10) + 10) / 100) * 451))
        successRate = trainTest(trainArray, trainLabelArray, testArray, testLabelArray,digitsToLookAt)
        #arrayOfSuccess[i][j] = successRate
        print(successRate)
    #statTesting(arrayOfSuccess)
    """
    time_start = time.time()
    successRate = trainTest(trainArray, trainLabelArray, testArray, testLabelArray, range(451))
    print(successRate)
    time_end = time.time()
    print("Time per training picture: " + str((time_end - time_start) / 451))
    """

def trainTest(trainArray, trainLabelArray, testArray, testLabelArray, digitsToLookAt):
    addedUpFeats, freqOfDigits = featuresAddedUp(trainArray, trainLabelArray, digitsToLookAt)
    chancesItIsDigit = [1 for a in range(2)]
    totCorrect = 0
    tot = 0
    for testing in range(150):
        for i in range(70):
            for j in range(60):
                curFeat = testArray[testing][i][j]
                for pickDigit in range(2):

                    if curFeat == 0:
                        if (1 - addedUpFeats[pickDigit][i][j]) == 0:
                            chancesItIsDigit[pickDigit] = chancesItIsDigit[pickDigit] + (1 - addedUpFeats[pickDigit][i][j])
                        else:
                            chancesItIsDigit[pickDigit] = chancesItIsDigit[pickDigit] + math.log10((1 - addedUpFeats[pickDigit][i][j]))
                    elif curFeat == 1:
                        if (addedUpFeats[pickDigit][i][j]) == 0:
                            chancesItIsDigit[pickDigit] = chancesItIsDigit[pickDigit] + (addedUpFeats[pickDigit][i][j])
                        else:
                            chancesItIsDigit[pickDigit] = chancesItIsDigit[pickDigit] + math.log10((addedUpFeats[pickDigit][i][j]))
        for y in range(2):
            chancesItIsDigit[y] = (chancesItIsDigit[y]) +  math.log10((freqOfDigits[y] / sum(freqOfDigits)))
        #chancesItIsDigit = [float(f)/sum(chancesItIsDigit) for f in chancesItIsDigit]
        maxProb = max(chancesItIsDigit)
        digitPrediction = chancesItIsDigit.index(maxProb)
        #print(digitPrediction)
        if(digitPrediction == testLabelArray[testing]):
            totCorrect+=1
            tot+=1
        else:
            tot+=1
        chancesItIsDigit = [1 for a in range(2)]
    return totCorrect / tot



def featuresAddedUp(trainArray, trainLabelArray, digitsToLookAt):
    freqOfDigits = [0 for m in range(2)]
    addedUpFeats = [[[1 for k in range(60)] for j in range(70)] for i in range(2)]
    for lookAtDigs in digitsToLookAt:
        freqOfDigits[trainLabelArray[lookAtDigs]] = freqOfDigits[trainLabelArray[lookAtDigs]] + 1
        for a in range(70):
            for b in range(60):
                addedUpFeats[trainLabelArray[lookAtDigs]][a][b] = addedUpFeats[trainLabelArray[lookAtDigs]][a][b] + trainArray[lookAtDigs][a][b]
    #print(freqOfDigits)
    for v in range(2):
        if freqOfDigits[v] == 0:
            freqOfDigits[v] = 1
        for l in range(70):
            for u in range(60):
                addedUpFeats[v][l][u] = (addedUpFeats[v][l][u]) /(freqOfDigits[v])
                addedUpFeats[v][l][u]
    return addedUpFeats, freqOfDigits

def statTesting(arrayOfSuccess):
    for i in range(10):
        print(str((i + 1) * 10) + "% of training data: Mean = " + str(statistics.mean(arrayOfSuccess[i])) + " Standard Deviation = " + str(statistics.stdev(arrayOfSuccess[i])))

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)
