import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset (you can replace with real data)
data = {
    "income": [25000, 50000, 75000, 100000, 120000],
    "age": [25, 35, 45, 32, 52],
    "loan": [5000, 20000, 15000, 30000, 40000],
    "approved": [0, 1, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[["income", "age", "loan"]]
y = df["approved"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
