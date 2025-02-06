import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import DataCollector as Collector
import MLP_Cla as Classifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import sys
import shutil
import time

N_INPUT = 17 * 17

###TODO###
# DELETE THE OK AND NOK FOLDER [X]
# Loop while increasing the number of 1-Data sizes, 2-number of hidden layer and 3-the number of neuronnes [X]
# Use data augmentation to get less overfitting
# Create a evaluation function(weigh the following : average, range, time of computation, number of image + number of layer(neurons))
# The results of the models need to be save with DataCollector.py [ X ]
# With the results, plot and analyse the best combinaison of factors.
# Make a interractive dashboard???

def iterate(classes, num_max_image=100, num_model_training=1) :
    layer_sizing = [(32,), (64,), (128,), (64, 32), (128, 64), (128, 64, 32)]
    #Increasing data size
    for i in range(10,num_max_image + 1,10) :
        print(f"====== Images generated : {i*5} ======")
        #Incresing hidden layer number while decresing the number of neurons
        for y in range(6) :
            #Time the training of the model
            start = time.time()
            average, nRange = trainModel(n=num_model_training,n_ok=i,n_nok=i*4,layer_size=layer_sizing[y],classes=classes)
            end = time.time()
            print(f"Average and range for {i} image, {str(layer_sizing[y])}: {average} - {nRange}")
            #Save data
            c_time = (end - start)
            num_layers = len(layer_sizing[y])
            num_neurons = sum(layer_sizing[y])
            num_image = i * 5
            c_time = (end - start)
            evaluation = evaluate(average, nRange, num_image, num_neurons, c_time, num_max_image)
            Collector.save(evaluation=evaluation,average=average,nRange=nRange,n_image=num_image,
                n_layers = num_layers, n_neurons=num_neurons,computation_time=c_time)

#Get the average of n time of the same model.
def trainModel(n, n_ok=25, n_nok=100, layer_size=(220,), classes=2) :
    #init data
    total = 0
    average = 0
    nRange = 0
    minimum = float('inf')
    maximum = float('-inf')

    #Generate images and convert them into arrays
    Generator.main(generateImage=True,ok=n_ok,nok=n_nok,color=None)
    array_2x, array_2y = Analyser.main(classes)

    #Using the same data set, train the same model n times to collect average and deviation
    for i in range(n) :
        result = Classifier.train(array_2x,array_2y, layer_size)
        if result > maximum :
            maximum = result
        if result < minimum :
            minimum = result
        total += result

    #Delete the images folder for the next model
    deleteImageFolder()

    #Calculate the average and the deviation.
    average = total / n
    nRange = maximum - minimum

    return average, nRange

computation_time_min = float('inf')
computation_time_max = float('-inf')

def evaluate(average, nRange, n_image, n_neurons, computation_time,num_max_image) :
    #Used to dynamically scale the computation time
    global computation_time_min, computation_time_max
    computation_time_min = min(computation_time_min, computation_time)
    computation_time_max = max(computation_time_max, computation_time)

    if computation_time_min == computation_time_max :
        computation_time_max += 1

    #Scale the parameters
    nRange = min_max_scale(nRange, 0, 100)
    n_image = min_max_scale(n_image, 10,num_max_image)
    n_neurons = min_max_scale(n_neurons, 32, 224)
    computation_time = min_max_scale(computation_time,computation_time_min,computation_time_max)
    
    #Calculation
    memory_weight = 1/3
    time_weight = 1/3
    result_weight = 1/3
    memory_eval = (80 * n_image)/100 + (20 * n_neurons)/100
    time_eval = computation_time
    result_eval = ((60 * average)/100 + (40 * nRange)/100)
    total_eval = ((memory_weight * -(memory_eval)) + (time_weight * time_eval) + (result_weight * result_eval))
    print(f'===== {memory_eval} + {time_eval} + {result_eval} = {total_eval * 100}')
    return total_eval

def main():
    iterate(num_max_image=200, classes=2, num_model_training=1)
    Collector.deleteData()
    #Exemple of DataCollector.py
    #Collector.save(10,10,10,10,10,10,10)
    #Collector.deleteData()

def deleteImageFolder() :
    try:
        folder_path1 = 'OK'
        folder_path2 = 'NOK'
        shutil.rmtree(folder_path1)
        shutil.rmtree(folder_path2)
    except:
        print('One of the image folder could not be deleted')

def min_max_scale(value, min_value, max_value) : 
    return (value - min_value)/(max_value - min_value)

if __name__ ==  "__main__" :
    sys.exit(main())