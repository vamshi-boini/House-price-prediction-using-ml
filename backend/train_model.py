import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# ensure model folder exists
os.makedirs("model", exist_ok=True)

# load dataset
df = pd.read_csv("../data/housing.csv")

# handle missing values
df["total_bedrooms"].fillna(df["total_bedrooms"].median(), inplace=True)

# features and target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# categorical & numerical columns
categorical_features = ["ocean_proximity"]
numerical_features = X.drop(columns=categorical_features).columns.tolist()

# preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

# model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# train model
model.fit(X, y)

# save model
joblib.dump(model, "model/house_price_model.pkl")

print("✅ Model trained on housing.csv and saved successfully")
