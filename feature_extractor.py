
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
"""

import numpy as np
import csv

import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="tells the program if train or predict", type=str, default="train")
    args = parser.parse_args()

    if args.method == "train":
        return "training_data.csv"
    return "testing_data.csv"

def extract(passwords):

    special_characters = '[@_!#$%^&*()<>?/\\}{~:]' 

    password_dictionary = {}
    vector_dataset = []

    # Place inside a dictionary common passwords
    with open("dataset/common_pass.txt", mode='r', encoding='utf-8', errors='replace') as file:
        print("Reading through common passwords and storing it to a dictionary...")
        for line in file:
            password = line.strip()
            password_dictionary[password] = None

    with open(f"dataset/{passwords}", mode='r', encoding='utf-8', errors='replace') as file:
        print("Parsing through training dataset and extracting features...")
        reader = csv.reader(file)
        for row in reader:

            password = row[0]
            strength = row[1]

            vector = [0] * 9
            
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
            if password in password_dictionary:
                vector[7] = 1
            else:
                vector[7] = 0
            vector[8] = strength
            vector_dataset.append(vector)

    with open('dataset/input.csv', 'w', newline='') as csvfile:
        print("Writing feature vectors to input.csv...")
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for vector in vector_dataset:
            spamwriter.writerow(vector)
                
                
                



if __name__ == "__main__":
    file = parser()
    extract(file)
    