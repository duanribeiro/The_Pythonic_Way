import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Read the database
customers = pd.read_csv("Ecommerce Customers")

# Select the independent and dependent variables.
y = customers['Yearly Amount Spent']
x = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]

# Split the data in training and test, then use the training data into our model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)
lm = LinearRegression()
lm.fit(x_train,y_train)


# Now try predict the test data using the model.
predictions = lm.predict(x_test)
plt.scatter(y_test,predictions)

# Make simple graph of the relation.
coef = [str(round(x,2)) for x in lm.coef_]
title = 'Coefficients: \n Avg. Session Length: {} - Time on App: {} - Time on Website: {} - Length of Membership: {}'.format(coef[0], coef[1], coef[2], coef[3])
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.title(title)
plt.show()

# Evaluating the model performance by calculating the residual sum of squares and the variance score explained (R ^ 2)
print('Mean absolute error: ', metrics.mean_absolute_error(y_test, predictions))
print('Mean squared error: ', metrics.mean_squared_error(y_test, predictions))
print('Root mean square deviation: ', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# Draw a histogram of the waste and make sure it looks normally distributed.
plt.hist(y_test-predictions)
plt.show()
