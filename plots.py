from queries import queries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



class plots:

    def __init__(self):
        self.query = queries()

    def plot_shooting_positions_of(self, playerID):

        player_shot_positions = self.query.shooting_positions_of(playerID)
        
        x = player_shot_positions["initialX"]
        y = player_shot_positions["initialY"]

        plt.figure(figsize=(15, 10))  # width=10 inches, height=6 inches
        plt.scatter(x, y)
        #plt.title(f"Goal Positions of {name}")
        plt.xlabel("Initial X")
        plt.ylabel("Initial Y")
        plt.xlim(0, 100)   # fixed x-axis range
        plt.ylim(0, 100)  # fixed y-axis range
    
        plt.gca().invert_yaxis()  # put 0 at top

        plt.show()  # optional depending on context   
    
        return 


    def plot_goal_positions_of(self, playerID):
        player_goal_positions = self.query.goal_positions_of(playerID)
        
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

        # Load and display background image
        img = mpimg.imread('football_pitch.jpg')
        plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto', alpha=0.65)
    
        plt.show()  # optional depending on context   
    
        return
        
    def plot_goal_positions_of_team(self, teamID):
        player_goal_positions = self.query.goal_positions_of(playerID)
        
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

        # Load and display background image
        img = mpimg.imread('football_pitch.jpg')
        plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto', alpha=0.65)
    
        plt.show()  # optional depending on context   
    
        return

    def plot_shots_vs_goals_of(self, playerID):
        player_shot_positions = self.query.shooting_positions_of(playerID)
        player_goal_positions = self.query.goal_positions_of(playerID)
        unsuccessful_shot_positions = player_shot_positions[~player_shot_positions["id"].isin(player_goal_positions["id"])]

        x_goal = player_goal_positions["initialX"]
        y_goal = player_goal_positions["initialY"]

        x_shot = unsuccessful_shot_positions["initialX"]
        y_shot = unsuccessful_shot_positions["initialY"]
    
        plt.figure(figsize=(15, 10))  # width=10 inches, height=6 inches
        plt.scatter(x_goal, y_goal, c="green")
        plt.scatter(x_shot, y_shot, c="red")
        #plt.title(f"Goal Positions of {name}")
        plt.xlabel("Initial X")
        plt.ylabel("Initial Y")
        plt.xlim(0, 100)   # fixed x-axis range
        plt.ylim(0, 100)  # fixed y-axis range
    
        plt.gca().invert_yaxis()  # put 0 at top

        # Load and display background image
        img = mpimg.imread('football_pitch.jpg')
        plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto', alpha=0.65)
    
        plt.show()  # optional depending on context 
        
        return


        
