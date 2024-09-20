import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class QNN(nn.Module):
    """Reseau de neurones pour approximer la Q fonction."""

    def __init__(self,input_dim:int, output_dim:int):
        """Initialisation des parametres ...
        """
        super(QNN, self).__init__()
        
        "*** TODO ***"
        
    def forward(self, state: np.ndarray) -> torch.Tensor :
        """Forward pass"""

        if isinstance(state, np.ndarray):
            state = torch.tensor(state, dtype=torch.float)
            
        "*** TODO ***"
        
        return state


