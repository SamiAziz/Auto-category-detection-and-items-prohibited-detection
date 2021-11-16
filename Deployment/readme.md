
# Flask-Deployment
###### This is a demo project to implement my project Models on production using Flask API
-------------------------------------------------------------------------------------------------
## Prerequisites
You must install:
1. NumPy library.
2. Tensorflow library.
3. Pandas library.
4. Flask (for API).
5. Pickle library.

## Deployment Structure
This Folder has four major parts :

- app.py -- This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
- image-model.h5 -- This contains Image Classification model to predict inserted product image file.
- text-model.pkl -- This contains Text Classification model to predict inserted product title.
- templates -- This folder contains the index HTML template to allow user to enter product title and image.


## Running the project
Ensure that you are in the project home directory, then open the (CMD/Terminal) then run:
```
python app.py using below command to start Flask API.
```
By default, flask will run on port 5000 so open your browser and navigate to URL http://localhost:5000

You should be able to view the homepage as below :

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

## Ok, you are ready now to use models.
