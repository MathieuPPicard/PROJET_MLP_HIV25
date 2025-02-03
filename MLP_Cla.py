from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import sys

np.set_printoptions(threshold=np.inf)


def transformArray(array):
    array = array.reshape(array.shape[0], -1)  # Flatten the input
    return array


def train(x_array, y_array):
    # Step 1: Preprocess the data (flattening)
    x_array = transformArray(np.array(x_array))
    y_array = np.array(y_array)

    # Step 2: Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x_array, y_array, test_size=0.2, random_state=42)

    # Step 3: Standardize the data (important for neural networks)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Step 4: Create MLPClassifier model with L2 regularization and early stopping
    mlp = MLPClassifier(
        hidden_layer_sizes=(200, 100, 50),
        max_iter=500,
        activation='relu',
        solver='lbfgs',
        random_state=42,
        alpha=0.001,  # L2 regularization strength (you can adjust this value)
        early_stopping=True,  # Stop training early if the validation score stops improving
        n_iter_no_change=10  # Number of iterations with no improvement before stopping
    )

    # Step 5: Train the model
    mlp.fit(X_train, y_train)

    # Step 6: Predict with the trained model
    y_pred = mlp.predict(X_test)

    # Step 7: Evaluate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(mlp)

    print(f"Train Accuracy: {mlp.score(X_train, y_train)}")
    print(f"Test Accuracy: {mlp.score(X_test, y_test)}")

    predictions = mlp.predict(X_test)
    print(predictions)

    cm = confusion_matrix(y_test, predictions)
    print(cm)

    print(f"Accuracy: {accuracy * 100:.2f}%")


def main(x_array, y_array):
    train(x_array, y_array)


if __name__ == "__main__":
    sys.exit(main())  # Run the main function
