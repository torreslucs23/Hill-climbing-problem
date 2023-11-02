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

def operation1(positions, id1, id2):
    x = positions[id1]
    positions[id1] = positions[id2]
    positions[id2] = x
    return positions

def operation2(positions, id1, id2):
    new_positions = []
    for i in range(id1):
        new_positions.append(positions[i])
    for i in range(id2, id1-1, -1):
        new_positions.append(positions[i])
    for i in range(id2+1, len(positions)):
        new_positions.append(positions[i])
    
    return new_positions


print(generateDistances([(0,0), (0,1), (1,0)]))


archive = open('entradas.txt', 'r')

s = archive.readlines()

print(s)