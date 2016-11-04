import csv
import json

bikeIDs = open('bikeids.txt', 'r').read()
ignore = 1
with open('data/HealthyRide Rentals 2016 Q3.csv', 'r') as csvfile:

    rentalReader = csv.reader(csvfile)
    output = []
    rawNodes = set()
    rawLinks = []
    stationNameDict = dict()
    useEvery = 50
    counter = 0
    for row in rentalReader:
        counter += 1
        if (counter % useEvery != 0):
            continue
        ignore -= 1;
        if (ignore >= 0):
            continue
        try:
            start = int(row[5])
            startName = row[6]
            end = int(row[7])
            endName = row[8]
            stationNameDict[start] = startName
            stationNameDict[end] = endName
            rawNodes.add(start)
            rawNodes.add(end)
            rawLinks.append((start,end))
        except:
            pass
    nodes = []
    links = []
    rawNodes = list(rawNodes)
    indices = dict()
    for rawNode in rawNodes:
        name = stationNameDict[rawNode]
        group = rawNode
        nodes.append({"name":name, "group": rawNode})
    for i in range(len(rawNodes)):
       stationId = rawNodes[i]
       indices[stationId] = i
    for (startId, endId) in rawLinks:
        source = indices[startId]
        target = indices[endId]
        sourceName = stationNameDict[startId]
        endName = stationNameDict[endId]
        weight = 1
        links.append({"source":sourceName, "target":endName, "weight":weight})
    output = {"nodes": nodes, "links":links}

    with open("graphFile.json","w") as outfile:
        outfile.write(json.dumps(output))

def getStations():
    pass
