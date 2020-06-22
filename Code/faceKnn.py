import random
import pprint
import math
import statistics
import time
from operator import itemgetter

def driver(trainArray, trainLabelArray, testArray, testLabelArray):

    arrayOfSuccess = [[0 for a in range(1)] for b in range(10)]
    #for j in range(1):
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

    successRate = trainTest(trainArray, trainLabelArray, testArray, testLabelArray, range(100))
    print(successRate)
    """


def trainTest(trainArray, trainLabelArray, testArray, testLabelArray,digitsToLookAt):
    tot = 0
    totCorrect = 0
    for i in range(150):
        prediction = euclideanDistStuff(trainArray, trainLabelArray, testArray[i], digitsToLookAt)
        if prediction == testLabelArray[i]:
            tot += 1
            totCorrect += 1
        else:
            tot += 1
    return totCorrect / tot

def euclideanDistStuff(trainArray, trainLabelArray, testArray, digitsToLookAt):
    k = 21
    freqOfDigits = [0 for i in range(2)]
    listOfDist = getEuclideanDistList(trainArray,testArray, trainLabelArray, digitsToLookAt)
    kLargestList = []
    kLargestList = kLargest(listOfDist,k)
    for j in range(len(kLargestList)):
        freqOfDigits[kLargestList[j][1]] += 1
    """
    maxDig = max(freqOfDigits)
    prediction = freqOfDigits.index(maxDig)
    """
    if freqOfDigits[1] > 7:
        prediction = 1
    else:
        prediction = 0
    #print(prediction)
    return prediction


def getEuclideanDistList(trainArray, testArray, trainLabelArray, digitsToLookAt):
    listOfDist = [[0 for k in range(2)] for p in range(len(digitsToLookAt))]
    for h in range(len(digitsToLookAt)):
        listOfDist[h][1] = trainLabelArray[digitsToLookAt[h]]
        for i in range(70):
            for j in range(60):
                listOfDist[h][0] = listOfDist[h][0] + math.pow((trainArray[digitsToLookAt[h]][i][j] - testArray[i][j]),2)
        listOfDist[h][0] = math.sqrt(listOfDist[h][0])
    return listOfDist

def kLargest(listOfDist,k):
    kLargestList = sorted(listOfDist, key=itemgetter(0), reverse=False)
    return kLargestList[:k]

def statTesting(arrayOfSuccess):
    for i in range(10):
        print(str((i + 1) * 10) + "% of training data: Mean = " + str(statistics.mean(arrayOfSuccess[i])) + " Standard Deviation = 0.0")
