## TEAM ANVESHAK 2024-25, CFI, IIT MADRAS ##
## POINT ROBOT MOTION PLANNING MAZE ##

##############################
## DON'T MODIFY THIS SCRIPT ##
##############################
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

colors = ['black', 'skyblue', 'orangered', 'lime']
cmap = ListedColormap(colors)

class Maze:

    def __init__(self, map_num=1):
        self.map_num = map_num
        self.maze=None
        self.fig = None
        self.ax = None

    def load_map(self):
        with open("map"+str(self.map_num)+".txt", 'r') as file:
            maze = []
            for line in file:
                line = line.rstrip()
                row = []
                for c in line:
                    if c == ' ':
                        row.append(1)
                    elif c == 's':
                        row.append(2)
                    elif c == 'g':
                        row.append(3)
                    else:
                        row.append(0)
                maze.append(row)

        self.maze = np.array(maze)
    
    def visualize_map(self):
        self.fig, self.ax = plt.subplots(figsize=(6,6))
        self.ax.pcolormesh(self.maze, cmap=cmap)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        plt.tight_layout()
        plt.gca().invert_yaxis()
        plt.show(block=False)

        # plt.show()
    
    def update_visualization(self, fringe, closed_list):
        self.ax.clear()
        self.ax.pcolormesh(self.maze, cmap=cmap)
        
        for node in fringe:
            rect = Rectangle((node[0][1], node[0][0]), 1, 1, color='blue', alpha=0.5)
            self.ax.add_patch(rect)
        for node in closed_list:
            rect = Rectangle((node[1], node[0]), 1, 1, color='red', alpha=0.5)
            self.ax.add_patch(rect)     
        
        plt.gca().invert_yaxis()
        plt.pause(0.2)
        plt.draw()
    
    def keep_plot_open(self, path):
        path = path[1:-1]
        for node in path:
                rect = Rectangle((node[1], node[0]), 1, 1, color='yellow', alpha=0.7)  # Yellow box for path
                self.ax.add_patch(rect)
        plt.show()
    
    def get_start_state(self):
        start = np.where(self.maze == 2)
        return ((start[0][0], start[1][0]), 0)

    def get_goal_state(self):
        goal = np.where(self.maze == 3)
        return (goal[0][0], goal[1][0])

    def get_distance(self, node, i):
         goal = self.get_goal_state()
         node = node[0]
         if i == "m":   ## Manhattan Distance
              return abs(goal[0]-node[0]) + abs(goal[1]-node[1])
         if i == "e":   ## Euclidean Distance
              return math.sqrt(pow(goal[0]-node[0],2) + pow(goal[1]-node[1],2))
    
    def get_successors(self, node):
        cost = 1
        successors = []
        node = node[0]
        node_cost = node[1]

        for del_x in range(-1,2,2):
                if self.maze[node[0]+del_x][node[1]] == 1 or self.maze[node[0]+del_x][node[1]] == 3:
                    successors.append(((node[0]+del_x, node[1]), cost))
        
        for del_y in range(-1,2,2):
                if self.maze[node[0]][node[1]+del_y] == 1 or self.maze[node[0]][node[1]+del_y] == 3:
                    successors.append(((node[0], node[1]+del_y), cost))
        
        return successors


    ################################
    ######## Diagnol Movement ######
    ################################
    # def get_successors(self, node):
    #     cost = 1
    #     successors = []
    #     node = node[0]
    #     node_cost = node[1]

    #     # Define all possible directions including diagonals
    #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    #     for direction in directions:
    #         new_x = node[0] + direction[0]
    #         new_y = node[1] + direction[1]

    #         # Check if the new position is within the maze boundaries and accessible
    #         if 0 <= new_x < len(self.maze) and 0 <= new_y < len(self.maze[0]) and \
    #         (self.maze[new_x][new_y] == 1 or self.maze[new_x][new_y] == 3):
    #             successors.append(((new_x, new_y), cost))

    #     return successors
