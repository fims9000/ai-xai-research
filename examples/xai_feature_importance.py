import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from ai_xai_toolkit.xai.explainers import SimpleGlobalFeatureImportance

X, y = load_breast_cancer(return_X_y=True)
clf = RandomForestClassifier(random_state=0).fit(X, y)

expl = SimpleGlobalFeatureImportance(clf, accuracy_score)
imp = expl.importance(X, y)
print("Global permutation importances:", imp)
