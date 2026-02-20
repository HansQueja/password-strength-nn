# Password Strength Neural Network

A neural network trained to classify passwords as **Weak**, **Moderate**, or **Strong** based on their structural characteristics and security features. Includes a real-time Tkinter GUI for easy testing.

## Overview

This project implements a machine learning model using Keras/TensorFlow that evaluates password strength. The model extracts specific structural features from a password and uses a feedforward neural network to provide a three-tier classification system, helping users understand their password security level instantly.

## Features

* **Three-tier Classification**: Categorizes passwords into Weak, Moderate, or Strong.
* **Real-time GUI**: Includes a Tkinter-based desktop app (`app.py`) that evaluates password strength keystroke by keystroke.
* **Feature Extraction**: Evaluates 8 specific password characteristics, including:
* Total length
* Presence of uppercase and lowercase letters
* Presence and count of numerical digits
* Presence and count of special characters
* Common dictionary password cross-referencing (via `common_passwords.npy`)


* **Automated Early Stopping**: Model training is optimized to prevent overfitting by monitoring validation loss.

## Quick Start

### Prerequisites

```bash
python >= 3.12

```

### Installation

```bash
# Clone the repository
git clone https://github.com/HansQueja/password-strength-nn.git
cd password-strength-nn

# Install dependencies
pip install -r requirements.txt

```

### Usage

**1. Training the Model via CLI**
To train the model using your datasets (ensure `dataset/train.csv` is present):

```bash
python main.py --method train

```

**2. Testing the Model via CLI**
To run predictions on a test dataset (ensure `dataset/predict.csv` is present):

```bash
python main.py --method predict

```

**3. Launching the GUI**
To open the interactive Password Strength Checker application:

```bash
python app.py

```

## Model Architecture

* **Input Layer**: 8 nodes (Vector embedding of extracted password features)
* **Hidden Layer 1**: 16 nodes (Dense), ReLU activation
* **Hidden Layer 2**: 32 nodes (Dense), ReLU activation
* **Output Layer**: 3 nodes (Dense), Softmax activation (Weak, Moderate, Strong classification)
* **Optimizer**: Adam
* **Loss Function**: Mean Squared Error (MSE)
* **Evaluation Metric**: Categorical Accuracy

## Training Details

### Dataset

* **Format**: CSV files located in `dataset/` (formatted as `password, strength_label`)
* **Text Conversion**: Common passwords text file converted to `.npy` via `helpers/text_convert.py`
* **Split**: 80% Training Data, 20% Testing Data (with a 10% validation split during the training phase)

### Training Parameters

* **Epochs**: 50 (with Early Stopping, patience=2)
* **Batch Size**: 16
* **Early Stopping**: Restores best weights based on validation loss

## Project Structure

```text
password-strength-nn/
├── .git/                   # Git repository data
├── dataset/                # Raw CSV files and embedded .npz datasets
├── helpers/                # Helper modules for data processing and modeling
│   ├── feature_extractor.py # Converts passwords to vector embeddings
│   ├── model.py             # Neural network architecture and training logic
│   └── text_convert.py      # Converts common passwords text to .npy
├── model/                  # Saved trained models (.keras)
├── venv/                   # Virtual environment (ignored in git)
├── .gitignore              # Git ignore rules
├── app.py                  # Tkinter GUI application for real-time checking
├── main.py                 # CLI entry point for training and predicting
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies

```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Open a Pull Request

## License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE) - see the https://www.google.com/search?q=LICENSE file for details.

---

*Made with ❤️ by Hans Queja*
