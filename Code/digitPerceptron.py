import random
import pprint
import time
import statistics

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
    successRate = trainTest(trainArray, trainLabelArray, testArray, testLabelArray, range(3000))
    print(successRate)
    time_end = time.time()
    #print("Time per training picture: " + str((time_end - time_start) / 5000))
    """

def trainTest(trainArray, trainLabelArray, testArray, testLabelArray, digitsToLookAt):
    tot = 0
    totCorrect = 0
    #addedUpFeats = addedUpFeats(trainArray, digitsToLookAt)
    weights = computeWeights(trainArray, trainLabelArray, digitsToLookAt)
    for k in range(1000):
        score = [0 for l in range(10)]
        for f in range(10):
            for i in range(28):
                for j in range(28):
                    score[f] = (weights[f][i][j] * testArray[k][i][j]) + score[f]
        maxScore = max(score)
        digPrediction = score.index(maxScore)
        #print(digPrediction)
        if(digPrediction == testLabelArray[k]):
            tot += 1
            totCorrect += 1
        else:
            tot += 1
    return totCorrect/tot




def computeWeights(trainArray, trainLabelArray, digitsToLookAt):
    c = 0
    sizeOfDigitsToLookAt = len(digitsToLookAt)
    weights = [[[0 for k in range(28)] for j in range(28)] for i in range(10)]
    t_end = time.time() + 10
    while time.time() < t_end:
        score = [0 for l in range(10)]
        for w in range(10):
            for  a in range(28):
                for b in range(28):
                    score[w] = (weights[w][a][b] * trainArray[c][a][b]) + score[w]
        maxScore = max(score)
        digPrediction = score.index(maxScore)
        if(digPrediction != trainLabelArray[c]):
            for ab in range(28):
                for cd in range(28):
                    weights[trainLabelArray[c]][ab][cd] = weights[trainLabelArray[c]][ab][cd] + trainArray[c][ab][cd]
                    weights[digPrediction][ab][cd] = weights[digPrediction][ab][cd] - trainArray[c][ab][cd]
        if c == sizeOfDigitsToLookAt - 1:
            c = 0
        else:
            c += 1

    return weights

def statTesting(arrayOfSuccess):
    for i in range(10):
        print(str((i + 1) * 10) + "% of training data: Mean = " + str(statistics.mean(arrayOfSuccess[i])) + " Standard Deviation = " + str(statistics.stdev(arrayOfSuccess[i])))
