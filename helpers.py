import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

class football:
    
    # Create SQLite engine (this creates a local file 'mydatabase.db')
    def __init__(self):  
        self.engine = create_engine('sqlite:///football.db')
    
    def load_data(self):
        # List of your CSV files and corresponding table names
        csv_files = {
            'players': 'dataframes/players.csv',
            'matches': 'dataframes/matches.csv',
            'events': 'dataframes/events.csv',
            'teams': 'dataframes/teams.csv',
            'positions': 'dataframes/positions.csv',
            'event_tags': 'dataframes/event_tags.csv'
        }
        
        for table_name, csv_file in csv_files.items():
            # Read CSV into DataFrame
            df = pd.read_csv(csv_file)
            
            # Write DataFrame to SQLite table (replace if exists)
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
            print(f'Loaded {csv_file} into table {table_name}')
        
        print("All files loaded into the database!")
    
    def query_this(self, query):
        result = pd.read_sql(query, con=self.engine)
        return result

    def show_players_table(self, limit):
        response = self.query_this(f""" SELECT * FROM players LIMIT {limit}""")
        return response
        
    def show_teams_table(self, limit):
        response = self.query_this(f""" SELECT * FROM teams LIMIT {limit}""")
        return response

    def show_matches_table(self, limit):
        response = self.query_this(f""" SELECT * FROM matches LIMIT {limit}""")
        return response

    def show_events_table(self, limit):
        response = self.query_this(f""" SELECT * FROM events LIMIT {limit}""")
        return response

    def show_event_tags_table(self, limit):
        response = self.query_this(f""" SELECT * FROM event_tags LIMIT {limit}""")
        return response

    def search_team_by_name(self, name, limit):
        query = f""" SELECT * FROM teams WHERE name LIKE '%{name}%' LIMIT {limit}"""
        response = self.query_this(query)
        return response

    def search_player_by_name(self, name, limit):
        query = f""" SELECT * FROM players WHERE firstName LIKE '%{name}%' OR lastName LIKE '%{name}%' LIMIT {limit}"""
        response = self.query_this(query)
        return response

    def get_all_players_from_team(self, teamID):
        query = f""" SELECT * FROM players WHERE currentTeamId = {teamID} """
        response = self.query_this(query)
        return response

    def get_match_by_id(self, matchID):
        query = f""" SELECT * FROM matches WHERE match_id = {matchID}"""
        response = self.query_this(query)
        return response

    
    def get_number_of_goals_by_player(self, playerID):
        query = f""" SELECT COUNT(events.id) AS 'Goals' FROM event_tags, events ON event_tags.event_id = events.id WHERE events.playerId={playerID} AND tag=101 AND eventId IN (3, 10)"""
        response = self.query_this(query)
        return response

    def get_number_of_goals_by_team(self, teamID):
        query = f""" SELECT (
                        SELECT COUNT(events.id)
                        FROM event_tags JOIN events
                        ON event_tags.event_id = events.id
                        WHERE events.teamId={teamID}
                        AND tag IN (101)
                        AND events.eventId IN (10, 3)) 
                    + (
                        SELECT COUNT(awarded_team) FROM (
                            SELECT 
                                CASE
                                    WHEN matches.away_team = own.teamId THEN matches.home_team
                                    ELSE matches.away_team
                                END AS awarded_team
                            FROM matches JOIN (
                                SELECT events.matchId, events.teamId
                                FROM events
                                JOIN event_tags 
                                    ON events.id = event_tags.event_id
                                WHERE tag = 102
                                ) AS own
                                ON matches.match_id = own.matchId
                        )
                         WHERE awarded_team={teamID}
                        ) AS total_goals
                """
        
        response = self.query_this(query)
        return response


    def get_goals_by_team_per_match(self, teamID):
        query = f"""
                    SELECT SUM(
                        CASE
                            WHEN matches.away_team = {teamID} THEN matches.away_score
                            ELSE matches.home_score
                        END
                        ) AS score
                        FROM matches WHERE matches.away_team = {teamID} OR matches.home_team = {teamID}
                        GROUP BY matches.match_id
                """
        response = self.query_this(query)
        return response


    def get_goals_by_all_teams(self):
        query = """
            SELECT 
                teams.name,
                SUM(goals_scored) AS total_goals
            FROM (
                SELECT 
                    home_team AS team_id,
                    home_score AS goals_scored
                FROM matches
                UNION ALL
                SELECT 
                    away_team AS team_id,
                    away_score AS goals_scored
                FROM matches
            ) AS all_goals
            JOIN teams
            ON all_goals.team_id = teams.wyId
            GROUP BY team_id
            ORDER BY total_goals DESC
        """
        return self.query_this(query)


    def get_all_goals_details_by_player(self, playerID):
        query = f"""SELECT * FROM matches
                    JOIN events
                    ON matches.match_id = events.matchId
                    WHERE events.id IN
                        (SELECT events.id FROM events 
                        JOIN event_tags
                        ON events.id = event_tags.event_id
                        WHERE tag = 101
                        AND eventId IN(3,10)
                        AND playerId = {playerID})
                 """
        response = self.query_this(query)
        return response
        
    def get_number_of_goals_by_players_from_team(self, teamID):
        pass
        query = none
        response = self.query_this(query)
        return response
    
    def shooting_positions_of(self, name):
        player_shots_positions = self.query_this(f"""SELECT * FROM positions
                      WHERE id IN (
                        SELECT id FROM events
                        WHERE playerId = (
                            SELECT wyId FROM players
                            WHERE shortName='{name}'
                        )
                        AND eventName='Shot'
                      )
                    """)
        
        x = player_shots_positions["initialX"]
        y = player_shots_positions["initialY"]
        
        plt.scatter(x, y)
        plt.title(f"Shooting Positions of {name}")
        plt.xlabel("Initial X")
        plt.ylabel("Initial Y")
        plt.show()  # optional depending on context   
    
        return
    
    
    def goal_positions_of(self, playerID):
        player_goal_positions = self.query_this(f"""SELECT * FROM positions
                      WHERE id IN (
                        SELECT events.id FROM events 
                        JOIN event_tags
                        ON events.id = event_tags.event_id
                        WHERE tag = 101
                        AND eventId IN(3,10)
                        AND playerId = {playerID})
                    """)
        
        x = player_goal_positions["initialX"]
        y = player_goal_positions["initialY"]

        plt.figure(figsize=(15, 10))  # width=10 inches, height=6 inches
        plt.scatter(x, y)
        #plt.title(f"Goal Positions of {name}")
        plt.xlabel("Initial X")
        plt.ylabel("Initial Y")
        plt.xlim(0, 100)   # fixed x-axis range
        plt.ylim(0, 100)  # fixed y-axis range
        # Label each point with its index
        for i, (xi, yi) in enumerate(zip(x, y)):
            plt.text(xi, yi, str(i), fontsize=9, ha='right', va='bottom')
        plt.gca().invert_yaxis()  # put 0 at top

        plt.show()  # optional depending on context   
    
        return
    
    
    def passing_positions_of(self, name):
        player_shots_positions = self.query_this(f"""SELECT * FROM positions
                      WHERE id IN (
                        SELECT id FROM events
                        WHERE playerId = (
                            SELECT wyId FROM players
                            WHERE shortName='{name}'
                        )
                        AND eventName='Pass'
                      )
                    """)
        
        x = player_passing_positions["initialX"]
        y = player_passing_positions["initialY"]
        
        plt.scatter(x, y)
        plt.title(f"Passing Positions of {name}")
        plt.xlabel("Initial X")
        plt.ylabel("Initial Y")
        plt.show()  # optional depending on context   
    
        return