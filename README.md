# Advanced House Prediction Project
## Project Overview

- This project aims to build a predictive model for estimating house prices based on over 80 various features, such as size, number of rooms, and location. Accurate house price predictions are valuable for buyers, sellers, and real estate professionals, enabling informed decision-making in the real estate market.
<p align="center">
  <img src="https://github.com/nnbankdeyu/Advanced-House-Price-Prediction/blob/main/Output%20Images/Project%20Image.png" alt="Image">
</p>


- To achieve this, we developed and evaluated three different models—**Ridge**, **Lasso**, and **Elastic Net**—achieving _**R-squared scores**_ of _**86.131%**_, _**87.189%**_, and _**86.131%**_ respectively, and _**MSE**_ values of _**0.245%**_, _**0.223%**_, and _**0.223%**_. Feature importance was analyzed using Recursive Feature Elimination (**RFE**), Variance Inflation Factor (**VIF**), and coefficient analysis in regression models to identify the most influential factors. The final result is a user-friendly **Streamlit** web application that allows users to input features and select a model for price predictions.

## Table of Contents
1. Problem Statement
2. Project Goals
3. Dataset
4. Data Preprocessing
5. Models
6. App Features
7. Installation
8. Usage
9. Results
10. Future Improvements
11. Contributors

## Problem Statement
- **Objective**: Build a predictive model for house prices based on various features (e.g., house size, age of house, number of rooms, number of fireplaces, etc.).
- **Problem**: House prices depend on numerous factors with differing levels of influence, making it challenging to identify the most impactful variables.
- **Key Question**: Which features most significantly affect house prices, and how can they be used to build an accurate prediction model?

## Project Goals
- **Model Development**: Train and evaluate Ridge, Lasso, and Elastic Net models for predicting house prices.
- **Feature Analysis**: Identify critical features influencing house prices using RFE, VIF, and regression model coefficients.
- **Streamlit Application**: Create an interactive web application for users to input house features, select a model, and receive predictions.

## Dataset

The dataset used in this project comes from the Kaggle competition "House Prices - Advanced Regression Techniques". 

Link to Advanced House Price Prediction dataset on Kaggle: [here](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).

It includes various features that may influence house prices, including:
- Numerical features: `LotFrontage`, `LotArea`, `OverallQual`, etc.
- Categorical features: `MSSubClass`, `Street`, `Neighborhood`, etc.

This comprehensive dataset offers a diverse range of characteristics to capture the nuances of the real estate market, making it well-suited for developing robust predictive models.

### Data Preprocessing
Data preprocessing is crucial for preparing the dataset for model training. The following steps were taken:

**1. Handling Missing Values**:
- Imputed missing values based on column data types, using median for numerical features and mode for categorical ones.

**2. Encoding Categorical Variables**:
- Applied label encoding for ordinal categorical variables (e.g., condition rating).
- Used one-hot encoding for nominal categorical variables (e.g., location, property type) to convert them into binary columns.

**3. Scaling Features**:
- Scaled numerical features (e.g., size, age, number of rooms) using StandardScaler to standardize the feature values for better model performance.

**4. Feature Engineering**:
+ Created new features from existing ones, such as “house age” (by subtracting the construction year from the current year).
+ Applied polynomial features for variables showing non-linear relationships with house price (e.g., square footage).
Removing Outliers:
+ Detected outliers using IQR methods, especially for high-variance features like house size, and removed extreme values to improve model stability.

**5. Feature Selection**:
- Applied RFE to select the most impactful features for model performance.
- Used VIF to remove features with high multicollinearity.
- Excluded variables with imbalanced distributions, where over 90% of the data consisted of a single unique value, as they lacked significance.

## Models
This project includes _three regression models_ for price prediction:

**1. Ridge Regression**:
Penalizes high coefficients to prevent overfitting, especially useful when features are highly correlated.

**2. Lasso Regression**:
Sets some feature coefficients to zero, effectively selecting a subset of features.

**3. Elastic Net Regression**:
Combines Ridge and Lasso, balancing between feature selection and preventing overfitting.

## Model Performance
- **Ridge Regression**: R-squared = 86.78%, MSE = 0.245%
- **Lasso Regression**: R-squared = 86.131%, MSE = 0.223%
- **Elastic Net Regression**: R-squared = 86.131%, MSE = 0.223%
<p align="center">
  <img src="https://github.com/nnbankdeyu/Advanced-House-Price-Prediction/blob/main/Output%20Images/Model%20Performance.png" alt="Model Performance">
</p>


Additionally, feature importance was examined using:

- **Recursive Feature Elimination (RFE)**: Sequentially removed features to determine the optimal set of predictors.
- **Variance Inflation Factor (VIF)**: Identified and removed multicollinear features.
- **Coefficient Analysis**: Used coefficients from Ridge, Lasso, and Elastic Net models to assess feature impacts.

## App Features
The Streamlit application allows users to:

- **Input House Features**: Select house size, number of rooms, location, etc.
- **Choose Prediction Model**: Select from Ridge, Lasso, or Elastic Net models.
```python
# Function to load models
@st.cache_data()
def load_model(file_path):
    model = joblib.load(file_path)
    return model
# Model selection
model_options = {"Ridge Regression": ridge_model, "Elastic Net": elastic_net_model}
model_choice = st.selectbox("Choose a model for prediction", list(model_options.keys()))
model = model_options[model_choice]
```
- **Get Price Prediction**: View the predicted price based on selected features.
```python
# Predict button
if st.button("Predict"):
    prediction = model.predict([input_features])  # Provide a list containing input_features
    st.write("Predicted House Price: $", round(prediction[0], 2))
```

## Demo
Below is the demo of House Price Prediction App using Streamlit with simple interface that allows to input features of a house and get the prices as the out based on the features.
<p align="center">
  <img src="https://github.com/nnbankdeyu/Advanced-House-Price-Prediction/blob/main/Output%20Images/demo_app_1.png" alt="demo_app_1">
</p>
<p align="center">
  <img src="https://github.com/nnbankdeyu/Advanced-House-Price-Prediction/blob/main/Output%20Images/demo_app_2.png" alt="demo_app_2">
</p>

Link to Full Demo App with PDF format: [here](https://github.com/nnbankdeyu/Advanced-House-Price-Prediction/blob/main/Output%20Images/ridge_app.pdf)
## Usage
- **Model Training**: Open House_Price_Prediction.ipynb and run the cells to train the Ridge, Lasso, and Elastic Net models.
- **Feature Importance Analysis**: Follow the steps in the notebook to explore feature importance using RFE, VIF, and regression coefficients.
- **App Interface**: Use the Streamlit app to input features, choose a model, and view predictions.

## Results
The Ridge, Lasso, and Elastic Net models were evaluated for accuracy, and feature importance analysis highlighted the most influential factors for house prices, such as:

- Size and location were consistently among the top predictors.
- Feature Importance Findings: RFE and VIF indicated that size (`GarageArea`, `LotArea`, `LotFrontage`), location (`Neighborhood`), and number of rooms/bathes/fireplaces were key determinants in price variation.

## Future Improvements
Future enhancements could include:

- **Model Optimization**: Fine-tuning models for better performance.
- **Additional Models**: Testing with more advanced models (e.g., neural networks).
- **Enhanced App Features**: Adding charts for feature importance visualization and interactive model comparisons.

  
## Contributors
Name: [Nhi Nguyen](https://github.com/nnbankdeyu)
