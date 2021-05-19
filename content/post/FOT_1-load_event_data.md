---
title: "01: Loading StatsBomb Data "
date: 2021-05-19T02:00:00-00:00
draft: false
tags: ["soccer analytics", "load_data", "statsbomb"]
---

This file shows how to explore data from statsbomb.
The statsbomb data is in "json" format.
This specific script will teach you:
    1) how to load json library
    2) how load data using json library
    3) how to extract data (of your interest) from the data file

## Tutorial


```python
import json

#Load the competition file
with open("G:\\University of South Carolina\\HOW TO\\Static Site\\Hugo\\soccer_analytics\\data\\statsbomb\\competitions.json") as f:
    competitions = json.load(f)


#Womens World Cup 2019 has competition ID 72
competition_id=72

#Load the list of matches for this competition
with open('G:\\University of South Carolina\\HOW TO\\Static Site\\Hugo\\soccer_analytics\\data\\statsbomb\\matches\\'+str(competition_id)+'\\30.json') as f:
    matches = json.load(f)
```


```python
#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = home_team_name + ' ['  + str(home_score) + '-' + str(away_score) + '] ' + away_team_name
    print(describe_text)
```

    Sweden Women's [1-0] Canada Women's
    Cameroon Women's [2-1] New Zealand Women's
    Germany Women's [3-0] Nigeria Women's
    England Women's [1-2] Sweden Women's
    Jamaica Women's [1-4] Australia Women's
    Italy Women's [0-2] Netherlands Women's
    France Women's [2-1] Brazil Women's
    Germany Women's [1-2] Sweden Women's
    England Women's [2-1] Scotland Women's
    Sweden Women's [5-1] Thailand Women's
    Japan Women's [0-2] England Women's
    Korea Republic Women's [1-2] Norway Women's
    United States Women's [3-0] Chile Women's
    Norway Women's [1-1] Australia Women's
    Norway Women's [3-0] Nigeria Women's
    United States Women's [2-0] Netherlands Women's
    China PR Women's [0-0] Spain Women's
    Italy Women's [0-1] Brazil Women's
    France Women's [4-0] Korea Republic Women's
    Germany Women's [1-0] China PR Women's
    Spain Women's [3-1] South Africa Women's
    Australia Women's [1-2] Italy Women's
    Brazil Women's [3-0] Jamaica Women's
    Canada Women's [1-0] Cameroon Women's
    Argentina Women's [0-0] Japan Women's
    France Women's [1-2] United States Women's
    New Zealand Women's [0-1] Netherlands Women's
    United States Women's [13-0] Thailand Women's
    Chile Women's [0-2] Sweden Women's
    Nigeria Women's [2-0] Korea Republic Women's
    France Women's [2-1] Norway Women's
    Germany Women's [1-0] Spain Women's
    South Africa Women's [0-1] China PR Women's
    Australia Women's [3-2] Brazil Women's
    England Women's [1-0] Argentina Women's
    Jamaica Women's [0-5] Italy Women's
    Japan Women's [2-1] Scotland Women's
    Netherlands Women's [3-1] Cameroon Women's
    Canada Women's [2-0] New Zealand Women's
    Nigeria Women's [0-1] France Women's
    South Africa Women's [0-4] Germany Women's
    Scotland Women's [3-3] Argentina Women's
    Thailand Women's [0-2] Chile Women's
    Netherlands Women's [2-1] Canada Women's
    Sweden Women's [0-2] United States Women's
    England Women's [3-0] Cameroon Women's
    Spain Women's [1-2] United States Women's
    Italy Women's [2-0] China PR Women's
    Netherlands Women's [2-1] Japan Women's
    Norway Women's [0-3] England Women's
    England Women's [1-2] United States Women's
    Netherlands Women's [1-0] Sweden Women's
    


```python
#Now lets find a match we are interested in
home_team_required ="England Women's"
away_team_required ="Sweden Women's"
match_id_required = -999

for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required):
        match_id_required = match['match_id']

print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))
```

    England Women's vs Sweden Women's has id:69301
    

