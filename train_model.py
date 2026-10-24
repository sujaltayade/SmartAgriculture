
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Step 1: Load crop dataset
data = pd.read_csv("data/crop_data.csv")

# Step 2: Separate inputs and output
X = data.drop("label", axis=1)
y = data["label"]

# Step 3: Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Step 4: Define five ML algorithms
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(kernel="rbf"),
    "Naive Bayes": GaussianNB()
}

# Step 5: Create models directory
os.makedirs("models", exist_ok=True)

results = []
trained_models = {}

# Step 6: Train and evaluate each algorithm
for name, algorithm in models.items():

    # Scale features where useful
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", algorithm)
    ])

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    results.append({
        "Algorithm": name,
        "Accuracy (%)": round(accuracy * 100, 2)
    })

    trained_models[name] = model

    print(f"\n{name}")
    print(f"Accuracy: {accuracy * 100:.2f}%")

# Step 7: Compare results
results_df = pd.DataFrame(results)
results_df = results_df.sort_values(
    by="Accuracy (%)",
    ascending=False
)

print("\n========== MODEL COMPARISON ==========")
print(results_df.to_string(index=False))

# Step 8: Select the best model based on test accuracy
best_name = results_df.iloc[0]["Algorithm"]
best_model = trained_models[best_name]

# Step 9: Save the best model
joblib.dump(best_model, "models/crop_model.pkl")

# Save the selected model name
with open("models/crop_model_name.txt", "w") as file:
    file.write(best_name)

print(f"\nBest model: {best_name}")
print("Saved model to models/crop_model.pkl")

# Step 10: Detailed evaluation of the selected model
best_predictions = best_model.predict(X_test)

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(y_test, best_predictions))
