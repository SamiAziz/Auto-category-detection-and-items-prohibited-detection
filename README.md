# Auto-category-detection-and-items-prohibited-detection
Sami Aziz

## Abstract
The goal of this project is to create models to avoid prohibited items in marketplaces by using classification models to predict the prohibited items and help marketplaces auto avoiding the violence of items. I worked with data provided by [CIFAR 10](https://www.cs.toronto.edu/~kriz/cifar.html) as the first phase and then created my own dataset in the local machine. 

## Design
The data is provided by [CIFAR 10](https://www.cs.toronto.edu/~kriz/cifar.html) for first phase and i created my own dataset all these are for image model. Then created text dataset for items.
I implemented two seperate models,the first for  **Image classification**,and the second **Text classification**. 
**1. Image classification**: Classifying any item image user inserted by using Convolutional Neural Network (CNN).
**2. Text classification**: Classifying any item title user typed by using K-Nearest Neighbors (KNN).

As last step, i tried to deploy these model as flask API to make it live.

## Data
The image dataset contains 60,000 32x32 color images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images. And Text dataset contains ~ 800 points, it's just a group of words as (prohibited, non-prohibited). 

## Algorithms

*Models*
  
Convolutional Neural Network (CNN), K-Nearest Neighbors (KNN).

*Model Evaluation and Selection*
  
The entire image training datasets of 60,000 and my own dataset were split into 80 train/20 validation. And for Text dataset was split into 80 train/20 test, and all scores reported below.

The official metric was classification rate (accuracy).

**Image Classification CNN scores:** 
   -  Accuracy 96.73 %
    I think it takes high accuracy because the images dataset that I have created is small.

**Text Classification KNN scores:** 
   - Accuracy 87.24 %
   - F1 0.81 micro
   - precision 0.79
   - recall 0.86 micro

## Tools
- Numpy and Pandas
- Scikit-learn
- Matplotlib and Seaborn
- Tensorflow
- Flask
- Pickle
- NLTK
- RE
- Os

## Communication
- Text Classification, ![Text Classification](https://github.com/SamiAziz/Auto-category-detection-and-items-prohibited-detection/blob/main/assets/text_classification.png)
- Image Classification, ![Image Classification](https://github.com/SamiAziz/Auto-category-detection-and-items-prohibited-detection/blob/main/assets/image_classification.png)
- Web homepage, ![Homepage](https://github.com/SamiAziz/Auto-category-detection-and-items-prohibited-detection/blob/main/assets/homepage.png)