## Exercises

1. Edit the code above to print out the result list for the Mens World cup 


```python
# find ID for FIFA World Cup  (i.e., Men's World Cup)
req_competition_name = "FIFA World Cup"
competition_id=-999

for competition in competitions:
    if (competition['competition_name'] == req_competition_name):
        competition_id = competition['competition_id']
       
print(f"Competition ID for Men's WC: {competition_id}")

#Load the list of matches for Men's WC competition
with open('G:\\University of South Carolina\\HOW TO\\Static Site\\Hugo\\soccer_analytics\\data\\statsbomb\\matches\\'+str(competition_id)+'\\3.json') as f:
    matches = json.load(f)        


#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = home_team_name + " [" + str(home_score) + '-' + str(away_score) + "] " +  away_team_name
    print(describe_text)
```

    Competition ID for Men's WC: 43
    Croatia [1-1] Denmark
    Nigeria [2-0] Iceland
    Poland [0-3] Colombia
    Croatia [2-0] Nigeria
    Brazil [2-0] Costa Rica
    Germany [0-1] Mexico
    Australia [0-2] Peru
    Serbia [0-2] Brazil
    Senegal [0-1] Colombia
    Panama [1-2] Tunisia
    Switzerland [2-2] Costa Rica
    France [2-1] Australia
    Uruguay [3-0] Russia
    Brazil [2-0] Mexico
    Russia [2-2] Croatia
    Denmark [1-1] Australia
    Costa Rica [0-1] Serbia
    France [1-0] Peru
    Belgium [3-2] Japan
    Belgium [3-0] Panama
    Argentina [0-3] Croatia
    France [4-3] Argentina
    Brazil [1-2] Belgium
    Uruguay [0-2] France
    France [4-2] Croatia
    Iceland [1-2] Croatia
    Poland [1-2] Senegal
    Denmark [0-0] France
    Egypt [0-1] Uruguay
    Argentina [1-1] Iceland
    Spain [1-1] Russia
    Belgium [5-2] Tunisia
    Peru [0-1] Denmark
    Uruguay [1-0] Saudi Arabia
    South Korea [1-2] Mexico
    Spain [2-2] Morocco
    Brazil [1-1] Switzerland
    Nigeria [1-2] Argentina
    Japan [2-2] Senegal
    Saudi Arabia [2-1] Egypt
    Uruguay [2-1] Portugal
    Japan [0-1] Poland
    Morocco [0-1] Iran
    Iran [0-1] Spain
    Russia [5-0] Saudi Arabia
    Sweden [1-0] South Korea
    Portugal [3-3] Spain
    Portugal [1-0] Morocco
    Mexico [0-3] Sweden
    Iran [1-1] Portugal
    England [6-1] Panama
    England [0-1] Belgium
    Colombia [1-1] England
    Sweden [1-0] Switzerland
    Croatia [2-1] England
    Sweden [0-2] England
    South Korea [2-0] Germany
    Colombia [1-2] Japan
    France [1-0] Belgium
    Belgium [2-0] England
    Russia [3-1] Egypt
    Germany [2-1] Sweden
    Serbia [1-2] Switzerland
    Tunisia [1-2] England
    

2. Edit the code above to find the ID for England vs. Sweden


```python
home_team_required ="England"
away_team_required ="Sweden"
match_id_required = -999

for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required) or(away_team_name==home_team_required) and (home_team_name==away_team_required) :
        match_id_required = match['match_id']

print(home_team_required + ' vs ' + away_team_required + ' has id: ' + str(match_id_required))

```

    England vs Sweden has id: 8651
    

3. Write new code to write out a list of just Sweden's results in the tournament.


```python
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

```

    Sweden [1-0] South Korea
    Mexico [0-3] Sweden
    Sweden [1-0] Switzerland
    Sweden [0-2] England
    Germany [2-1] Sweden
    
