import csv

winner = 0
candidate_votes = 0 
candidate_votes_percent = 0
vote_count = 0 
list = []
with open('../Resources/PyPoll_Resource.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for i in csv_reader:
        vote_count += 1
        candidate_votes = csv_reader.count[2]
        candidate_votes_percent = csv_reader.count([2])/len(csv_reader)
        if candidate[2] not in list:
            list.append(candidate)

with open('../Resources/PyPoll_Resource.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for j in csv_reader:
        if int(j[2])>winner:
            winner = str(j[0])


candidate_count = candidate.count()
print("Election Results")
print(list)
print("Total Votes: ", vote_count)
print(candidate_votes, " : ", candidate_votes_percent)
print("Winner: ", winner)