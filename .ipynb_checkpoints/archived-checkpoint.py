import queries
import plots
import pandas as pd

class archived():

    def __init__(self):
        self.query = queries.queries()
        self.plot = plots.plots()
        
    def find_matches_with_anomaly_goals_of_team(self, teamID):

        a = self.query.get_goals_by_team_per_match(teamID)[["match_id", "score"]]
        b = self.query.get_goals_by_team_per_match_from_events(teamID)

        merged = pd.merge(a, b, left_on='match_id', right_on='matchId', how='left')
        merged = merged.drop("matchId", axis=1)
        merged['score_y'] = merged['score_y'].fillna(0).astype(int)
        
        merged['anomaly'] = merged['score_x'] - merged['score_y']
        
        anomalies = merged[merged["anomaly"] != 0]
        
        matches = self.query.get_matches_by_team(teamID)
        
        return matches[matches["match_id"].isin(anomalies["match_id"])]