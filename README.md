# Auto-category-detection-and-items-prohibited-detection
Sami Aziz

## Abstract
The goal of this project was to create models to avoid prohibited items in marketplaces by using classification models to predict the prohibited items and help marketplaces auto avoiding the violance of items. I worked with data provided by [CIFAR 10](https://www.cs.toronto.edu/~kriz/cifar.html) as first phase and then created my own dataset in local machine.    

## Design
The data is provided by [CIFAR 10](https://www.cs.toronto.edu/~kriz/cifar.html) for first phase and i created my own dataset all these are for image model. Then created text dataset for items.
I implemented two seperate models,the first for  **Image classification**,and the second **Text classification**. 
**1. Image classification**: Classifying any item image user inserted by using Convolutional Neural Network (CNN).
**2. Text classification**: Classifying any item title user typed by using K-Nearest Neighbors (KNN).

As last step, i tried to deploy these model as flask API to make it live.

## Data
Image dataset contains of 60,000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images. And Text dataset contains ~ 800 points, its just group of words as (prohibited, non-prohibited). 

## Algorithms

*Feature Engineering*
1. Mapping latitude and longitude to 3-dimensional coordinates so nearby continuous values would also be close in reality
2. Converting categorical features to binary dummy variables
3. Combining particular dummies and ranges of numeric features to highlight strong signals and illogical values for waterpoint status identified during EDA
4. Selecting subsets of the total unique values for categorical features that were converted to dummies, according to the number of samples they were associated with and their contribution to certain statuses

*Models*
  
Convolutional Neural Network (CNN), K-Nearest Neighbors (KNN).

*Model Evaluation and Selection*
  
The entire image training datasets of 60,000 and my own dataset were split into 80 train/20 validation. And for Text dataset was split into into 80 train/20 test, and all scores reported below.

The official metric was classification rate (accuracy).

**Image Classification CNN scores:** 
   -  Accuracy 96.73 %
    I think it takes high accuracy because the images dataset that i have created is small.

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
- Text Classification, [Text Classification](https://github.com/SamiAziz/Auto-category-detection-and-items-prohibited-detection/blob/main/assets/text_classification.png)
- Image Classification, [Image Classification](https://github.com/SamiAziz/Auto-category-detection-and-items-prohibited-detection/blob/main/assets/image_classification.png)
- Web homepage, [Homepage](https://github.com/SamiAziz/Auto-category-detection-and-items-prohibited-detection/blob/main/assets/homepage.png)
