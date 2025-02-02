from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np 
import sys

np.set_printoptions(threshold=np.inf) 

def transformArray(array) :
    array = array.reshape(array.shape[0], -1)
    return array

def train(x_array, y_array) :
    # Step 1: Preprocess the data (flattening)
    x_array = transformArray(np.array(x_array))
    y_array = np.array(y_array)

    # Step 2: Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x_array, y_array, test_size=0.2, random_state=42)
    print(X_train)
    print(y_train)
    print("================")
    print(X_test)
    print(y_test)

    # Step 3: Create MLPClassifier model
    mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, activation='relu', solver='adam', random_state=42)

    # Step 4: Train the model
    mlp.fit(X_train, y_train)

    # Step 5: Predict with the trained model
    y_pred = mlp.predict(X_test)

    # Step 6: Evaluate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")

def main(x_array, y_array ) :
    train(x_array, y_array)

if __name__ ==  "__main__" :
    sys.exit(main())