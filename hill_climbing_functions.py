from math import sqrt
from random import shuffle
from random import randint


# calculate the euclidian distance
def calculateDistance(p1,p2):
    return round(float(sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)),4)

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

#aplies the operator 1
def operator1(positions, id1, id2):
    x = positions[id1]
    positions[id1] = positions[id2]
    positions[id2] = x
    return positions

#aplies the operator 2
def operator2(positions, id1, id2):
    new_positions = []
    for i in range(id1):
        new_positions.append(positions[i])
    for i in range(id2, id1-1, -1):
        new_positions.append(positions[i])
    for i in range(id2+1, len(positions)):
        new_positions.append(positions[i])
    
    return new_positions


#calculate the cost of a sequence
def calculateCost(sequence):
    cost = 0
    for i in range(len(sequence)):
        if i == len(sequence) -1:
            cost += calculateDistance(sequence[i], sequence[0])
            break
        cost += calculateDistance(sequence[i], sequence[i+1])
    return cost



#variation1: initial state 1 with operator 1 and no random neighbor
def variation1(coordenates):
    coord = coordenates.copy()
    aux = []
    cost = 0
    while True:
        flag = False
        cost = calculateCost(coord)
        print(cost)
        for i in range(len(coord)):
            for w in range(i, len(coord)):
                aux = operator1(coord, i, w)
                if calculateCost(aux) < cost:
                    coord = aux.copy()
                    flag = True
                    cost = calculateCost(coord)
                    break
            if flag == True:
                break
        if flag == False:
            break
    cost = calculateCost(coord)
    print(cost, coord)
    print("")
    return cost


#variation 2: initial state 1 with operator 1 and random neighbor
def variation2(coordenates):
    coord = coordenates.copy()
    aux = []
    cost = 0

    #n_cities just calculate the lenght of coordenates(cities)
    n_cities = len(coord)

    #this is a list of visited indexes for cut repetition on the random states
    visited_indexes = []
    while True:
        cost = calculateCost(coord)
        flag = False
        print(cost)
        while len(visited_indexes) < (n_cities**2 - n_cities)/2:
            x = randint(0, n_cities-1)
            y = randint(0, n_cities-1)
            if sorted((x,y)) in visited_indexes:
                continue

            visited_indexes.append(sorted((x,y)))
            aux = operator1(coord, x, y)
            if calculateCost(aux) < cost:
                coord = aux.copy()
                flag = True
                break
        if flag == False:
            break
    calculateCost(coord)
    print(coord,cost)
    print(" ")
    return cost




#variation 3: initial state 1 with operator 2 and no random neighbor
#notice that this variation is similar to variation 1, but just replacing the operator 2 above operator 1
def variation3(coordenates):
    coord = coordenates.copy()
    aux = []
    cost = 0
    while True:
        flag = False
        cost = calculateCost(coord)
        print(cost)
        for i in range(len(coord)):
            for w in range(i, len(coord)):
                aux = operator2(coord, i, w)
                if calculateCost(aux) < cost:
                    coord = aux.copy()
                    flag = True
                    cost = calculateCost(coord)
                    break
            if flag == True:
                break
        if flag == False:
            break
    cost = calculateCost(coord)
    print(cost, coord)
    print("")
    return cost


#variation 4: initial state 1 with operator 2 and random neighbor
#notice that this variation is similar to variation 2, but just replacing the operator 2 above operator 1
def variation4(coordenates):
    coord = coordenates.copy()
    aux = []
    cost = 0

    #n_cities just calculate the lenght of coordenates(cities)
    n_cities = len(coord)

    #this is a list of visited indexes for cut repetition on the random states
    visited_indexes = []
    while True:
        cost = calculateCost(coord)
        flag = False
        print(cost)
        while len(visited_indexes) < (n_cities**2 - n_cities)/2:
            x = randint(0, n_cities-1)
            y = randint(0, n_cities-1)
            if sorted((x,y)) in visited_indexes:
                continue

            visited_indexes.append(sorted((x,y)))
            aux = operator2(coord, x, y)
            if calculateCost(aux) < cost:
                coord = aux.copy()
                flag = True
                break
        if flag == False:
            break
    cost = calculateCost(coord)
    print(coordenates, cost)
    print(" ")
    return cost

#variation 5: initial state 2 with operator 1 and no random neighbor
def variation5(coordenates):
    shuffle(coordenates)
    return variation1(coordenates)

#variation 6: initial state 2 with operator 1 and random neighbor
def variation6(coordenates):
    shuffle(coordenates)
    return variation2(coordenates)


#variation 7: initial state 2 with operator 2 and no random neighbor
def variation7(coordenates):
    shuffle(coordenates)
    return variation3(coordenates)


#variation 8: initial state 2 with operator 2 and random neighbor
def variation8(coordenates):
    shuffle(coordenates)
    return variation4(coordenates)

