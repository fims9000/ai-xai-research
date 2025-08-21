from typing import Any, Dict
import numpy as np

class SimpleGlobalFeatureImportance:
    """Baseline: permutation-based feature importance for tabular models."""
    def __init__(self, model, metric):
        self.model = model
        self.metric = metric

    def importance(self, X: np.ndarray, y: np.ndarray) -> Dict[int, float]:
        baseline = self.metric(y, self.model.predict(X))
        importances = {}
        rng = np.random.RandomState(42)
        for j in range(X.shape[1]):
            Xp = X.copy()
            rng.shuffle(Xp[:, j])
            score = self.metric(y, self.model.predict(Xp))
            importances[j] = baseline - score
        return importances
