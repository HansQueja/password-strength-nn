
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical
from keras.metrics import CategoricalAccuracy
from keras.models import load_model

MODEL_PATH = "model/password_model.keras"

"""
Trains the model from the input and output vectors from the feature extractor
"""
def train(X, y):

    # Convert the y values into a softmax of three values
    y = to_categorical(y, num_classes=3)

    # Split data into training and testing splits
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Build a basic feedforward neural network with two hidden 
    model = Sequential([
        Dense(16, input_dim=X.shape[1], activation='relu'),
        Dense(32, activation='relu'),
        Dense(3, activation='softmax')
    ])

    # Compile model to add optimizers and metrics to measure performance
    model.compile(
        optimizer='adam', 
        loss='mse', 
        metrics=[
            CategoricalAccuracy(name="categorical_accuracy")
        ])

    early_stop = EarlyStopping(
            monitor='val_loss',    
            patience=2,           
            restore_best_weights=True 
        )

    # Train model with validation to adjust weights and biases
    model.fit(
        X_train, 
        y_train, 
        epochs=50, 
        validation_split=0.1, 
        batch_size=16, 
        callbacks=[early_stop],
        verbose=1
    )

    # Save trained model
    model.save(MODEL_PATH)

    # Evaluate the trained model using the testing split
    history = model.evaluate(
        x=X_test,
        y=y_test,
        return_dict=True
    )

    # Print Results
    print("=" * 50)
    print("Training Complete. Metrics below:\n")
    print(f"Categorical Accuracy: {history["categorical_accuracy"]:.3f}")
    print(f"Loss (MSE): {history["loss"]:.3f}\n")
    print("=" * 50)


"""
Predict
"""
def predict(X, y):
    # Load the model for testing
    model = load_model(MODEL_PATH)

    # Convert the y values into a softmax of three values
    y = to_categorical(y, num_classes=3)

    # Predict and evaluate using the x test split
    predictions = model.predict(X, verbose=2)

    mse = mean_squared_error(y, predictions)

    print(mse)
