from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from PIL import Image
import os

# Define a function to load images and their labels
def load_images(image_folder):
    images = []
    labels = []
    for file in os.listdir(image_folder):
        if file.endswith(".jpg") or file.endswith(".png"):  # Assuming the images are in jpg or png format
            image_path = os.path.join(image_folder, file)
            image = Image.open(image_path).convert("L")  # Convert to grayscale (optional)
            image = image.resize((11, 11))  # Resize to 11x11 pixels
            image_array = np.array(image).flatten()  # Flatten to 1D array
            images.append(image_array)
            
            # Label as 0 for 'NOk_Image_*' (not okay) and 1 for 'Ok_Image_*' (okay)
            label = 1 if "Ok_Image" in file else 0  # Label 1 for 'Ok_Image_*', 0 for 'NOk_Image_*'
            labels.append(label)
    
    return np.array(images), np.array(labels)

# Load the data (replace with the path to your image folder containing cap images)
X, y = load_images('ImagesMLP')

# Step 1: Preprocessing the data (Scaling features)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Choose the model (MLPClassifier for classification)
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, activation='relu', solver='adam', random_state=42)

# Step 4: Training the model
mlp.fit(X_train, y_train)

# Step 5: Making predictions
y_pred = mlp.predict(X_test)

# Step 6: Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
