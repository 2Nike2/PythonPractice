"""糖尿病データセットの回帰分析."""

import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

diabetes_data = load_diabetes()

x_df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
y_df = pd.DataFrame(diabetes_data.target, columns=["diabetes"])

model = LinearRegression()
scores = cross_val_score(model, x_df, y_df, cv=5)
print(scores.mean())
