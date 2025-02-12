import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

CSV_PATH = 'data.csv'
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", 1000)  # Prevent line wrapping

def save(average, nRange, n_image, n_layers, n_neurons,computation_time, average_test_time) :
    data = pd.DataFrame([{
        'number_image' : n_image,
        'number_layer' : n_layers,
        'number_neurons' : n_neurons,
        'average' : average,
        'range' : nRange,
        'computation_time' : computation_time,
        'average_test_time' : average_test_time
    }])

    if not os.path.exists(CSV_PATH) :
        data.to_csv(CSV_PATH, mode='w', index=False, header=True)
    else :
        data.to_csv(CSV_PATH, mode="a", index=False, header=False)

def graphic() :
    df = pd.read_csv(filepath_or_buffer=CSV_PATH)
    fig, ax = plt.subplots()
    ax.scatter(df['number_neurons'], df['average'])

    # Label each point with its line number
    for i, row in df.iterrows():
        ax.text(row['number_neurons'], row['average'], str(i), fontsize=9, ha='right')    

    plt.show()

def graphicx3():
    # Read the CSV file
    df = pd.read_csv(filepath_or_buffer=CSV_PATH)
    
    df = df.drop(df[df['average'] == 1.0].index)

    print(df)

    # Create the figure with two subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 6))
    
    # Plot 1: average vs. number_neurones
    ax1.scatter(df['number_neurons'], df['average'], color='b')
    ax1.set_title('Average vs. Number of Neurones')
    ax1.set_xlabel('Number of Neurones')
    ax1.set_ylabel('Average')
    
    # Label each point with its line number
    for i, row in df.iterrows():
        ax1.text(row['number_neurons'], row['average'], str(i), fontsize=9, ha='right')
    
    # Plot 2: average vs. computation_time
    ax2.scatter(df['computation_time'], df['average'], color='r')
    ax2.set_title('Average vs. Computation Time')
    ax2.set_xlabel('Computation Time')
    ax2.set_ylabel('Average')
    
    # Label each point with its line number
    for i, row in df.iterrows():
        ax2.text(row['computation_time'], row['average'], str(i), fontsize=9, ha='right')

        # Plot 3: average vs. number_image
    ax3.scatter(df['number_image'], df['average'], color='r')
    ax3.set_title('Average vs. number of image')
    ax3.set_xlabel('number image')
    ax3.set_ylabel('Average')
    
    # Label each point with its line number
    for i, row in df.iterrows():
        ax3.text(row['number_image'], row['average'], str(i), fontsize=9, ha='right')
    
    # Show the plots
    plt.tight_layout()  # To ensure the subplots don't overlap
    plt.show()

def deleteData() :
    try:
        os.remove(CSV_PATH)
    except:
        print('The csv file could not be remove.')