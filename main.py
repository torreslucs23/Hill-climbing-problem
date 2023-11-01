from math import sqrt

def calculateDistance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def getCoordenates(entry):
    xString = entry.split(' ')
    xCoordenates = []
    for i in range(0, len(i)-1):
        xCoordenates.append(float(i))
    

def generateDistances(xPositions, yPositions):
    distances = [[0,0,0] for i in range(len(xPositions))]

    for i in range(len(xPositions)):
        print(i)
        for w in range(i,len(xPositions)):
            distances[i][w] = calculateDistance(xPositions[i], yPositions[i], xPositions[w], yPositions[w])
    return distances


x=[0,0,1]
y=[0,0,1]

print(generateDistances(x,y))

arquivo = open('entradas.txt', 'r')

s = arquivo.readlines()

print(s)