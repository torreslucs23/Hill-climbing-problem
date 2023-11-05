from math import sqrt
from random import shuffle


# calculate the euclidian distance
def calculateDistance(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

#get the coordenates of txt
def getCoordenates(entry):
    xString = entry[0].split(' ')
    yString = entry[1].split(' ')
    coordenates = []
    for i in range(0, len(xString)):
        x = float(xString[i])
        y = float(yString[i])
        coordenates.append((x,y))
    return coordenates


    
#create a matrix of all distances
def generateDistances(positions):
    distances = [[0,0,0] for i in range(len(positions))]

    for i in range(len(positions)):
        print(i)
        for w in range(i,len(positions)):
            distances[i][w] = calculateDistance(positions[i][0], positions[i][1], positions[w][0], positions[w][1])
    return distances

def initialState2(positions):
    return shuffle(positions)

def operator1(positions, id1, id2):
    x = positions[id1]
    positions[id1] = positions[id2]
    positions[id2] = x
    return positions

def operator2(positions, id1, id2):
    new_positions = []
    for i in range(id1):
        new_positions.append(positions[i])
    for i in range(id2, id1-1, -1):
        new_positions.append(positions[i])
    for i in range(id2+1, len(positions)):
        new_positions.append(positions[i])
    
    return new_positions


def calculateCost(sequence):
    cost = 0
    for i in range(len(sequence)):
        if i == len(sequence) -1:
            cost += calculateDistance(sequence[i], sequence[0])
            break
        cost += calculateDistance(sequence[i], sequence[i+1])
    return cost




archive = open('entries.txt', 'r')

coordenates = getCoordenates(archive.readlines())





#variation1: initial state 1 with operator 1 and no random neighbor
def variation1(coordenates):
    aux = []
    cost = 0
    while True:
        flag = False
        cost = calculateCost(coordenates)
        print(cost)
        for i in range(len(coordenates)):
            for w in range(i, len(coordenates)):
                aux = operator1(coordenates, i, w)
                if calculateCost(aux) < cost:
                    coordenates = aux.copy()
                    flag = True
                    cost = calculateCost(coordenates)
                    break
            if flag == True:
                break
        if flag == False:
            break
    return (cost, coordenates)


print(variation1(coordenates))



            


#coordenates 


