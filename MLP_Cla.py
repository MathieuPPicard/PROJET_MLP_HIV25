from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import ImageCapAnalyser as Analyser
import numpy as np 
import sys
import time

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

    # Step 8 : Time the model
    test_time = test(mlp,scaler)

    return accuracy , test_time

def test(mlp, scaler) :
    x_array, y_array = Analyser.analyseTest()

    # Step 1: Preprocess the test data (flattening)
    x_array = transformArray(np.array(x_array))
    y_array = np.array(y_array)

    # Step 2: Scale
    x_array = scaler.transform(x_array)

    # Step 3: make the mlp predict 
    start = time.perf_counter()
    result = mlp.predict(x_array)
    end = time.perf_counter()
    c_time = (end - start)
    print(f"Prediction time: {c_time:.4f} seconds")
    print("Predictions:", result)
    return c_time

def main(x_array, y_array ) :
    train(x_array, y_array,(220,))

if __name__ ==  "__main__" :
    sys.exit(main())