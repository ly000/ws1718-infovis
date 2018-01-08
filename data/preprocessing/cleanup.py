import sys
import pandas as pd
import numpy as np

def preproc(input, output):
    unprocessed_data = pd.read_csv(input, decimal=",")
    #data = pd.DataFrame([np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5], columns)
    data = unprocessed_data.dropna(axis=1, how='all');
    data['JAHR'].astype(int)
    data = data[data['JAHR'] >= 2007]
    data = data[data['JAHR'] <= 2014]
    #data = data.sort_index(ascending=True);
    data = data.sort_values(by=['NUMMER','JAHR'])
    #data.groupby('NUMMER')
    #data['INDIKATOR_WERT'].astype(float);
    #data = data.groupby('NUMMER').apply(pd.DataFrame.sort, 'JAHR');
    data.to_csv(output);
    print(data.head());

if __name__ == "__main__":
    inp = sys.argv[1]
    outp = sys.argv[2]
    preproc(inp, outp)
