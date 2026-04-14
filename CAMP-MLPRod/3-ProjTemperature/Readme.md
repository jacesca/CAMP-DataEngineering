# Predicting Temperature in London
Perform a machine learning experiment to find the best model that predicts the temperature in London!

## Project Description
As the climate changes around the world, the ability to predict changing weather is becoming more and more important.

In this project you will work on predicting the mean temperature in London. You will import, preprocess, and explore historical weather data and automate the training and evaluation of multiple machine learning models. This will be setup in an automated workflow using functions, utilizing methods from sklearn and MLflow.

## Project Task
Use machine learning to predict the mean temperature in London, England, logging your root mean squared error (RMSE) metrics using mlflow.

Build a model to predict "mean_temp" with a RMSE of 3 or less.
Use MLflow to log any models you train, their hyperparameters, and respective RMSE scores (ensuring you include "rmse" as part of the metric name).
Search all of your mlflow runs and store the results as a variable called experiment_results.

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/ForcastTempLondonProject.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```
