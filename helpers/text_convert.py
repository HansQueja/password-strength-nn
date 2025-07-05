
import numpy as np

def convert_text():

    # Data structures for parsed data storage
    password_dictionary = []

    # Read through common passwords and store it in a dictionary for lookups later
    with open("helpers/origin_data/common_pass.txt", mode='r', encoding='utf-8', errors='replace') as file:
        print("Reading through common passwords and storing it to a list...")
        for line in file:
            password = line.strip()
            password_dictionary.append(password)

    # Save preprocessed data
    np.save("common_passwords.npy", password_dictionary)
    print("Conversion of text file to npy complete.\n")

if __name__ == "__main__":
    convert_text()