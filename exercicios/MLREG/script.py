import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plot

x = np.array([4, 10, 14, 19, 25, 31]).reshape(-1, 1)
y = np.array([6, 19, 14, 29, 25, 41])

model = LinearRegression().fit(x, y)

r_2 = model.score(x, y)
print(r_2)

y_prev = model.predict(x)

plot.scatter(x, y, color="red")
plot.plot(x, y_prev,color="black", linewidth=2)
plot.show()