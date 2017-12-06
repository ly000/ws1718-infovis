import sys
import pandas as pd
import numpy as np

def preproc(input, output):
    unprocessed_data = pd.read_csv(input, index_col="NUMMER")
    #data = pd.DataFrame([np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5], columns)
    data = unprocessed_data.dropna(axis=1, how='all');
    data = data.sort_index(ascending=True)
    data.to_csv(output)
    print(data.head())

if __name__ == "__main__":
    inp = sys.argv[1]
    outp = sys.argv[2]
    preproc(inp, outp)
