from queries import queries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



class plots:

    def __init__(self):
        self.query = queries()

    def basic_plot(self, x=[], y=[], label=False):
        
        #plt.title(f"Goal Positions of {name}")
        plt.xlim(0, 100)   # fixed x-axis range
        plt.ylim(0, 100)  # fixed y-axis range
        plt.gca().invert_yaxis()  # put 0 at top
        
         # Load and display background image
        img = mpimg.imread('football_pitch.jpg')
        plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto', alpha=0.65)

        if label:
            # Label each point with its index
            for i, (xi, yi) in enumerate(zip(x, y)):
                plt.text(xi, yi, str(i), fontsize=9, ha='right', va='bottom')
            
        
        plt.show()  # optional depending on context  
        

    def plot_shooting_positions_of(self, playerID):

        player_shot_positions = self.query.shooting_positions_of(playerID)
        
        x = player_shot_positions["initialX"]
        y = player_shot_positions["initialY"]

        plt.figure(figsize=(15, 10))
        plt.scatter(x,y)

        
        self.basic_plot()
    
        return 


    def plot_goal_positions_of(self, playerID):
        player_goal_positions = self.query.goal_positions_of(playerID)
        
        x = player_goal_positions["initialX"]
        y = player_goal_positions["initialY"]

        plt.figure(figsize=(15, 10))
        plt.scatter(x, y)

        self.basic_plot(x,y,label=True)
    
        return

    def plot_assist_positions_of(self, playerID):
        player_goal_positions = self.query.assist_positions_of(playerID)
        
        x = player_goal_positions["initialX"]
        y = player_goal_positions["initialY"]

        plt.figure(figsize=(15, 10))
        plt.scatter(x, y, c='yellow')

        self.basic_plot(x,y,label=True)
    
        return

    def plot_assist_path_of(self, playerID):
        player_goal_positions = self.query.assist_positions_of(playerID)
        
        initialX = player_goal_positions["initialX"]
        initialY = player_goal_positions["initialY"]
        finalX = player_goal_positions["finalX"]
        finalY = player_goal_positions["finalY"]

        plt.figure(figsize=(15, 10))
        
        # Loop through each pair of start and end points
        for x1, y1, x2, y2 in zip(initialX, initialY, finalX, finalY):
            plt.plot([x1, x2], [y1, y2], c="black", linewidth=0.5)  # Draw line with points

        # Plot initial points
        plt.scatter(initialX, initialY, color='blue', label='Initial Position', zorder=3)
        
        # Plot final points
        plt.scatter(finalX, finalY, color='red', label='Final Position', zorder=3)

        plt.legend()

        self.basic_plot()
    
        return
        
    def plot_goal_positions_of_team(self, teamID, separate_players=False):
        team_goal_positions = self.query.goal_positions_of_team(teamID)
        
        x = team_goal_positions["initialX"]
        y = team_goal_positions["initialY"]
        player = team_goal_positions["shortName"]

        plt.figure(figsize=(15, 10))

        if separate_players:
            # Get unique players
            unique_players = list(set(player))
            
            # Create a color map
            custom_colors = [
            'red', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray',
            'black', 'white', 'cyan', 'magenta', 'gold', 'navy', 'maroon', 'indigo',
            'crimson', 'darkblue', 'darkorange', 'darkred', 'darkviolet', 'deeppink',
            'chocolate', 'darkgray', 'dodgerblue', 'hotpink', 'midnightblue', 'coral',
            'firebrick', 'royalblue', 'darkslateblue', 'orangered', 'darkmagenta',
            'steelblue', 'tomato', 'slateblue', 'darkturquoise', 'mediumorchid'
            ]
            colors = custom_colors[:len(unique_players)]
            
            # Plot each player with a different color
            for i, player_id in enumerate(unique_players):
                # Filter data for this player
                player_mask = [p == player_id for p in player]
                player_x = [x[j] for j, mask in enumerate(player_mask) if mask]
                player_y = [y[j] for j, mask in enumerate(player_mask) if mask]
  
                plt.scatter(player_x, player_y, c=[colors[i]], label=f'Player {player_id}')
    
            plt.legend()  # Show legend with player names
        else: 
            plt.scatter(x, y)
    
        self.basic_plot()  
    
        return


    def plot_shots_vs_goals_of(self, playerID):
        player_shot_positions = self.query.shooting_positions_of(playerID)
        player_goal_positions = self.query.goal_positions_of(playerID)
        unsuccessful_shot_positions = player_shot_positions[~player_shot_positions["id"].isin(player_goal_positions["id"])]

        x_goal = player_goal_positions["initialX"]
        y_goal = player_goal_positions["initialY"]

        x_shot = unsuccessful_shot_positions["initialX"]
        y_shot = unsuccessful_shot_positions["initialY"]

        plt.figure(figsize=(15, 10))
        plt.scatter(x_goal, y_goal, c="green")
        plt.scatter(x_shot, y_shot, c="red")
       
        self.basic_plot()
        
        return


        
