import csv
import re
import json


pattern = r'vs\. (.+)'

totalScorigami = 0;
losingTeams = [];
losingTeamsCount = {};

with open('gamesList.csv', newline='') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        for row in csv_reader:
            # Access values of the desired columns using the column names
            getCount = row[6]
            if(getCount == '1'):
                if(totalScorigami == 0):
                    totalScorigami = 1
                else:
                    totalScorigami += 1
                match = re.search(pattern, row[8])
                if match:
                    losingTeams.append(match.group(1).strip())

    for team in losingTeams:
        if team in losingTeamsCount:
            losingTeamsCount[team] += 1
        else:
            losingTeamsCount[team] = 1

    max_pair = max(losingTeamsCount.items(), key=lambda x: x[1])

with open('results.txt', 'w') as file:
    file.write(str(totalScorigami) + '\n')
    json.dump(max_pair, file)
    file.write('\n')
    json.dump(losingTeamsCount, file)
        
