# Importing the necessary Libraries
import os
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import poisson

# Loading the Team Strength DataFrame 

base_dir = Path.cwd()
while base_dir.name != "World Cup Predictor":
    base_dir = base_dir.parent
ts_path = base_dir/"data"/"processed"/"team_strength.csv"
ts_df = pd.read_csv(ts_path)

# Dixon-Coles Correction Function

def dixon_coles_correction(home_goals, away_goals, lambda_home, lambda_away, rho=-0.1):
    if home_goals == 0 and away_goals == 0:
        tau = 1 - lambda_home*lambda_away*rho
    elif home_goals == 1 and away_goals == 0:
        tau = 1 + lambda_away*rho
    elif home_goals == 0 and away_goals == 1:
        tau = 1 + lambda_home*rho
    elif home_goals == 1 and away_goals == 1:
        tau = 1 - rho
    else:
        tau = 1

    return tau


# The main function that will be predicting the match outcomes

def predict_outcome(home_team: str, away_team: str):
    '''
    ts_df.at[row, column] is just pandas for "give me the value at this specific row and column", like looking up a cell in a table.
    So:
      - team_strength_df.at['Brazil', 'goals_for'] → average goals Brazil scores
      - team_strength_df.at['France', 'goals_against'] → average goals France concedes

    When you multiply them:
      - High attack × High defense conceded = high lambda (expect lots of goals)
      - Low attack × Low defense conceded = low lambda (expect few goals)
    
    In the function, home_team and away_team are the row names, and 'goals_for'/'goals_against' are the column names.
    '''
    lambda_home = ts_df.at[home_team, 'goals_for'] * ts_df.at[away_team, 'goals_against']
    lambda_away = ts_df.at[away_team, 'goals_for'] * ts_df.at[home_team, 'goals_against']

    # Double looping over all scorelines from 0-10
    prob_home, prob_away, prob_draw = 0,0,0
    for i in range(11):
        for j in range(11):
            base_probability = poisson.pmf(i, lambda_home) * poisson.pmf(j, lambda_away)
            dc_correction = dixon_coles_correction(i, j, lambda_home, lambda_away)
            corrected_probability = base_probability*dc_correction
            if i>j:
                prob_home += corrected_probability
            elif j>i:
                prob_away += corrected_probability
            else:
                prob_draw += corrected_probability

    return (prob_home, prob_away, prob_draw)


prob_home, prob_away, prob_draw = predict_outcome('Brazil','France')
prob_sum = prob_home+prob_away+prob_draw
print(prob_sum)