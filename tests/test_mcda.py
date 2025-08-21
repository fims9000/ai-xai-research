from ai_xai_toolkit.dss.mcda import weighted_sum
import numpy as np

def test_weighted_sum():
    scores = np.array([[1,2],[3,4]])
    w = np.array([0.3, 0.7])
    out = weighted_sum(scores, w)
    assert out.shape == (2,)
