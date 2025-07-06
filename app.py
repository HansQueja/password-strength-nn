import tkinter as tk
from tkinter import ttk
from keras.models import load_model
from helpers.feature_extractor import extract_input

MODEL_PATH = "model/password_model.keras"

def main():
    window = tk.Tk()
    window.title("Password Strength Checker")
    window.geometry("400x200")
    window.configure(bg="#f5f5f5")

    # Fonts and styling
    FONT_TITLE = ("Helvetica", 16, "bold")
    FONT_BODY = ("Helvetica", 12)

    # Title label
    label = tk.Label(window, text="Password Strength", font=FONT_TITLE, bg="#f5f5f5")
    label.pack(pady=(20, 10))

    # Entry field
    entry = ttk.Entry(window, font=FONT_BODY, width=30)
    entry.pack(pady=(0, 10))
    entry.focus()

    # Output label
    label_output = tk.Label(window, text="Type a password...", font=FONT_BODY, bg="#f5f5f5", fg="#444")
    label_output.pack(pady=(5, 10))

    def on_key_release(event):
        embedded = extract_input(entry.get())
        class_index, confidence = predict(embedded)
        label_output.config(
            text=f"Predicted: {['Weak', 'Moderate', 'Strong'][class_index]} ({confidence:.2f})",
            fg=["#d9534f", "#f0ad4e", "#5cb85c"][class_index]
        )

    entry.bind("<KeyRelease>", on_key_release)

    window.mainloop()

def predict(X):
    model = load_model(MODEL_PATH)
    prediction = model.predict(X, verbose=0)
    class_index = prediction.argmax(axis=1)[0]
    confidence = prediction[0][class_index]
    return class_index, confidence

if __name__ == "__main__":
    main()
