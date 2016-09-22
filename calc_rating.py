__author__ = 'pintord'

def calculate_ungraded_player(player_name):
    return 75

games_file='games.txt'
grades = []
games = [game for game in open(games_file) if game[:-1]]

for game in games:
    print game
    opp_grade=game.split()[2]
    #print "*" + opp_grade + "*"
    if opp_grade!="UNG":
        #print "graded"
        if   game.split()[1]=="1":   grades.append(int(opp_grade[:-1])+50)
        elif game.split()[1]=="0.5": grades.append(int(opp_grade[:-1]))
        elif game.split()[1]=="0":   grades.append(int(opp_grade[:-1])-50)
    else:
        #print "ungraded"
        ung_est_rating=calculate_ungraded_player(game.split()[3])
        if   game.split()[1]=="1":   grades.append(int(ung_est_rating)+50)
        elif game.split()[1]=="0.5": grades.append(int(ung_est_rating))
        elif game.split()[1]=="0":   grades.append(int(ung_est_rating)-50)

print "\n\nYour rating is: " + str(sum(grades)/len(grades))