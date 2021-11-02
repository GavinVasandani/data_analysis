import pandas as pd
import numpy as np


def read_csv_file(file: str):
    df = pd.read_csv(file)
    df.index = np.arange(1, len(df) + 1)
    print(df)


def main() -> None:
    read_csv_file("Copy of packages.csv")


if __name__ == '__main__':
    main()
