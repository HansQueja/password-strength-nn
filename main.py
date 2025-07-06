import argparse

from helpers.feature_extractor import extract
from helpers.model import train, predict


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="tells the program if train or predict", type=str, default="train")
    args = parser.parse_args()

    print("=" * 50)
    print(f"\nLaunching Password NN {args.method}")
    if args.method == "train":
        X, y = extract(args.method)
        train(X, y)
    else:
        X, y = extract(args.method)
        predict(X, y)

if __name__ == "__main__":
    parser()