# 🏦 Loan Amount Prediction
This project predicts the loan amount using applicant information and machine learning.

## Project Overview
The dataset contains information about loan applicants, such as:

 Gender
 Married
 Dependents
 Education
 Self Employed
 Applicant Income
 Coapplicant Income
 Loan Amount Term
 Credit History
 Property Area

A new feature called `TotalIncome` was created using Applicant Income and Coapplicant Income.

## Machine Learning Models
The following regression models were tested:
1) Linear Regression
2) Random Forest Regression
3) Gradient Boosting Regression

Gradient Boosting produced the best results in this experiment.

## Best Model

Gradient Boosting:

 MAE: 31.57
 RMSE: 50.23
 R²: 0.3155

## Web Application

The trained model is deployed using Streamlit.

The application allows users to enter applicant information and receive a predicted loan amount.

## Technologies Used

 Python
 Pandas
 NumPy
 Scikit-learn
 Joblib
 Streamlit
