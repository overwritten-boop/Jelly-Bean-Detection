#imports libraries to be used later in the program
import jetson.inference
import jetson.utils

import argparse

#creates a parser object to translate the command line to variables
parser = argparse.ArgumentParser()


#ONLY UNCOMMENT IN NEED OF EMERGENCY
#adds the arguments to the cmd command
#allows for arguments given in the command line to be taken as variables
#parser.add_argument("filename", type=str, help="filename of the image to process")
#parser.add_argument("--network", type=str, default="gowbaoglenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")

#creates a parser object that allows the command line variables to be passed into the program
opt = parser.parse_args()

#loads the image passed in the parameters
input = jetson.utils.videoSource("/dev/video0")

#gets the network from the file path provided in the parameters
net = jetson.inference.imageNet("beans/resnet18.onnx")

while True:
    #gets the input from the
    img = input.Capture()

    #begins the classification network process
    #assigns the class that is most probable as class_idx(str), and the confidience as confidence(int)
    class_idx, confidence = net.Classify(img)

    class_desc = net.GetClassDesc(class_idx)
    if(class_desc == "LIQUORICE"):
        #here any result from detecting the bean flavor
        print("WARNING >>> YUCKY BEAN DETECTED")
