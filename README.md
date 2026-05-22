<div align="center">

# 🌍 FIFA World Cup 2026 Prediction System

### ⚽ Monte Carlo Tournament Simulation using Poisson Modeling & Dixon-Coles Correction

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/NumPy-Scientific_Computing-orange?style=for-the-badge&logo=numpy">
<img src="https://img.shields.io/badge/Pandas-Data_Analysis-purple?style=for-the-badge&logo=pandas">
<img src="https://img.shields.io/badge/SciPy-Statistics-green?style=for-the-badge&logo=scipy">
<img src="https://img.shields.io/badge/Football-Analytics-red?style=for-the-badge">

<br>

*A complete football analytics pipeline for predicting FIFA World Cup 2026 outcomes using statistical modeling, Poisson goal modeling, Dixon-Coles correction, and Monte Carlo simulation.*

</div>

---

# 🧠 Overview

Football is inherently unpredictable, low-scoring, and highly probabilistic. Traditional deterministic prediction methods often fail to capture the uncertainty of tournament football.

This project builds a realistic **World Cup prediction framework** using:

* ⚽ Historical international football results
* 🧠 Team strength estimation
* 🏆 Elo ratings
* 🎯 Poisson goal distributions
* 🔧 Dixon-Coles low-score correction
* 🎲 Monte Carlo tournament simulation

The framework predicts match outcomes and simulates the entire FIFA World Cup 2026 tournament structure probabilistically.

---

# 💻 Features

### ✅ Historical Data Processing

* Load and clean international football match data
* Extract competitive and FIFA World Cup fixtures
* Generate processed datasets

### ✅ Team Strength Modeling

* Estimate offensive strength
* Estimate defensive weakness
* Build team strength metrics from historical matches

### ✅ Elo Rating Integration

* Fetch and integrate national team Elo ratings
* Standardize and merge team metadata

### ✅ Poisson Match Prediction

* Compute expected goals
* Generate score probability distributions
* Calculate win/draw/loss probabilities

### ✅ Dixon-Coles Correction

* Improve low-scoring football predictions
* Correct unrealistic Poisson assumptions

### ✅ Monte Carlo Tournament Simulation

* Simulate group stage outcomes
* Simulate knockout brackets
* Predict tournament progression

---

# ⚽ Poisson Goal Modeling

Football scores are modeled using Poisson distributions.

Expected goals are estimated as:

<div align="center">

### λ<sub>home</sub> = Attack<sub>home</sub> × Defense<sub>away</sub>

### λ<sub>away</sub> = Attack<sub>away</sub> × Defense<sub>home</sub>

</div>

These expected goals are then used to generate score probabilities from 0–10 goals.

---

# 🔧 Dixon-Coles Correction

Traditional Poisson models underestimate realistic low-scoring outcomes such as:

* 0-0
* 1-0
* 0-1
* 1-1

This project implements the **Dixon-Coles correction** to improve calibration for defensive and tactical matches.

```python
rho = -0.1
```

---

# 🎲 Tournament Simulation

The simulation engine models the complete FIFA World Cup tournament structure.

### Group Stage Workflow

1. Simulate fixtures
2. Allocate points
3. Update standings
4. Rank teams
5. Determine qualification

### Knockout Stage Workflow

* Round of 32
* Round of 16
* Quarter-finals
* Semi-finals
* Final

using official FIFA bracket mappings.

---

# 📊 Dataset Summary

| Dataset                   | Description                            |
| ------------------------- | -------------------------------------- |
| `results.csv`             | Historical international match results |
| `goalscorers.csv`         | Goalscorer information                 |
| `competitive_matches.csv` | Competitive international fixtures     |
| `wc_matches.csv`          | FIFA World Cup matches                 |
| `elo_ratings.csv`         | National team Elo ratings              |
| `team_strength.csv`       | Offensive & defensive strength metrics |
| `fixtures_2026.csv`       | FIFA World Cup 2026 fixtures           |

---

# 📁 Project Structure

```bash
World-Cup-Predictor/
│
├── notebooks/
│   ├── data_collection.ipynb
│   ├── data_processing.ipynb
│   ├── elo_ratings.ipynb
│   ├── national_teams_data.ipynb
│   ├── fetch_fixtures.ipynb
│   ├── model.ipynb
│   └── simulation.ipynb
│
├── data/
│   ├── results.csv
│   ├── goalscorers.csv
│   ├── wc_matches.csv
│   ├── competitive_matches.csv
│   ├── clean_wc_matches.csv
│   ├── clean_competitive_matches.csv
│   ├── elo_ratings.csv
│   ├── team_strength.csv
│   ├── fixtures_2026.csv
│   ├── fixtures_group_stage.csv
│   ├── fixtures_knockouts.csv
│   └── national_teams.csv
│
├── model.py
└── README.md
```

---

# ⚡ Computational Optimizations

### ✅ Vectorized Probability Computation

Uses NumPy vectorization and `np.outer()` instead of nested loops.

### ✅ Precomputed Matchups

Caches match probabilities to avoid repeated computations during tournament simulation.

---

# 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* SciPy
* Requests
* Pathlib

### APIs & Sources

* [https://www.football-data.org/](https://www.football-data.org/)
* [https://www.eloratings.net/](https://www.eloratings.net/)
* [https://www.transfermarkt.com/](https://www.transfermarkt.com/)

---

# 🚀 Future Improvements

Potential future enhancements include:

* 📈 Dynamic Elo updates
* ⚽ Expected Goals (xG) integration
* 🤖 Machine learning models
* 👤 Player-level statistics
* 🚑 Injury & suspension tracking
* 🌐 Large-scale tournament simulations

---

# 📝 Conclusion

This project demonstrates a complete football analytics and tournament prediction framework using:

* Historical football data
* Team strength estimation
* Elo ratings
* Poisson goal modeling
* Dixon-Coles correction
* Monte Carlo tournament simulation

The modular pipeline provides a realistic and extensible system for FIFA World Cup outcome prediction under uncertainty.

---

# 📚 References

1. Dixon, M. J., & Coles, S. G. (1997). *Modelling Association Football Scores*
2. [https://www.eloratings.net/](https://www.eloratings.net/)
3. [https://www.football-data.org/](https://www.football-data.org/)
4. [https://www.transfermarkt.com/](https://www.transfermarkt.com/)
5. [https://numpy.org/](https://numpy.org/)
6. [https://pandas.pydata.org/](https://pandas.pydata.org/)
7. [https://scipy.org/](https://scipy.org/)