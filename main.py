from math import sqrt
from random import shuffle

def calculateDistance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def getCoordenates(entry):
    xString = entry[0].split(' ')
    yString = entry[1].split(' ')
    coordenates = []
    for i in range(0, len(xString)):
        x = float(xString[i])
        y = float(yString[i])
        coordenates.append((x,y))
    return coordenates


    

def generateDistances(positions):
    distances = [[0,0,0] for i in range(len(positions))]

    for i in range(len(positions)):
        print(i)
        for w in range(i,len(positions)):
            distances[i][w] = calculateDistance(positions[i][0], positions[i][1], positions[w][0], positions[w][1])
    return distances

def initialState2(positions):
    return shuffle(positions)


print(generateDistances([(0,0), (0,1), (1,0)]))


arquivo = open('entradas.txt', 'r')

s = arquivo.readlines()

print(s)