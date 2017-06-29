import numpy as np  
import pandas as pd  
from processing_functions import *
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from support_functions import *
from Autoencoder_Functions import *

## Parameters
n_components=30 # 30 components in the encoded matrix
anomaly_digit = 2

## Pre-Process Data
# Read data
data_path = 'data/input_data/'
# Read image matrix (n*m), labels (vector of m), and image size
imgs_train, imgs_test, labels_train, labels_test, height, width = read_process_data(data_path, anomaly_digit)
# The length of one image vector
img_size = height*width 

# Specify the model config
encoder_layers_size, decoder_layers_size = get_deep_model_config()

# Merge the data
imgs = np.concatenate((imgs_train, imgs_test))
labels = np.concatenate((labels_train, labels_test))

# Train and compile the model
autoencoder,encoder = train_autoencoder(imgs, labels,encoder_layers_size,decoder_layers_size,save_model = True)

