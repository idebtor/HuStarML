import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])        # input
    w = np.array([0.5, 0.5])      # weights
    b = -0.75                      # bias
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    return 1
    
def NAND(x1, x2):
    return int(not AND(x1, x2))
    
def OR(x1, x2):
    x = np.array([x1, x2])        # input
    w = np.array([0.5, 0.5])      # weights
    b = -0,45                      # bias
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    return 1
    
def XOR(x1, x2):
    None
