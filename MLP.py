import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import DataCollector as Collector
import MLP_Cla as Classifier
import numpy as np
import sys

N_INPUT = 17 * 17

###TODO###
# DELETE THE OK AND NOK FOLDER EACH TIME AT THE END OF CapGenerator main
# Loop while increasing the number of 1-Data sizes, 2-number of hidden layer and 3-the number of neuronnes [X]
# The results of the models need to be save with DataCollector.py
# With the results, plot and analyse the best combinaison of factors.
# Make a interractive dashboard???

def iterate(num_max_layer, num_max_image, classes, num_model_training=1) :
    layer_sizing = []
    size = N_INPUT
    #Increasing data size
    for i in range(10,num_max_image+1,10) :
        print(f"Images genere : {i*2}")
        #Incresing hidden layer number while decresing the number of neurons
        for y in range(1,num_max_layer+1,1) :
            layer_sizing.append(int(np.floor(size/y)))
            result = getAverage(num_model_training,i,i,tuple(layer_sizing),classes)
            print(f"Average for {y} layers: {result}")    
            #
            # Add the collection of data here.
            # Will need average, Standard deviation, time of computation, number of images used, number of hidden layers, number of neurons(total) and how may classes  
            # Collector.save()
            #
            
        layer_sizing = []

#Get the average of n time of the same model.
def getAverage(n, n_ok=25, n_nok=100, layer_size=(220,), classes=2) :
    Generator.main(generateImage=True,ok=n_ok,nok=n_nok,color=None)
    array_2x, array_2y = Analyser.main(classes)
    total = 0
    for i in range(n) :
        result = Classifier.train(array_2x,array_2y, layer_size)
        total += result
    return total / n

def main():
    iterate(num_max_layer=6, num_max_image=167, classes=2, num_model_training=1)

    #array_5x, array_5y = Analyser.main(5)
    #print(array_5x)
    #print(array_5y)
    #Classifier.train(array_5x,array_5y) 

if __name__ ==  "__main__" :
    sys.exit(main())