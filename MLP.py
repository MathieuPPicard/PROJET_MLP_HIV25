import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import sys

def main():
    Generator.main(generateImage=True,ok=4,nok=4,color=None)

    array_2x, array_2y = Analyser.main(2)

    array_5x, array_5y = Analyser.main(5)


if __name__ ==  "__main__" :
    sys.exit(main())