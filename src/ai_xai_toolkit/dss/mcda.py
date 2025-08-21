import numpy as np

def weighted_sum(scores, weights):
    scores = np.asarray(scores)
    w = np.asarray(weights)
    w = w / w.sum()
    return (scores * w).sum(axis=1)
