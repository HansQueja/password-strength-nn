
"""
From a given password, the following features will be extracted
- Length of the password
- Has upper case characters
- Has lower case characters
- Has numerical characters
- Has special characters
- Number of numerical characters
- Number of special characters
- Binary classification if the password is in a public dictionary or not

The values will be extracted as a set of vectors.

NOTE: method here is the argument provided from the command line
ex. python main.py --method predict
"""

import numpy as np
import pandas as pd

def extract(method):

    # String list of special characters for checking
    special_characters = '[@_!#$%^&*()<>?/\\}{~:]' 

    # Data structures for parsed data storage
    vector_dataset = []
    label = []

    # Read through the training data and convert them into vector embeddings
    print(f"\nParsing {method}ing data..\n")
    dataframe = pd.read_csv(f"dataset/{method}.csv", encoding='utf-8', on_bad_lines='skip') 

    for index, row in dataframe.iterrows():
        password = str(row.iat[0].strip())
        strength = row.iat[1]

        # Prepare vector list for later storage
        vector = [0] * 8

        # If the training data has invalid characters, skip it
        if len(row) > 2:
            continue
        
        # Get length of password
        vector[0] = len(password)

        # Loop through the password to check some features
        for char in password:
            if char.isupper() and vector[1] == 0:
                vector[1] = 1
            if char.islower() and vector[2] == 0:
                vector[2] = 1
            if char.isnumeric():
                vector[3] = 1
                vector[5] += 1
            if char in special_characters:
                vector[4] = 1
                vector[6] += 1
        label.append(strength)

        # Append vector to the embedding data structure
        vector_dataset.append(vector)

    print("Embedding finished. Saving training data...")
    # Prepare input and output data 
    X = np.array(vector_dataset)
    Y = np.array(label)

    # Save preprocessed data
    np.savez(f"dataset/{method}_embed_dataset.npz", X=X, Y=Y)
    print("Training dataset saved.\n")

    return X, Y