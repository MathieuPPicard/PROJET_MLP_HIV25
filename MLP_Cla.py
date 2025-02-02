from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from PIL import Image
import os

# Function to load images and labels for cap detection
def load_images(image_folder):
    images = []
    labels = []
    for file in os.listdir(image_folder):
        if file.endswith(".jpg") or file.endswith(".png"):  # Image format
            image_path = os.path.join(image_folder, file)
            image = Image.open(image_path).convert("L")  # Convert to grayscale
            image = image.resize((11, 11))  # Resize images to standard size
            image_array = np.array(image).flatten()  # Flatten image into 1D array
            images.append(image_array)
            
            # Assign label based on file name (OK or NOT OK)
            label = 1 if "Ok_Image" in file else 0  # OK = 1, NOT OK = 0
            labels.append(label)
    
    return np.array(images), np.array(labels)

# Load images and labels from your 'ImagesMLP' folder
X, y = load_images('ImagesMLP')

# Step 1: Preprocess the data (scaling)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Create MLPClassifier model
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, activation='relu', solver='adam', random_state=42)

# Step 4: Train the model
mlp.fit(X_train, y_train)

# Step 5: Predict with the trained model
y_pred = mlp.predict(X_test)

# Step 6: Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
