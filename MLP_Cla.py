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

def train(x_array, y_array, layer_size) :

    
    # Step 1: Preprocess the data (flattening)
    x_array = transformArray(np.array(x_array))
    y_array = np.array(y_array)

    # Step 2: Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x_array, y_array, test_size=0.2, random_state=42)

    # Step 3: Scale
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Step 4: Create MLPClassifier model
    mlp = MLPClassifier(hidden_layer_sizes=layer_size,
        max_iter=1000, 
        activation='relu',
        solver='adam',
        alpha=0.01,
        early_stopping=True,
        n_iter_no_change=10)

    # Step 5: Train the model
    mlp.fit(X_train, y_train)

    # Step 6: Predict with the trained model
    y_pred = mlp.predict(X_test)
    
    # Step 7: Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    #print(f"Accuracy: {accuracy * 100:.2f}%")

    train_accuracy = mlp.score(X_train, y_train)
    test_accuracy = mlp.score(X_test, y_test)
    print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
    print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

    return accuracy

def main(x_array, y_array ) :
    train(x_array, y_array,(220,))

if __name__ ==  "__main__" :
    sys.exit(main())