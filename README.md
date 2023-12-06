Image-Classification-December-
# Image Classification with CIFAR-10 Dataset

# Overview
This repository contains code for image classification using the CIFAR-10 dataset. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 different classes. 
The goal of this project is to build and train a deep learning model that can accurately classify these images into their respective categories.

# Prerequisites

- Python 3.x
- TensorFlow
- Keras
- Matplotlib
- NumPy

# Dataset
Download the CIFAR-10 dataset from the official website or use the provided script:

* Code: from tensorflow.keras.datasets import cifar10
* Link: https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

# Model Architecture
The model architecture consists of simple artificial neural networks which consists of conv2D layers, MaxPooling layers, Flattern Layers and Dense Layers.

# NETWORK TOPOLOGY 
* # Input Layer:
Shape: (32, 32, 3) - This corresponds to the dimensions of the CIFAR-10 images (32 pixels in height, 32 pixels in width, and 3 color channels for RGB).

* # Hidden Layer:
* Convolutional Layer:
 - Filters: 32
 - Kernel/Filter Size: (3, 3)
 - Activation Function: ReLU
* Pooling Layer:
 - MaxPooling with a pool size of (2, 2)
* Flatten Layer:
 - It flattens the input into a 1D array (Vector form)

* # Output Layer:
* Dense Layer:
  - Neurons: 10 (equal to the number of classes in CIFAR-10)
  - Activation Function: Softmax
 
# Weights:
The weights for the convolutional layer are initialized randomly and updated during training. 
The dense layer has weights connecting the flattened output of the previous layer to the 10 output neurons. 

# Activation functions:
* Convolutional Layer : ReLu
* Output Layer: Softmax 
