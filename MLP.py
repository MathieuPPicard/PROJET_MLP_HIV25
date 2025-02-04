import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import DataCollector as Collector
import MLP_Cla as Classifier
import numpy as np
import sys
import shutil

N_INPUT = 17 * 17

###TODO###
# DELETE THE OK AND NOK FOLDER [X]
# Loop while increasing the number of 1-Data sizes, 2-number of hidden layer and 3-the number of neuronnes [X]
# Use data augmentation to get less overfitting
# Create a evaluation function(weigh the following : average, standard deviation, time of computation, number of image)
# The results of the models need to be save with DataCollector.py
# With the results, plot and analyse the best combinaison of factors.
# Make a interractive dashboard???

def iterate(classes, num_max_image=100, num_model_training=1) :
    layer_sizing = [(64, 32), (128, 64), (128, 64, 32)]
    #Increasing data size
    for i in range(10,num_max_image + 1,10) :
        print(f"Images genere par classes : {i}")
        #Incresing hidden layer number while decresing the number of neurons
        for y in range(3) :
            result = trainModel(n=num_model_training,n_ok=i,n_nok=i*4,layer_size=layer_sizing[y],classes=classes)
            print(f"Average for {i} image, {str(layer_sizing[y])}: {result}")
            #
            # Add the collection of data here.
            # Will need eval fonction ,average , Standard deviation, time of computation, number of images used, number of hidden layers, number of neurons(total) and how may classes  
            # Collector.save()
            #

#Get the average of n time of the same model.
def trainModel(n, n_ok=25, n_nok=100, layer_size=(220,), classes=2) :
    Generator.main(generateImage=True,ok=n_ok,nok=n_nok,color=None)
    array_2x, array_2y = Analyser.main(classes)
    total = 0
    for i in range(n) :
        result = Classifier.train(array_2x,array_2y, layer_size)
        total += result
    deleteImageFolder()
    return total / n

def deleteImageFolder() :
    try:
        folder_path1 = 'OK'
        folder_path2 = 'NOK'
        shutil.rmtree(folder_path1)
        shutil.rmtree(folder_path2)
    except:
        print('One of the image folder could not be deleted')

def main():
    iterate(num_max_image=200, classes=2, num_model_training=1)

if __name__ ==  "__main__" :
    sys.exit(main())