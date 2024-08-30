
# AWS Machine Learning Engineer Capstone Project
## Overview
This is the final project of the [Udacity AWS Machine Learning Engineer Nanodegree Program](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).

The dataset contains simulated data that replicates customer behavior on the Starbucks rewards mobile app. Every few days, Starbucks sends offers to app users, which can range from simple advertisements to discounts or BOGO (buy one, get one free) deals. Some users may not receive any offers in certain weeks. The challenge lies in the fact that not all users receive the same offer. The task is to combine transaction, demographic, and offer data to identify which demographic groups respond best to different types of offers. This dataset is a simplified version of the actual Starbucks app, as the simulator only includes one product, whereas Starbucks sells a wide variety of items.

## Files and Folders
- `EDA.ipynb` - notebook for Exploratory data analysis, including visualizations
- `FeatureEngineering.ipynb` - notebook for feature engineering
- `ModelTraining.ipynb` - notebook for model training
- `data` - the dataset folder
- `dataloaders.pt` - dataloaders for loading PyTorch dataset
- `FNN.pt` - file containing the weights of the FNN model
- `RNN.pt` - file containing the weights of the RNN model
- `proposal.pdf` - proposal document
- `report.pdf` - report document


## How to Run
This project is developed in Python 3.10, with the following Libraries needing to be installed:  
- notebook 7.2.1
- numpy 1.24.4
- pandas 2.2.2
- matplotlib 3.6.3
- torch 2.0.0
- scikit-learn 1.4.0

Go through the files `EDA.ipynb`, `FeatureEngineering.ipynb`, and `ModelTraining.ipynb` and run the cells inside these files.

## References
https://github.com/silviomori/udacity-machine-learning-capstone-starbucks