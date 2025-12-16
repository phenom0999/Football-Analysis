# Premier League Football Analysis (2017-18)

Comprehensive data analysis and visualization of the 2017-18 Premier League season, featuring expected goals (xG) modeling, shot analysis, and player performance metrics.

## Features

### 1. Expected Goals (xG) Model
- Logistic regression model predicting goal probability from shot characteristics
- Handles class imbalance through weighted training
- Calibrated predictions for accurate xG estimates
- Player-level aggregation identifying over/underperformers

### 2. Shot Analysis
- [Describe what you analyze about shots]

### 3. Goal Visualization
- [Describe your goal position analysis]

### 4. Assist Networks
- [Describe your assist path visualizations]

### 5. [Any Other Analysis]
- [Add more sections for other visualizations/analyses you have]

## Dataset

Soccer Match Event Dataset (2017-18 Premier League) from Figshare.
See `data/DATA_SOURCE.md` for details.

## Usage

1. **Download dataset** - Follow instructions in `data/DATA_SOURCE.md` to download and place the data one level above this repo
2. **Process data** - Run `notebooks/data_processing.ipynb` to create database from raw JSON files
3. **Run analysis** - Open `notebooks/xG_analysis.ipynb` for main analysis and visualizations
