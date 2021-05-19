# -*- coding: utf-8 -*-
"""
This file shows how to explore data from statsbomb.
The statsbomb data is in "json" format.
This specific script will teach you:
    1) how to load json library
    2) how load data using json library
    3) how to extract data (of your interest) from the data file
"""

import json

#Load the competition file
with open(".\\data\\statsbomb\\competitions.json") as f:
    competitions = json.load(f)


#Womens World Cup 2019 has competition ID 72
competition_id=72

#Load the list of matches for this competition
with open('.\\data\\statsbomb\\matches\\'+str(competition_id)+'\\30.json') as f:
    matches = json.load(f)
    
#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = home_team_name + ' '  + str(home_score) + ' VS ' + str(away_score) + ' ' + away_team_name
    print(describe_text)


#Now lets find a match we are interested in
home_team_required ="England Women's"
away_team_required ="Sweden Women's"
match_id_required = -999

for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required):
        print("---------------------------------------------------------------")
        match_id_required = match['match_id']


print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))



# EXERCISES
#1, Edit the code above to print out the result list for the Mens World cup 

# find ID for FIFA World Cup  (i.e., Men's World Cup)
req_competition_name = "FIFA World Cup"
competition_id=-999

for competition in competitions:
    if (competition['competition_name'] == req_competition_name):
        competition_id = competition['competition_id']
       
print(f"Competition ID for Men's WC: {competition_id}")

#Load the list of matches for Men's WC competition
with open('.\\data\\statsbomb\\matches\\'+str(competition_id)+'\\3.json') as f:
    matches = json.load(f)        


#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = home_team_name + " [" + str(home_score) + '-' + str(away_score) + "] " +  away_team_name
    print(describe_text)



#2, Edit the code above to find the ID for England vs. Sweden

home_team_required ="England"
away_team_required ="Sweden"
match_id_required = -999

for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required) or(away_team_name==home_team_required) and (home_team_name==away_team_required) :
        match_id_required = match['match_id']

print(home_team_required + ' vs ' + away_team_required + ' has id: ' + str(match_id_required))


#3, Write new code to write out a list of just Sweden's results in the tournament.

#Print all match results
team_name = "Sweden"

for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if home_team_name ==  team_name or away_team_name == team_name: 
        home_score=match['home_score']
        away_score=match['away_score']
        describe_text = home_team_name + " [" + str(home_score) + '-' + str(away_score) + "] " +  away_team_name
        print(describe_text)

