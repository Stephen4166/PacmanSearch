# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class Node:
    def __init__(self, state, action, cost, parent):
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent   # last position


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    start_state = problem.getStartState()
    visited = []
    queue = util.Queue()
    queue.push(Node(start_state, None, 0, None))
    finalNode = None
    while not queue.isEmpty():
        tempN = queue.pop()
        if tempN.state in visited:
            continue
        else:
            visited.append(tempN.state)
        # if we arrive
        if problem.isGoalState(tempN.state):
            finalNode = tempN
            break
        for triple in problem.getSuccessors(tempN.state):
            node = Node(triple[0], triple[1], triple[2], tempN)
            queue.push(node)
        
    ans = []    
    temp = finalNode
    while temp:
        if temp.action is not None:
            ans.append(temp.action)
        temp = temp.parent
    ans.reverse()
    return ans

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    root = Node(start_state, None, 0, None)
    pq = util.PriorityQueue()
    pq.push(root, 0)
    while not pq.isEmpty():
        node = pq.pop()
        # print node.cost
        if problem.isGoalState(node.state):
            ans = []
            while node.parent is not None:
                ans.append(node.action)
                node = node.parent
            ans.reverse()
            return ans
        successors = problem.getSuccessors(node.state)
        for triple in successors:
            newnode = Node(triple[0], triple[1], triple[2]+node.cost, node)
            if triple[0] in problem._visitedlist:
                continue
            pq.update(newnode, newnode.cost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    root = Node(start_state, None, 0, None)
    pq = util.PriorityQueue()
    pq.push(root, heuristic(start_state, problem))
    while not pq.isEmpty():
        node = pq.pop()
        # print node.cost
        if problem.isGoalState(node.state):
            ans = []
            while node.parent is not None:
                ans.append(node.action)
                node = node.parent         
            ans.reverse()
            return ans
        successors = problem.getSuccessors(node.state)
        for triple in successors:
            if triple[0] in problem._visitedlist:
                continue
            newnode = Node(triple[0], triple[1], triple[2]+node.cost, node)
            heur = heuristic(newnode.state, problem)
            pq.update(newnode, newnode.cost+heur)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
