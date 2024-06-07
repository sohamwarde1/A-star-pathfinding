## TEAM ANVESHAK 2024-25, CFI, IIT MADRAS ##
## POINT ROBOT MOTION PLANNING TASK 2     ##

## A STAR SEARCH ##

## USE THESE LIBRARIES, YOU WON'T NEED ANY OTHER AND YOU ARE NOT SUPPOSED TO USE TOO ##
import math
import numpy as np
from maze import Maze

def manhattan(node):
    # WRITE YOUR CODE HERE
    pass

def euclidean(node):
    # WRITE YOUR CODE HERE
    pass

def aStarSearch(start, goal, m, i, epsilon):
    # print(f"Start State: {start}")
    # print(f"Goal State: {goal}")

    ### THINK WHY THESE ARE DEFINED ###
    fringe, closed_list = [start+(m.get_distance(start,i),)], []
    parent = {}
    nodes_expanded = 0
    cost_so_far = {start[0] : 0}
    ### VISUALIZATION PURPOSE , DON'T MODIFY ###
    m.visualize_map()
    while fringe:
        ### VISUALIZATION PURPOSE , DON'T MODIFY ###
        m.update_visualization(fringe, closed_list)
        nodes_expanded+=1
        ### YOUR CODE STARTS HERE ###

        fringe.sort(key = lambda x: x[2])
        current = fringe[0]
        fringe.pop(0)
        
        if current[0] == goal:
            path = []
            node = goal
            while node != start[0]:
                path.append(node)
                node = parent[node]
            path.append(start[0])
            path.reverse()
            return path, nodes_expanded


        for next in m.get_successors(current):
            new_cost = cost_so_far[current[0]] + 1
            if (next not in fringe) and (next[0] not in closed_list):
                cost_so_far[next[0]] = new_cost
                priority = (1*new_cost) + (1*m.get_distance(next,i))
                fringe.append(next + (priority,))
                closed_list.append(next[0])
                parent[next[0]] = current[0]
            

                
            
               
        
    ### YOUR CODE ENDS HERE ###

if __name__ == "__main__":
    m = Maze(map_num=1) ## TOGGLE BETWEEN 1 AND 2 TO TEST IN BOTH ENVIRONMENTS 

    ###  DON'T MODIFY ###
    m.load_map()

    # m.visualize_map() ### UNCOMMENT THIS TO JUST VIEW THE MAZE, AND plt.show() IN MAZE.PY LINE 52, ALSO COMMENT THE BELOW 5 LINES TOO

    ### COMMENT THESE TO JUST VIEW THE MAZE
    i="e" ### Have a look at get_distance function in maze.py
    path, nodes_expanded = aStarSearch(m.get_start_state(), m.get_goal_state(), m, i, epsilon=1)  ### Don't worry about epsilon
    print(f"Number of Steps taken by the Robot: {len(path)}")
    print(f"Number of Nodes Expanded: {nodes_expanded}")
    m.keep_plot_open(path)
