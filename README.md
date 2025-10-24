Telecom Churn Predictor 🚀

Keeping customers is more valuable than acquiring new ones.

In the highly competitive telecom industry, companies invest millions in acquiring customers, but many still leave for competitors. This loss — known as customer churn — directly impacts revenue and growth.

Imagine a telecom company noticing a steady outflow of subscribers each month. Which customers are likely to leave next? How can the company intervene proactively to retain them?

This project tackles that challenge by building a machine learning model to predict customer churn. By analyzing customer behavior, contract types, and usage patterns, the model helps the company identify at-risk customers and take action before they leave.

Table of Contents

Project Overview

Workflow & Methodology

Key Features

Tech Stack

Dataset

How It Works

Installation & Running

Usage

Future Enhancements

Contact

Project Overview

Telecom companies face a high risk of losing customers to competitors. This project leverages machine learning models to predict which customers are likely to churn, enabling proactive retention strategies.

The approach is data-driven and includes:

Exploratory Data Analysis (EDA) using correlation heatmaps, boxplots, and feature distributions

Handling unbalanced data in the target (Churn) using SMOTE

Model comparison between Random Forest Classifier and XGBoost Classifier

Selection of the best-performing model based on metrics

Deployment as an interactive Streamlit app

Workflow & Methodology

Data Cleaning & Preprocessing

Dropped unnecessary columns

Converted TotalCharges to float

Handled missing values and corrected data types

Exploratory Data Analysis (EDA)

Visualized relationships using correlation heatmaps

Used boxplots to identify outliers

Examined categorical distributions

Handling Class Imbalance

Observed an unbalanced target column (Churn)

Applied SMOTE (Synthetic Minority Oversampling Technique) to balance classes

Model Building & Comparison

Compared Random Forest Classifier vs XGBoost Classifier

Evaluated using accuracy, confusion matrix, and classification report

Chose the best-performing model for deployment

Model Saving & Deployment

Saved model and encoders using pickle

Built a Streamlit app for interactive predictions

Key Features

Predict whether a customer will stay or churn

Handles both numerical and categorical features

Displays churn probability for better decision-making

Interactive Streamlit app for live input

Includes EDA visualizations for insights

Tech Stack

Python 3.10+

Pandas & NumPy for data manipulation

Scikit-learn for preprocessing and modeling

XGBoost for boosting classifier comparison

Imbalanced-learn for SMOTE

Matplotlib & Seaborn for EDA visualizations

Streamlit for interactive web app

Pickle for saving/loading models

Dataset

Customer dataset including:

Demographics: gender, SeniorCitizen, Partner, Dependents

Account info: tenure, Contract, PaymentMethod, PaperlessBilling

Services: PhoneService, MultipleLines, InternetService, StreamingTV, etc.

Charges: MonthlyCharges, TotalCharges

Target: Churn (Yes/No)

How It Works

User inputs customer data in the Streamlit app

Categorical features are encoded using saved LabelEncoders

Input features are ordered to match training data

Random Forest model predicts churn and probability

Result displayed interactively: Stay ✅ or Churn 🚨

Installation & Running

Clone the repository:

git clone <your-repo-url>
cd Telecom-Churn-Predictor


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run streamlit_app.py


Ensure customer_churn_model.pkl and encoders.pkl are in the same folder as streamlit_app.py.

Usage

Enter customer details via input fields

Click Predict Churn

View prediction and churn probability

Optionally, check Show Input Details to verify inputs

Future Enhancements

Bulk upload for multiple customer predictions

Include feature importance charts for insights

Improve UI with color-coded probability bars and metrics

Deploy to Heroku or Streamlit Cloud for online access

Contact

Name: Esunma Bezawit

Email: [your-email@example.com
]

GitHub: [your-github-link]

LinkedIn: [your-linkedin-link]"# FUTURE_ML_02" 
