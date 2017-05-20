# This assignment is meant to give you an idea of your general workflow,
# that you will be following for the next assignments. 
# 
# It'll help you get used to the systems, check your level of readiness 
# for the course and weed out setup problems early on.
# 
# The assignment description will be provided in an iPython notebook, 
# in which you can also write code. A good introduction to iPython can
#  be found at http://opentechschool.github.io/python-data-intro/core/notebook.html.
# 
# You will have an python file that you'll submit to our test server,
# Bonnie. The code that we will test against will be in this file. 
# Any code in the iPython notebook is meaningless from the testing 
# perspective.
# 
# You should ideally take no more than 15 minutes, to finish the 
# following exercises.

# This file is your main submission that will be graded against. Only copy-paste
# code on the relevant classes included here from the IPython notebook. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.


from __future__ import division
import math
import random
import pickle
import sys
import os
# Comment the next line when submitting to bonnie
# import matplotlib.pyplot as plt









# Implement a heapq backed priority queue (accompanying the relevant question)
import heapq

class PriorityQueue():
    
    # HINT look up the module heapq.

    def __init__(self):
        self.queue = []
        self.current = 0        

    def next(self):
        if self.current >=len(self.queue):
            self.current
            raise StopIteration
    
        out = self.queue[self.current]
        self.current += 1

        return out

    def pop(self):
        raise NotImplementedError

    def remove(self, nodeId):
        raise NotImplementedError
    
    def __iter__(self):
        return self

    def __str__(self):
        return 'PQ:[%s]'%(', '.join([str(i) for i in self.queue]))

    def append(self, node):
        raise NotImplementedError

    def __contains__(self, key):
        self.current = 0
        return key in [n for v,n in self.queue]

    def __eq__(self, other):
        self.current = 0
        return self == other

    def size(self):
        return len(self.queue)
    
    def clear(self):
        self.queue = []
        
    def top(self):
        return self.queue[0]

    __next__ = next

#Warmup exercise: Implement breadth-first-search
def breadth_first_search(graph, start, goal):
    raise NotImplementedError

#Warmup exercise: Implement uniform_cost_search
def uniform_cost_search(graph, start, goal):
    raise NotImplementedError

# Warmup exercise: Implement A*
def null_heuristic(graph, v, goal ):
    return 0

# Warmup exercise: Implement the euclidean distance heuristic
def euclidean_dist_heuristic(graph, v, goal):
    raise NotImplementedError

# Warmup exercise: Implement A* algorithm
def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    raise NotImplementedError

# Exercise 1: Bidirectional Search
def bidirectional_ucs(graph, start, goal):
    raise NotImplementedError

# Exercise 2: Bidirectional A*
def bidirectional_a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    raise NotImplementedError

# Exercise 3: Tridirectional UCS Search
def tridirectional_search(graph, goals):
    raise NotImplementedError

# Exercise 4: Present an improvement on tridirectional search in terms of nodes explored
def tridirectional_upgraded(graph, goals, heuristic=euclidean_dist_heuristic):
    raise NotImplementedError

# Extra Credit: Your best search method for the race
# Loads data from data.pickle and return the data object that is passed to the custom_search method. Will be called only once. Feel free to modify. 
def load_data():
    data = pickle.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.pickle"), 'rb'))
    return data

def custom_search(graph, goals, data=None):
    raise NotImplementedError
