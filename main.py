from hill_climbing_functions import *
import pandas as pd


#read the entries.txt
archive = open('entries.txt', 'r')

coordenates = getCoordenates(archive.readlines())

#list of variations functions
variations = [variation1, variation2, variation3,
            variation4, variation5, variation6,
            variation7, variation8]

#results of variations
variations_results = [[] for i in range(8)]


#the main loop
for i in range(8):
    for w in range(30):
        variations_results[i].append(variations[i](coordenates))
    variations_results[i].sort()


#this block of code create a pandas dataframe to show the results on the terminal
df = pd.DataFrame(variations_results)

df = df.transpose()

df.columns = ["variation " + str(i) for i in range(1,9)]

print(df)

#this block of code writes the table in a file called table.txt
variations_results = list(map(list, zip(*variations_results)))

with open('table.txt', 'w') as file:
    file.write("Data Table:\n")
    for row in variations_results:
        file.write('\t'.join([str(elem) for elem in row]) + '\n')