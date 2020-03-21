from sklearn.naive_bayes import GaussianNB

# Create SVM classification object
model = GaussianNB()

# there are other distributions for multinomial classes like
# Bernoulli Naive Bayes

# Assumed you have, X (predictor) and Y (target) for training data set and
# x_test(predictor) of test_dataset

# Train the model using the training sets and check score
model.fit(X, y)

# Predict Output
predicted = model.predict(x_test)
