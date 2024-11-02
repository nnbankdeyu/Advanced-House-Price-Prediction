# Advanced House Prediction Project
## Project Overview

- This project aims to build a predictive model for estimating house prices based on various features, such as size, number of rooms, and location. Accurate house price predictions are valuable for buyers, sellers, and real estate professionals, enabling informed decision-making in the real estate market.

- To achieve this, we developed and evaluated three different models—**Ridge**, **Lasso**, and **Elastic Net**—achieving _**R-squared scores**_ of _**86.131%**_, _**87.189%**_, and _**86.131%**_ respectively, and _**RMSE**_ values of _**0.245%**_, _**0.223%**_, and _**0.223%**_. Feature importance was analyzed using Recursive Feature Elimination (**RFE**), Variance Inflation Factor (**VIF**), and coefficient analysis in regression models to identify the most influential factors. The final result is a user-friendly **Streamlit** web application that allows users to input features and select a model for price predictions.

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
