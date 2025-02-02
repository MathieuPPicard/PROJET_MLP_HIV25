# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Loading a sample dataset (Iris dataset for classification)
data = load_iris() # TO DO LOAD MY DATA
X = data.data  # Features
y = data.target  # Labels

# Step 1: Preprocessing the data (Scaling features)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Creating the MLP model
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, activation='relu', solver='adam', random_state=42)

# Step 4: Training the model
mlp.fit(X_train, y_train)

# Step 5: Making predictions
y_pred = mlp.predict(X_test)

# Step 6: Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
