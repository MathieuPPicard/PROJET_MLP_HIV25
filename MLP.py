import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import sys

def main():
    Generator.main(generateImage=True,ok=4,nok=4,color=None)

    array_2x, array_2y = Analyser.main(2)
    print(array_2x)
    print(array_2y)

    array_5x, array_5y = Analyser.main(5)
    print(array_5x)
    print(array_5y)

    # Loop while augmenting the number of images to train, the number of hidden layer and the number of neuronnes
    # The results of the models need to be save
    # With the result plot and analyse the best combinaison of factors.
    # Make a interractive dashboard???


if __name__ ==  "__main__" :
    sys.exit(main())