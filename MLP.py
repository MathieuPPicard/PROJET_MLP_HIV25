import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import DataCollector as Collector
import MLP_Cla as Classifier
import numpy as np
import sys
import shutil
import time

np.set_printoptions(threshold=np.inf) 

N_INPUT = 17 * 17

###TODO###
# DELETE THE OK AND NOK FOLDER [X]
# Loop while increasing the number of 1-Data sizes, 2-number of hidden layer and 3-the number of neuronnes [X]
# The results of the models need to be save with DataCollector.py [X]
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
            average, nRange, test_time = trainModel(n=num_model_training,n_ok=i,n_nok=i*4,layer_size=layer_sizing[y],classes=classes)
            end = time.time()
            print(f"Average and range for {i} image, {str(layer_sizing[y])}: {average} - {nRange}")
            #Save data
            print(f'this is the test time in iterate : {test_time}')
            c_time = (end - start)
            num_layers = len(layer_sizing[y])
            num_neurons = sum(layer_sizing[y])
            num_image = i * 5
            Collector.save(average=average,nRange=nRange,n_image=num_image,
                n_layers = num_layers, n_neurons=num_neurons,computation_time=c_time , average_test_time=test_time)

#Get the average of n time of the same model.
def trainModel(n, n_ok=25, n_nok=100, layer_size=(220,), classes=2) :
    #init data
    total = 0
    average = 0
    nRange = 0
    total_test_time = 0
    minimum = float('inf')
    maximum = float('-inf')

    #Generate images and convert them into arrays
    Generator.main(generateImage=True,ok=n_ok,nok=n_nok,color=None)
    array_2x, array_2y = Analyser.main(classes)

    #Using the same data set, train the same model n times to collect average and deviation
    for i in range(n) :
        result, test_time = Classifier.train(array_2x,array_2y, layer_size)
        if result > maximum :
            maximum = result
        if result < minimum :
            minimum = result
        total += result
        total_test_time += test_time

    #Delete the images folder for the next model
    deleteImageFolder()

    #Calculate the average and the deviation.
    average = total / n
    nRange = maximum - minimum
    average_test_time = (total_test_time / n) * 1000

    return average, nRange, average_test_time

def main():
    iterate(num_max_image=300, classes=2, num_model_training=20)
    #Collector.graphic()
    #Collector.graphicx3()
    #Collector.deleteData()

def deleteImageFolder() :
    try:
        folder_path1 = 'OK'
        folder_path2 = 'NOK'
        shutil.rmtree(folder_path1)
        shutil.rmtree(folder_path2)
    except:
        print('One of the image folder could not be deleted')

if __name__ ==  "__main__" :
    sys.exit(main())