import pandas as pd
import pprint as pprint
import regex as re
from pathlib import Path

#non corner 3's
# 3pt line is 23.75 ft from the center of the hoop
# y > 7.8

#corner 3's
# 3pt line is 22 from the court Y's axis at all points
# y <= 7.8

# 0 = miss
# 1 = make


#effective field goal (eFG) = FGM + (0.5 * 3PM) / FGA


def shot_calculator(file):

    csv_file = open(file)

    shots_df = pd.read_csv(file)

    shot_dict = {}

    #converts CSV to dictionary
    for idx, row in shots_df.iterrows():
        shot_dict[idx] = {
            "team": shots_df.iloc[idx]["team"],
            "x": shots_df.iloc[idx]["x"],
            "y": shots_df.iloc[idx]["y"],
            "fgmade": shots_df.iloc[idx]["fgmade"]
        }

    overall_shot = {}

    #keeping count for every team
    team_set = set()

    team_shot_counter = 0


    #search for all types of shots for each team
    for k, v in shot_dict.items():

        #if team not in the set, it takes in new info for a new team
        if v["team"] not in team_set:
            team_set.add(v["team"])

            # checking if it is a corner 3
            if abs(v["x"]) >= 22:
                # corner 3
                if abs(v["y"]) <= 7.8:
                    # print(v["x"], " ", v["y"], ": corner 3")
                    overall_shot[v["team"]] = {
                        "overall eFG": 0.0,
                        "overall shots made": 0,
                        "overall shot attempts": 0,
                        "2PT zone percentage": 0.0,
                        "3PT zone percentage": 0.0,
                        "NC3 zone percentage": 0.0,
                        "C3 zone percentage": 0.0,
                        "2PT shots made": 0,
                        "2PT shot attempts": 0,
                        "2PT shot attempt percentage": 0,
                        "2PT eFG": 0,
                        "NC3 shots made": 0,
                        "NC3 shot attempts": 0,
                        "NC3 shot attempt percentage": 0,
                        "NC3 eFG": 0,
                        "C3 shots made": v["fgmade"],
                        "C3 shot attempts": 1,
                        "C3 shot attempt percentage": 0,
                        "C3 eFG": 0,
                    }
                #regular 2 point shot
                else:
                    # print(v["x"], " ", v["y"], ": 2PT")
                    overall_shot[v["team"]] = {
                        "overall eFG": 0.0,
                        "overall shots made": 0,
                        "overall shot attempts": 0,
                        "2PT zone percentage": 0.0,
                        "3PT zone percentage": 0.0,
                        "NC3 zone percentage": 0.0,
                        "C3 zone percentage": 0.0,
                        "2PT shots made": v["fgmade"],
                        "2PT shot attempts": 1,
                        "2PT shot attempt percentage": 0,
                        "2PT eFG": 0,
                        "NC3 shots made": 0,
                        "NC3 shot attempts": 0,
                        "NC3 shot attempt percentage": 0,
                        "NC3 eFG": 0,
                        "C3 shots made": 0,
                        "C3 shot attempts": 0,
                        "C3 shot attempt percentage": 0,
                        "C3 eFG": 0,
                    }
            # checking if it is a non corner 3
            elif abs(v["y"]) >= 23.75:
                # non corner 3
                if abs(v["y"]) > 7.8:
                    # print(v["x"], " ", v["y"], ": not corner 3")
                    overall_shot[v["team"]] = {
                        "overall eFG": 0.0,
                        "overall shots made": 0,
                        "overall shot attempts": 0,
                        "2PT zone percentage": 0.0,
                        "3PT zone percentage": 0.0,
                        "NC3 zone percentage": 0.0,
                        "C3 zone percentage": 0.0,
                        "2PT shots made": 0,
                        "2PT shot attempts": 0,
                        "2PT shot attempt percentage": 0,
                        "2PT eFG": 0,
                        "NC3 shots made": v["fgmade"],
                        "NC3 shot attempts": 1,
                        "NC3 shot attempt percentage": 0,
                        "NC3 eFG": 0,
                        "C3 shots made": 0,
                        "C3 shot attempts": 0,
                        "C3 shot attempt percentage": 0,
                        "C3 eFG": 0,
                    }
                # regular 2 point shot
                else:
                    # print(v["x"], " ", v["y"], ": 2PT")
                    overall_shot[v["team"]] = {
                        "overall eFG": 0.0,
                        "overall shots made": 0,
                        "overall shot attempts": 0,
                        "2PT zone percentage": 0.0,
                        "3PT zone percentage": 0.0,
                        "NC3 zone percentage": 0.0,
                        "C3 zone percentage": 0.0,
                        "2PT shots made": v["fgmade"],
                        "2PT shot attempts": 1,
                        "2PT shot attempt percentage": 0,
                        "2PT eFG": 0,
                        "NC3 shots made": 0,
                        "NC3 shot attempts": 0,
                        "NC3 shot attempt percentage": 0,
                        "NC3 eFG": 0,
                        "C3 shots made": 0,
                        "C3 shot attempts": 0,
                        "C3 shot attempt percentage": 0,
                        "C3 eFG": 0,
                    }
            # regular 2 point shot
            else:
                # print(v["x"], " ", v["y"], ": 2PT")
                overall_shot[v["team"]] = {
                    "overall eFG": 0.0,
                    "overall shots made": 0,
                    "overall shot attempts": 0,
                    "2PT zone percentage": 0.0,
                    "3PT zone percentage": 0.0,
                    "NC3 zone percentage": 0.0,
                    "C3 zone percentage": 0.0,
                    "2PT shots made": v["fgmade"],
                    "2PT shot attempts": 1,
                    "2PT shot attempt percentage": 0,
                    "2PT eFG": 0,
                    "NC3 shots made": 0,
                    "NC3 shot attempts": 0,
                    "NC3 shot attempt percentage": 0,
                    "NC3 eFG": 0,
                    "C3 shots made": 0,
                    "C3 shot attempts": 0,
                    "C3 shot attempt percentage": 0,
                    "C3 eFG": 0,
                }

        else:
            # checking if its a corner 3
            if abs(v["x"]) >= 22:
                if abs(v["y"]) <= 7.8:
                    #checking if shot is not made
                    #otherwise add shot attempt
                    if v["fgmade"] == 0:
                        # print(v["x"], " ", v["y"], ": miss")
                        overall_shot[v["team"]]["C3 shot attempts"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
                        continue
                    else:
                        # print(v["x"], " ", v["y"], ": corner 3")
                        overall_shot[v["team"]]["C3 shots made"] += 1
                        overall_shot[v["team"]]["C3 shot attempts"] += 1
                        overall_shot[v["team"]]["overall shots made"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
                else:
                    #for 2 pointers
                    # checking if shot is not made
                    # otherwise add shot attempt
                    if v["fgmade"] == 0:
                        # print(v["x"], " ", v["y"], ": miss")
                        overall_shot[v["team"]]["2PT shot attempts"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
                    else:
                        # print(v["x"], " ", v["y"], ": 2PT")
                        overall_shot[v["team"]]["2PT shots made"] += 1
                        overall_shot[v["team"]]["2PT shot attempts"] += 1
                        overall_shot[v["team"]]["overall shots made"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
            # checking if its not a corner 3
            elif abs(v["y"]) >= 23.75:
                if v["y"] > 7.8:
                    # checking if shot is not made
                    # otherwise add shot attempt
                    if v["fgmade"] == 0:
                        # print(v["x"], " ", v["y"], ": miss")
                        overall_shot[v["team"]]["NC3 shot attempts"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
                    else:
                        # print(v["x"], " ", v["y"], ": not corner 3")
                        overall_shot[v["team"]]["NC3 shots made"] += 1
                        overall_shot[v["team"]]["NC3 shot attempts"] += 1
                        overall_shot[v["team"]]["overall shots made"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
                else:
                    #for 2 pointers
                    # checking if shot is not made
                    # otherwise add shot attempt
                    if v["fgmade"] == 0:
                        # print(v["x"], " ", v["y"], ": miss")
                        overall_shot[v["team"]]["2PT shot attempts"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
                    else:
                        # print(v["x"], " ", v["y"], ": 2PT")
                        overall_shot[v["team"]]["2PT shots made"] += 1
                        overall_shot[v["team"]]["2PT shot attempts"] += 1
                        overall_shot[v["team"]]["overall shots made"] += 1
                        overall_shot[v["team"]]["overall shot attempts"] += 1
            #regular 2 pointer shot
            else:
                if v["fgmade"] == 0:
                    # print(v["x"], " ", v["y"], ": miss")
                    overall_shot[v["team"]]["2PT shot attempts"] += 1
                    overall_shot[v["team"]]["overall shot attempts"] += 1
                else:
                    # print(v["x"], " ", v["y"], ": 2PT")
                    overall_shot[v["team"]]["2PT shots made"] += 1
                    overall_shot[v["team"]]["2PT shot attempts"] += 1
                    overall_shot[v["team"]]["overall shots made"] += 1
                    overall_shot[v["team"]]["overall shot attempts"] += 1
    # pprint.pprint(overall_shot, depth=4)



    # pprint.pprint(overall_shot, depth=4)
    # print("\n")

    #calculating all the overall_eFG for each team, as well
    #eFG for 2 pointers, C3, and NC3

    for team, teamStats in overall_shot.items():

        #resets for every team

        tempShot = 0
        tempAttempts = 0
        tempPercentage = 0.0
        eFG = 0.0
        total_three_pointers = 0
        total_two_pointers = 0
        overall_attempts = 0
        for key, stat in teamStats.items():
            #checks if the shot calculation has been available
            if tempPercentage > 0:
                overall_shot[team][key] = format(tempPercentage, '.3f')

                #resets for every type of shot
                tempShot = 0
                tempAttempts = 0
                tempPercentage = 0.0

            #adds the eFG for a specific shot
            if re.search("eFG", key) and eFG > 0:
                overall_shot[team][key] = format(eFG, '.3f')

            #takes in the shot makes for the specific shot
            if re.search("\s(shots)\s(made)$", key) and key != "overall shots made":
                tempShot = stat

            #takes in the shot attempts for the specific shot
            if re.search("\s(shot)\s(attempts)$", key) and key != "overall shot attempts":
                tempAttempts = stat

            #if both shot and attempts is available
            #it can be calculated
            if tempShot > 0 and tempAttempts > 0:
                #shot percentage calculation
                tempPercentage = tempShot/tempAttempts

                #takes in the overall_attempts to calculate for the team overall eFG
                overall_attempts += tempAttempts

                #regular 2PT
                if re.search("2PT", key):
                    total_two_pointers += tempShot
                    eFG = tempPercentage
                #for all types of 3 pointers
                else:
                    total_three_pointers += tempShot
                    eFG = tempPercentage * 1.5

        #calculating overall eFG
        overall_eFG = (total_two_pointers + (0.5 * total_three_pointers)) / overall_attempts

        #totaling 2PT zone percentage
        overall_shot[team]["2PT zone percentage"] = format(total_two_pointers/overall_attempts, '.3F')

        #totaling NC3 zone percentage
        overall_shot[team]["NC3 zone percentage"] = format(overall_shot[team]["NC3 shot attempts"]/overall_attempts, '.3F')

        #totaling C3 zone percentage
        overall_shot[team]["C3 zone percentage"] = format(overall_shot[team]["C3 shot attempts"] / overall_attempts, '.3f')

        #totaling 3PT zone percentage
        overall_shot[team]["3PT zone percentage"] = format((overall_shot[team]["NC3 shot attempts"] +
                                                           overall_shot[team]["C3 shot attempts"]) / overall_attempts, '.3f')

        overall_shot[team]["overall eFG"] = format(overall_eFG, '.3f')

    # converts the dictionary back to dataframe to be converted into CSV
    final_shots_df = pd.DataFrame(overall_shot)
    final_shots_df.to_csv(file.split(".")[0] + "_converted.csv")

    pprint.pprint(overall_shot, depth=4)

test = shot_calculator("shots_data.csv")