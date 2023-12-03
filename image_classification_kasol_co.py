# -*- coding: utf-8 -*-
"""Image Classification-Kasol Co

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qu9M9iu0PP_yNjuHy8geq2R395RcB8tP
"""

pip install tensorflow

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

# CIFAR-10 dataset
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
train_images = train_images / 255
test_images = test_images / 255

train_labels = to_categorical(train_labels, num_classes=10)
test_labels = to_categorical(test_labels, num_classes=10)

# neural network model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.2)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')

predictions = model.predict(test_images[:10])

# CIFAR-10 class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Display the predictions
plt.figure(figsize=(10,10))
for i in range(min(6, len(test_labels))):
    plt.subplot(2, 3, i + 1)
    plt.imshow(test_images[i], interpolation='nearest')
    plt.title(f"True: {class_names[np.argmax(test_labels[i])]}, Predicted: {class_names[np.argmax(predictions[i])]}")
    plt.axis('off')
plt.show()