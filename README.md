# 🔮 STREAMSAGE — Churn Prediction for Streaming Platforms

## 📌 Overview
**STREAMSAGE** is a machine learning-powered web application that predicts customer churn for small-to-mid-sized streaming platforms. Built using **Streamlit** and **CatBoost**, it enables users to upload customer datasets and receive churn predictions along with actionable retention strategies.

---

## 🎯 Objectives
- Predict customers likely to churn  
- Enable data-driven retention strategies  
- Provide an easy-to-use interface for non-technical users  

---

## ⚙️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **ML Model:** CatBoostClassifier  
- **Libraries:** pandas, numpy, scikit-learn, imbalanced-learn  

---

## 🚀 Key Features
- 📂 Upload CSV file for predictions  
- 🧠 Automatic feature engineering (handles missing engineered features)  
- 🔍 Optimized churn prediction (threshold = 0.3)  
- 💡 Personalized retention recommendations  
- 📊 Interactive data preview  
- 📥 Download predictions as CSV  
- 🎨 Clean dark-themed UI  

---

## 📊 Model Performance
| Metric        | Score |
|--------------|------|
| Accuracy     | ~85% |
| Precision    | ~46% |
| Recall       | ~77% |
| F1 Score     | ~58% |
| ROC-AUC      | ~82% |

> ⚠️ Threshold set to **0.3** to prioritize high recall and reduce missed churn cases.

---

## 📁 Input Requirements

### Required Columns
- `gender`
- `age`
- `no_of_days_subscribed`
- `weekly_mins_watched`
- `minimum_daily_mins`
- `maximum_daily_mins`
- `weekly_max_night_mins`
- `videos_watched`
- `maximum_days_inactive`
- `customer_support_calls`
- `multi_screen`
- `mail_subscribed`

> ⚠️ Missing engineered features will be automatically generated.

---

## 🧠 Feature Engineering
The system dynamically generates the following features:

- **subscription_tenure** → normalized subscription duration  
- **engagement_score** → user activity level  
- **consistency_score** → usage consistency  
- **night_owl_score** → late-night viewing behavior  
- **churn_risk_score** → combines inactivity & support calls  
- **multi_screen_score** → multi-device usage  
- **email_marketing_score** → email engagement  

---

## 🤖 Model Details
- Algorithm: **CatBoostClassifier**  
- Handles categorical features efficiently  
- Performs well on small datasets (~2500 records)  
- Threshold tuning applied for business optimization  

---

## 🔄 Workflow
1. Upload CSV dataset  
2. Data preprocessing & encoding  
3. Feature engineering (auto-generated if missing)  
4. Churn probability prediction  
5. Apply threshold (0.3)  
6. Generate retention recommendations  
7. View & download results  

---

## 💡 Business Impact
- Identifies high-risk customers early  
- Enables targeted retention strategies  
- Useful for startups without dedicated data science teams  

---

## ⚠️ Limitations
- Trained on a relatively small dataset  
- Rule-based recommendation system  
- Not deployed (runs locally via Streamlit)  

---

## 🔮 Future Improvements
- Integrate real-time streaming data  
- Deploy as a cloud-based API  
- AI-driven recommendation engine  
- Explore deep learning models (e.g., BERT)  

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
