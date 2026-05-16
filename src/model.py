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
ts_df = pd.read_csv(ts_path, index_col= 'team')

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

    # Creating 2 numpy arrays and using np.outer() to speed up the process instead of using double loops
    i, j = np.arange(11), np.arange(11)    
    m1 = poisson.pmf(i, lambda_home)
    m2 = poisson.pmf(j, lambda_away)
    # np.outer(a, b) — 11x11 matrix where cell [2,3] = probability of home scoring exactly 2 AND away scoring exactly 3
    matrix = np.outer(m1,m2)

    # Applying the Dixon-Coles correction to specific cells as per the goal values 
    rho = -0.1 # Default value
    matrix[0,0] *= 1 - lambda_home * lambda_away * rho
    matrix[1,0] *= 1 + lambda_away * rho
    matrix[0,1] *= 1 + lambda_home * rho
    matrix[1,1] *= 1 - rho

    # The upper triangle (excluding diagonal) represents Home wins (home goals > away goals)
    # The Lower triangle (excluding diagonal) represents Away wins (home goals < away goals)
    # The Diagonal represents Draws (home goals = away goals)
    prob_home = np.triu(matrix, k=1).sum() # (k=1 means start one above diagonal)
    prob_away = np.tril(matrix, k=-1).sum() # (k=-1 means start one below diagonal)
    prob_draw = np.diag(matrix).sum()
    
    return (prob_home, prob_away, prob_draw)