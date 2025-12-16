# Data Source

## Dataset
Soccer Match Event Dataset from Figshare (2017-18 Premier League)

**Download:** [Figshare Collection](https://figshare.com/collections/Soccer_match_event_dataset/4415000)

## Setup Instructions

1. Download and extract the dataset
2. Place the data folder **one level above** this repository:
```
your-projects/
├── data/              ← Dataset goes here
│   ├── matches/
│   │   └── matches_England.json
│   ├── events/
│   │   └── events_England.json
│   ├── players.json
│   └── teams.json
└── football-analysis/ ← Your repo
    ├── notebooks/
    └── ...
```

3. Run `notebooks/data_processing.ipynb` to create the database

## Why External?
The original dataset (~500MB) is too large for GitHub.
