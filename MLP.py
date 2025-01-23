import CapGenerator as Generator
import ImageCapAnalyser as Analyser
import sys

def main():
    Generator.main()
    array_x, array_y = Analyser.main()
    print(array_x)
    print("============")
    print(array_y)

if __name__ ==  "__main__" :
    sys.exit(main())