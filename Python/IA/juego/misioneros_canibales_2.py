
from dataclasses import dataclass,field
from copy import deepcopy
from collections import deque
from typing import TypeVar
from graphviz import Digraph

import sys 
import time

Node = TypeVar("Node")

@dataclass
class State:
    missioneries : int
    cannibals : int
    boat : int

    def successor(self):
        pass

    def is_valid(self):
        pass

    def is_goal(self):
        pass


@dataclass
class Node:
    parent : Node
    state : State
    action : None
    depth : int

    def expand(self):
        pass

    def extract_soluction(self):
        pass

def bfs(initial_state): #Search first in depth
    pass

def main():
    pass

if __name__  == "__main__":
    main()