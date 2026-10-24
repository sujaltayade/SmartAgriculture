
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the fertilizer dataset
data = pd.read_csv("data/fertilizer_data.csv")

# 2. Clean column names
data.columns = data.columns.str.strip()

# 3. Select input features and target
X = data.drop("Fertilizer Name", axis=1)
y = data["Fertilizer Name"]

# 4. Identify numerical and categorical columns
categorical_columns = ["Soil Type", "Crop Type"]
numerical_columns = [
    "Temparature",
    "Humidity",
    "Moisture",
    "Nitrogen",
    "Potassium",
    "Phosphorous"
]

# 5. Prepare preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "numerical",
            StandardScaler(),
            numerical_columns
        ),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ]
)

# 6. Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 7. Create the model pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    (
        "classifier",
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
    )
])

# 8. Train the model
model.fit(X_train, y_train)

# 9. Evaluate the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n========== FERTILIZER MODEL RESULTS ==========")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# 10. Save the trained model
os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/fertilizer_model.pkl"
)

print("\nFertilizer model saved successfully!")
print("Location: models/fertilizer_model.pkl")
