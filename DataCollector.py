import pandas as pd
import os

CSV_PATH = 'data.csv'

def save(evaluation, average, nRange, n_image, n_layers, n_neurons,computation_time) :
    data = {
        'number_image' : n_image,
        'number_layer' : n_layers,
        'number_neurons' : n_neurons,
        'evaluation' : evaluation,
        'average' : average,
        'range' : nRange,
        'computation_time' : computation_time  
    }
    df = pd.DataFrame([data])

    if not os.path.exists(CSV_PATH) :
        df.to_csv(CSV_PATH, mode='w', index=False, header=True)
    else :
        df.to_csv(CSV_PATH, mode="a", index=False, header=False)

def deleteData() :
    try:
        os.remove(CSV_PATH)
    except:
        print('The csv file could not be remove.')