import csv
import math


def LoadDataTraining(FileTrain):
    trainingSet = []

    with open (fileTrain) as csvfile1:
        lines = csv.reader(csvfile1)

    dataset = list(lines)

    for x in range (7) :
        for y in range (5):
            dataset [x] [y] = int (dataset [x] [y])


        trainingSet.append(dataset[x])

    return trainingSet

def loadDataTest(fileTest):
    testSet = []

    with open(fileTest) as csvfile1:
        lines = csv.reader(csvfile1)

        dataset = list(lines)

        for x in range(53):
            for y in range(5):
                dataset[x][y] = int(dataset[x][y])

                testSet.append(dataset[x])

    return testSet

str h
movspd,mana = int
if (h, movsp >=270):
    print(h,"MARKSMAN")
elif (h, mana >=500):
    print(h,"MAGE")


