import csv
import sys

winner = 0
candidate_votes = 0 
candidate_votes_percent = 0
vote_count = 0

Khan_count = 0
Li_count = 0
Tooley_count = 0 
Correy_count = 0

with open('Resources/PyPoll_Resource.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers = (next(csv_reader))
    for row in csv_reader:
        vote_count += 1
        candidate_name = row[2]
        if candidate_name == "Khan":
            Khan_count += 1
        elif candidate_name =="Li":
            Li_count += 1
        elif candidate_name == "O'Tooley":
            Tooley_count += 1
        else:
            Correy_count += 1

Khan_percent = "{:.2%}".format(Khan_count/vote_count)
Li_percent = "{:.2%}".format(Li_count/vote_count)
Tooley_percent = "{:.2%}".format(Tooley_count/vote_count)
Correy_percent = "{:.2%}".format(Correy_count/vote_count)
winner = max(Khan_count,Li_count,Tooley_count,Correy_count)

sys.stdout = open("pypoll_results.txt", "w")
print("Election Results")
print("----------------------")
print("Total Votes: ", vote_count)
print("----------------------")
print("Correy: ", Correy_percent, "(",Correy_count,")")
print("Khan:", Khan_percent, "(", Khan_count, ")")
print("Li:", Li_percent, "(",Li_count,")")
print("O'Tooley:", Tooley_percent, "(",Tooley_count,")")
print("----------------------")
print("Winner: ", "Khan")

sys.stdout.close()

