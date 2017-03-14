import csv
import re

def soccer():
    #read the CSV file and close it
    players = open("soccer_players.csv")
    players_csv = csv.reader(players)

    #declare variables
    players_yes = []
    players_no = []
    sharks = ["Sharks"]
    dragons = ["Dragons"]
    raptors = ["Raptors"]

    #split players into 2 groups: experienced and novice
    for player in players_csv:
        if player[2] == 'YES':
            del player[1]
            players_yes.append(', '.join(player))
        else:
            del player[1]
            players_no.append(', '.join(player))

    #evenly divide players from the 2 groups into 3 teams
    for i in range(0,3):
        sharks.append(players_yes.pop())
        sharks.append(players_no.pop())
        dragons.append(players_yes.pop())
        dragons.append(players_no.pop())
        raptors.append(players_yes.pop())
        raptors.append(players_no.pop())

    #write the individual letters
    teams = [sharks, raptors, dragons]
    for team in teams:
        for player in range(1,7):
            m = re.search(r'\w+',team[player])
            n = re.search(r'\s\w+',team[player])
            o = re.search(r'[^,]*$',team[player])
            names1 = m.group() + n.group()
            names = (m.group() + "_" + n.group()[1:]).lower()
            file_name = names + ".txt"
            text_file1 = open(file_name,'w')
            text_file1.write("Dear")
            text_file1.write(o.group())
            text_file1.write("\n")
            text_file1.write("\n")
            text_file1.write("We are happy to inform you that ")
            text_file1.write(names1)
            text_file1.write(" has been assigned to following team: ")
            text_file1.write(team[0])
            text_file1.write("\n")
            text_file1.write("\n")
            text_file1.write("First practice will be on the 20th of March at 19:00")

    #write the teams.txt file
    text_file = open('teams.txt','a')
    text_file.writelines("\n".join(sharks))
    text_file.write("\n")
    text_file.write("\n")
    text_file.write("\n")
    text_file.writelines("\n".join(dragons))
    text_file.write("\n")
    text_file.write("\n")
    text_file.write("\n")
    text_file.writelines("\n".join(raptors))

    players.close()

if __name__ == "__main__":
    soccer()