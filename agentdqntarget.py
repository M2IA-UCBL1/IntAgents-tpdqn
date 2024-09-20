import numpy as np
import random
from collections import namedtuple, deque

from QNN import QNN
from replaybuffer import ReplayBuffer

import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim


class AgentDQNTarget():
    """Agent qui utilise l'algorithme DQN."""

    def __init__(self, state_size:int, action_size:int, gamma=0.99):
        """Constructeur.
        

        """
        self.state_size = state_size
        self.action_size = action_size
        

    def sampling_step(self,state : np.ndarray ,action : np.ndarray ,reward: float,next_state: np.ndarray ,done: bool):
        return 0
        
    def train_step(self):
        return 0
    
    
    def act_egreedy(self, state : np.ndarray ,eps: float = 0.0) -> int:
        return 0