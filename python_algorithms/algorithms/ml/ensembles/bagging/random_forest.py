### LOAD DATA
from sklearn import datasets

iris = datasets.load_iris()

# print label species and four features names
print(iris.target_names)
print(iris.feature_names)

### EXPLORE THE DATA
# print top 5 records
print(iris.data[0:5])

# print the iris labels (0:setosa, 1:versicolor, 2:virginica)
print(iris.target)

# DataFrame Creation
import pandas as pd
data=pd.DataFrame({
    'sepal length':iris.data[:,0],
    'sepal width':iris.data[:,1],
    'petal length':iris.data[:,2],
    'petal width':iris.data[:,3],
    'species':iris.target
})
data.head()

# separate the columns into dependent and independent variables (or features and
# labels). Split those variables into a training and test set.
# Import train_test_split function
from sklearn.model_selection import train_test_split

# Features
X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]
# Labels
y=data['species']

# Split into training set and test set; 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# After splitting, train the model on the training set and perform predictions
# on the test set.

# Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

# Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

# Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

# After training, check the accuracy using actual and predicted values.
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# which type of flower is it?
clf.predict([[3, 5, 4, 2]]) # Virginica


### FEATURE IMPORTANCES
from sklearn.ensemble import RandomForestClassifier

# Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

# Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

import pandas as pd
feature_imp = pd.Series(clf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)
feature_imp


### VISUALISATION
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
# Creating a bar plot
sns.barplot(x=feature_imp, y=feature_imp.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.legend()
plt.show()


### GENERATING THE MODEL ON SELECTED FEATURES
# Remove the "sepal width" feature because it has very low importance, and
# select the 3 remaining features.

# Import train_test_split function
from sklearn.cross_validation import train_test_split

## Split dataset into features and labels; removed feature "sepal width"
X=data[['petal length', 'petal width', 'sepal length']]
y=data['species']

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=5) # 70% training and 30% test

# After spliting, generate a model on the selected training set features,
# perform predictions on the selected test set features, and compare actual
# and predicted values.

# Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

# Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

# prediction on test set
y_pred=clf.predict(X_test)

# for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
