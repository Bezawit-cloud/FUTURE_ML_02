# 📞 Telecom Churn Predictor  📞 
### ⚡ **Keeping customers is more valuable than acquiring new ones.**

In the telecom industry, companies spend millions acquiring customers — but many still leave for competitors.  
This loss, called **customer churn**, directly affects a company’s growth and revenue.

Imagine a telecom provider losing 5% of its customers every month.  
What if it could **predict who’s likely to leave next**, and intervene before that happens?

This project tackles that challenge by building an intelligent **machine learning model** that predicts customer churn based on service usage, contract type, and demographic data — helping telecoms make proactive retention decisions.

## 🎯 **Live Demo**
👉 [**Launch Streamlit App**](#)  
*(https://futureml02-ywxtwftgrdivqguw3uuxfr.streamlit.app/)*  

---
##  **Overview**
This project predicts **customer churn** for a telecom company using machine learning.  
The workflow includes:
- Data preprocessing  
- Exploratory Data Analysis (EDA)  
- Handling unbalanced data using **SMOTE**  
- Comparing multiple ML models (Random Forest vs XGBoost)  
- Selecting the best model for deployment via **Streamlit**

##  **Workflow & Methodology**

###  Data Cleaning & Preprocessing
- Removed unnecessary columns  
- Converted `TotalCharges` to float  
- Filled missing values  
- Encoded categorical columns using LabelEncoder  

###  Exploratory Data Analysis (EDA)
- Correlation heatmap for relationships  
- Boxplots to detect outliers  
- Visualized service usage vs churn  
- Distribution analysis of tenure, contracts, and payment methods  

###  Handling Class Imbalance
- Detected imbalance in `Churn` column  
- Applied **SMOTE (Synthetic Minority Oversampling Technique)**  
- Balanced dataset improved recall for minority class  

###  Model Building & Comparison
- Trained and compared **Random Forest** and **XGBoost** classifiers  
- Used 80/20 train-test split  
- Evaluated performance using **Accuracy**, **Precision**, **Recall**, and **F1-Score**

---

##  **Model Evaluation**

| Metric | Random Forest | XGBoost |
|:--------|:--------------:|:-------:|
| Accuracy | 0.82 | **0.86** |
| Precision | 0.79 | **0.84** |
| Recall | 0.77 | **0.85** |
| F1-Score | 0.78 | **0.85** |

- XGBoost performed best overall and was chosen for final deployment  
- A **confusion matrix** and **classification report** supported this selection  

##  **Model Deployment**

After selecting the best-performing model (XGBoost):  
1. The trained model and encoders were **saved using `pickle`**:  
   - `customer_churn_model.pkl` → trained model  
   - `encoders.pkl` → label encoders for categorical data  
2. The Streamlit app (`streamlit_app.py`) loads these files to perform live predictions.  
3. Inputs from users are encoded and aligned with the training features.  
4. The model predicts whether a customer will **Stay ✅** or **Churn 🚨**.  
5. Deployed to **Streamlit Cloud** for easy public access.

  
## 🌟 **Key Features**
✅ Predicts if a customer will **Stay** or **Churn**  
✅ Displays **churn probability score** for better understanding  
✅ Integrates **EDA insights** visually  
✅ Handles both **categorical and numerical data**  
✅ Deployable on **Streamlit Cloud or Heroku**

feature_names = model_data["features_names"]

