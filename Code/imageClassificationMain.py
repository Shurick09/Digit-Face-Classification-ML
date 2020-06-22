import random
import pprint
import digitBayes
import digitPerceptron
import digitKnn
import faceBayes
import facePerceptron
import faceKnn



def mainDriver(type, ml): #type(0) is digits type(1) is faces ... ml(0) = naive bayes ml(1) = perceptron ml(2) = K nearest neighbors
    trainArray, trainLabelArray, testArray, testLabelArray = readPics(type)
    if type == 0:
        if ml == 0:
            digitBayes.driver(trainArray, trainLabelArray, testArray, testLabelArray)
        elif ml == 1:
            digitPerceptron.driver(trainArray,trainLabelArray, testArray, testLabelArray)
        elif ml == 2:
            digitKnn.driver(trainArray,trainLabelArray, testArray, testLabelArray)
    elif type == 1:
        if ml == 0:
            faceBayes.driver(trainArray, trainLabelArray, testArray, testLabelArray)
        elif ml == 1:
            facePerceptron.driver(trainArray,trainLabelArray, testArray, testLabelArray)
        elif ml == 2:
            faceKnn.driver(trainArray,trainLabelArray, testArray, testLabelArray)

def readPics(typeOfPic):
    #0 is a digit, 1 is a face
    if typeOfPic == 0:
        x = 28 #col
        y = 28 #row
        z = 5000 #totDigits in training data
        z2 = 1000 #totDigits in test data
        trainArray = [[[0 for k in range(x)] for j in range(y)] for i in range(z)]
        trainLabelArray = [0 for some in range(z)]
        testArray = [[[0 for a in range(x)] for b in range(y)] for c in range(z2)]
        testLabelArray = [0 for d in range(z2)]
        with open("trainingimages") as f:
            for totDigits in range(z):
                for yTrain in range(y):
                    for xTrain in range(x):
                        c = f.read(1)
                        if (c == '#' or c == '+'):
                            trainArray[totDigits][yTrain][xTrain] = 1
                    c = f.read(1)
        with open("traininglabels") as f1:
            for totDigits1 in range (z):
                c1 = f1.read(1)
                trainLabelArray[totDigits1] = int(c1)
                c1 = f1.read(1)

        with open("testimages") as f2:
            for totDigits2 in range(z2):
                for yTrain2 in range(y):
                    for xTrain2 in range(x):
                        c2 = f2.read(1)
                        if(c2 == '#' or c2 == '+'):
                            testArray[totDigits2][yTrain2][xTrain2] = 1
                    c2 = f2.read(1)

        with open("testlabels") as f3:
            for totDigits3 in range(z2):
                c3 = f3.read(1)
                testLabelArray[totDigits3] = int(c3)
                c3 = f3.read(1)

        return trainArray, trainLabelArray, testArray, testLabelArray

    elif typeOfPic == 1:
        x = 60
        y = 70
        z = 451
        z2 = 150
        trainArray = [[[0 for k in range(x)] for j in range(y)] for i in range(z)]
        trainLabelArray = [0 for some in range(z)]
        testArray = [[[0 for a in range(x)] for b in range(y)] for c in range(z2)]
        testLabelArray = [0 for d in range(z2)]
        with open("facedatatrain") as f:
            for totDigits in range(z):
                for yTrain in range(y):
                    for xTrain in range(x):
                        c = f.read(1)
                        if (c == '#' or c == '+'):
                            trainArray[totDigits][yTrain][xTrain] = 1
                    c = f.read(1)
        with open("facedatatrainlabels") as f1:
            for totDigits1 in range (z):
                c1 = f1.read(1)
                trainLabelArray[totDigits1] = int(c1)
                c1 = f1.read(1)

        with open("facedatatest") as f2:
            for totDigits2 in range(z2):
                for yTrain2 in range(y):
                    for xTrain2 in range(x):
                        c2 = f2.read(1)
                        if(c2 == '#' or c2 == '+'):
                            testArray[totDigits2][yTrain2][xTrain2] = 1
                    c2 = f2.read(1)

        with open("facedatatestlabels") as f3:
            for totDigits3 in range(z2):
                c3 = f3.read(1)
                testLabelArray[totDigits3] = int(c3)
                c3 = f3.read(1)


        return trainArray, trainLabelArray, testArray, testLabelArray


type = int(input("Do you want to predict digits(0) or faces(1)? "))
ml = int(input("Do you want to use Naive Bayes Classifier(0), Perceptron Classifier(1), or K Nearest Neighbors(2)? "))
mainDriver(type,ml)
