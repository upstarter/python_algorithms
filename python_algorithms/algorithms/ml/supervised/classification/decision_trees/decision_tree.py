import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# %matplotlib inline

### Import data
# Always good to set a seed for reproducibility
SEED = 222
np.random.seed(SEED)

df = pd.read_csv(
    "python_algorithms/algorithms/ml/supervised/classification/decision_trees/input.csv"
)

### Training and test set
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score


def get_train_test(test_size=0.95):
    """Split Data into train and test sets."""
    y = 1 * (df.cand_pty_affiliation == "REP")
    X = df.drop(["cand_pty_affiliation"], axis=1)
    X = pd.get_dummies(X, sparse=True)
    X.drop(X.columns[X.std() == 0], axis=1, inplace=True)
    return train_test_split(X, y, test_size=test_size, random_state=SEED)


xtrain, xtest, ytrain, ytest = get_train_test()

# A look at the data
print("\nExample data:")
df.head()


import pydotplus
from IPython.display import Image
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def print_graph(clf, feature_names):
    """Print decision tree."""
    graph = export_graphviz(
        clf,
        label="root",
        proportion=True,
        impurity=False,
        out_file=None,
        feature_names=feature_names,
        class_names={0: "D", 1: "R"},
        filled=True,
        rounded=True,
    )
    graph = pydotplus.graph_from_dot_data(graph)
    return Image(graph.create_png())


t1 = DecisionTreeClassifier(max_depth=1, random_state=SEED)
t1.fit(xtrain, ytrain)
p = t1.predict_proba(xtest)[:, 1]

print("Decision tree ROC-AUC score: %.3f" % roc_auc_score(ytest, p))
print_graph(t1, xtrain.columns)


# t2 = DecisionTreeClassifier(max_depth=3, random_state=SEED)
# t2.fit(xtrain, ytrain)
# p = t2.predict_proba(xtest)[:, 1]
#
# print("Decision tree ROC-AUC score: %.3f" % roc_auc_score(ytest, p))
# print_graph(t2, xtrain.columns)
