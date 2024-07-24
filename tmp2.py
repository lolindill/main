import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Example preprocessing function
def preprocess_data(data):
    # Convert categorical data (action_chosen) into numerical values
    action_mapping = {'attack': 0, 'defend': 1, 'special': 2}
    data['action_chosen'] = action_mapping.get(data['action_chosen'], -1)
    
    # Prepare feature vector
    feature_vector = np.array([
        data['player_health'],
        data['enemy_health'],
        data['player_energy'],
        data['action_chosen']
    ])
    
    return feature_vector

# Example model
def build_model(input_shape):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_shape,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')  # Assuming binary outcome (win/lose)
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Example usage
data = {'player_health': 50, 'enemy_health': 30, 'player_energy': 3, 'action_chosen': 'attack'}
feature_vector = preprocess_data(data)
feature_vector = feature_vector.reshape((1, -1))  # Add batch dimension

model = build_model(input_shape=feature_vector.shape[1])
# You would normally train your model here with historical data.
# For demonstration, we're not training here.

# Prediction example
# prediction = model.predict(feature_vector)
# print(prediction)
